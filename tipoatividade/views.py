from django.shortcuts import render

def cadastroTiposAtividade(request):
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

def listarTiposAtividade(request):
    return render(request, 'tipoatividade/listarTiposAtividade.html')