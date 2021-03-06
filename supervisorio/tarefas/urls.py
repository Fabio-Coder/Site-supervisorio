from django.urls import path
from supervisorio.tarefas import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:tarefa_id>', views.detalhe, name='detalhe'),
    path('delete/<int:tarefa_id>', views.delete, name='delete'),
]
