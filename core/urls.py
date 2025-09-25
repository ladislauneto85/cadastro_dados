from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario_view, name='perfil_usuario'),
    path('dashboard/', views.admin_visualizacao, name='admin_visualizacao'),
    path('usuario/<int:user_id>/', views.detalhe_usuario, name='detalhe_usuario'),
    path('dashboard/exportar/', views.exportar_excel_view, name='exportar_excel'),
    # A rota de cadastro completo pelo admin (opcional)
    path('cadastro-admin/', views.cadastro_admin_view, name='cadastro_admin'),
]