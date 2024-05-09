from django.urls import path
from . views import *
from . import views

urlpatterns=[path('',regis),
             path('success/',success),
             path('send/',send_mail_regis),
             path('error/',error),
             path('log/',login),
             path('verify/<auth_token>',verify),
             path('login/',login),
             path('create/',create),
             path('createtodo/', create_todo)

             , path('view/<str:project_title>/', views.view_project, name='view_project')
             ,path('viewdetail/<str:project_title>/', views.view_projectdetail, name='view_project'),
             path('edit/<str:todo_name>/',edit)
             ,path('delete/<str:todo_name>/',delete)


             ]
