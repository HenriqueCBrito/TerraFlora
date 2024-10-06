from django.shortcuts import render, redirect
from .models import Fazenda  # aq ele importa o modelo fazenda que a gente criou la em models

# view para exibir o formulario e processar o cadastro da fazenda
def cadastrar_fazenda(request):
    # ve se a requisição é post (submissao de formulario)
    if request.method == 'POST':
        # aq ele coleta os dados enviados pelo formulario usando request.POST.get
        nome_proprietario = request.POST.get('nome_proprietario')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        nome_fazenda = request.POST.get('nome_fazenda')
        localizacao = request.POST.get('localizacao')
        area_uso = request.POST.get('area_uso')

        # aq ele cria um novo objeto Fazenda com os dados do formulário 
        nova_fazenda = Fazenda(
            nome_proprietario=nome_proprietario,
            telefone=telefone,
            email=email,
            nome_fazenda=nome_fazenda,
            localizacao=localizacao,
            area_uso=area_uso
        )

        # vai salvar o novo objeto Fazenda no banco de dados
        nova_fazenda.save()

        # redireciona para a página de sucesso dps de salvar
        return redirect('fazenda_sucesso')

    # se a requisicao não for POST (primeira vez carregando o formulario), exibe o formulario
    return render(request, 'cadastro/cadastrar_fazenda.html')

# view para exibir a página de sucesso após o cadastro
def sucesso(request):
    # renderiza o template de sucesso
    return render(request, 'cadastro/sucesso.html')
