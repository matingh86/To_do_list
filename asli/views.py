from django.shortcuts import render ,redirect, get_object_or_404
from .models import to_do

# Create your views here.

def home(request):
    todo=to_do.objects.all()
    return render(request,"asli/home.html",context={"to_do":todo})

def add_work(request):
    if request.method=="POST":
        title=request.POST.get("title")
        day=request.POST.get("day")
        if title and day:
            to_do.objects.create(title=title,day=day)
    return redirect("home")

def del_work(request,id):
    todo=get_object_or_404(to_do,id=id)
    todo.delete()
    return redirect("home")
def complete_work(request,id):
    todo=get_object_or_404(to_do,id=id)
    todo.completed=True
    todo.save()
    return redirect("home")