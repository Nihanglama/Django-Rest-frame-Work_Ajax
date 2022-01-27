from django.urls import path
from .views import Apioverview,Task_list, Task_search,TaskDetail,Taskcreate, Taskdelete, Taskupdate

urlpatterns = [
    path('',Apioverview,name='apioverView'),
    path('task_list/',Task_list,name='tasklist'),
    path('task_detail/<str:pk>/',TaskDetail,name='taskdetail'),
    path('task_create/',Taskcreate,name='taskcreate'),
    path('task_update/<str:pk>/',Taskupdate,name='taskupdate'),
    path('task_delete/<str:pk>/',Taskdelete,name='taskdelete'),
    path('task_search/<str:name>',Task_search,name='tasksearch'),
]
