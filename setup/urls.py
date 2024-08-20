from django.contrib import admin
from django.urls import path
from escola.views import escola
from tipoatividade.views import cadastroTiposAtividade, listarTiposAtividade



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', escola, name='escola'),
    path('tipoatividade/', cadastroTiposAtividade, name='cadastroTiposAtividade'),
    path('tipoatividade/listar/', listarTiposAtividade, name='listarTiposAtividade'),

]
