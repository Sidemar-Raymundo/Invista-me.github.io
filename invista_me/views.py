from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html', context = dados)


# deixei em comentário a função abaixo devido que estou colocando uma nova pagina inicial cujo ela mostra os investimentos para o usuario. isso é um treinamento
#def pagina_inicial(request): 
   # return HttpResponse('Pronto para investir ')

def contatos(request):
    return(HttpResponse('Aqui estão os contatos para voçê'))    


#FUNCÃO COMENTADA DEVIDO QUE A MESMA ERA APENAS PARA TESTES E TREINO.
# def minha_historia(request):
#     pessoa = {'nome': 'Side',
#               'idade': 34,
#               'hobby':'violao'
#     }


    return render(request,'investimentos/minha_historia.html',pessoa )


#DEIXEI COMENTADA A FUNÇÃO ABAIXO PORQUE ESTOU CRIANDO NOVOS INVESTIMENTO DINÂMICOS
#def novo_investimento(request):
    #return render(request, 'investimentos/novo_investimento.html')


def investimento_registrado(request):
    investimento = {'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html',investimento)


def detalhe(request, id_investimento):
    dados = {'dados': Investimento.objects.get(pk=id_investimento)}
    return render(request ,'investimentos/detalhe.html',dados)


@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')

    investimento_form = InvestimentoForm()
    formulario = {
        'formulario': investimento_form
    }
    return render(request, 'investimentos/novo_investimento.html', context = formulario)


@login_required
def editar(request ,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # novo_investimento/ -> GET
    if request.method =='GET':
        formulario = InvestimentoForm(instance=investimento)
    # caso requisição seja POST
    else:
        formulario = InvestimentoForm(request.POST, instance= investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    
    return render(request,  'investimentos/novo_investimento.html', {'formulario': formulario})


@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method =='POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request,  'investimentos/confirmar_exclusão.html',{'item':investimento})






    
