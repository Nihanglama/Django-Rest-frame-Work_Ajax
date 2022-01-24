from django.shortcuts import render

def list_view(request):
    template='frontend/list.html'
    return render(request,template)