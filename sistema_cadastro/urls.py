from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Adiciona as URLs de mídia apenas em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Configurar Títulos Django Admin

admin.site.site_header = "Sistema de Cadastro"
admin.site.site_title = "ACESSO AO SISTEMA"
admin.site.index_title = "Ficha de Dados"