from django.urls import path
from django.views import View
from . import views
from .views import loginview
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('login/',loginview.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',views.registerPage,name='register'),

    path('',views.TaskList,name='task'),
    path('task/<int:pk>',views.TaskDetail,name='taskdetail'),
    path('create_task',views.createtask,name='cre-tsk'),
    path('update/<int:pk>',views.Update,name='update'),
    path('delete/<int:pk>',views.Delete,name='delete'),
]
