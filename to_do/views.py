from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from to_do.models import Task

def login_page(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return HttpResponseRedirect('/task')
    else:
        formulario = AuthenticationForm(request.POST)
    return render_to_response('index.html', {'formulario': formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def tareas(request):
    tasks = Task.objects.all().exclude(estato='Culminado')
    taskCulminado = Task.objects.filter(estato='Culminado')
    if request.method == 'POST':
        estados = request.POST.getlist('estado')
        for estado in estados:
            dividido = estado.split('_')
            if dividido[1]=='':
                continue
            else:
                tarea = Task.objects.get(pk=dividido[0])
                tarea.estato=dividido[1]
                tarea.save()
    return render_to_response('task.html', {'tasks':tasks, 'taskCulminado':taskCulminado}, context_instance=RequestContext(request))