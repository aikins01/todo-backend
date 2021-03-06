from django.urls import path
from . import views 
 
urlpatterns = [ 
    path(r'todos/', views.todos_list),
    path(r'todos/<int:todo_id>/', views.todo_detail),
]
