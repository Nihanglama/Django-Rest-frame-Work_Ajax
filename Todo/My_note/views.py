from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Task_serilize
from .models import Tasks


@api_view(['GET'])
def Apioverview(request):
    api_urls={
        'List':'/task-list/',
        'Detail/':'/task_detail/<str:pk>/',
        'create':'/Create_task/',
        'update/':'/task_update/<str:pk>/',
        'Delete/':'/task_delete/<str:pk>/',
        'Search/':'/task_search',
    }

    return Response(api_urls)

@api_view(['GET'])
def Task_list(request):
    task=Tasks.objects.all()
    serializer=Task_serilize(task,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def Task_search(request,name):
    task=Tasks.objects.filter(title__icontains=name)
    print(task)
    serializer=Task_serilize(task,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TaskDetail(request,pk):
    task =Tasks.objects.get(id=pk)
    serializer=Task_serilize(task,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Taskcreate(request):
    serializer=Task_serilize(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Taskupdate(request,pk):
    task=Tasks.objects.get(id=pk)
    serializer=Task_serilize(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Taskdelete(request,pk):
    task=Tasks.objects.get(id=pk)
    task.delete()
    return Response("Item deleted sucessfully")
