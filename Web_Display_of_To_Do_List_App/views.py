from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem


def home(request):
    return HttpResponse('The Most Fabulous To-Do List')


# Create your views here.
def to_do(request):
    to_do_list = ToDoItem.objects.all()
    return render(request,'index.html', {"to_do_list": to_do_list})
