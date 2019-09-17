from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.messages import SUCCESS,ERROR
from django.http import HttpResponse
from .forms import Add_Show_Form

def index(request):
    show_list = Shows.objects.all()
    
    context = {
        "show_list_html": show_list
    }
    return render(request, "index.html", context)

def create_show(request):
    
    if len(request.POST["title"]) > 1 and len(request.POST["desc"]) > 5 and len(request.POST["network"]) > 1 and len(request.POST["relase_date"]) > 5:
        Shows.objects.create(title=request.POST["title"],network=request.POST["network"],relase_date=request.POST["relase_date"],desc=request.POST["desc"])
        messages.add_message(request, messages.INFO, "A New Show was added!")
    else:
        messages.add_message(request, messages.INFO, "Show could not be added. Make sure you enter a title and network and realse date and a description longer than five characters.")
    return redirect("/add_show")
def add_show(request):
    return render(request,"add_show.html")

def show(request,num):
    shows=Shows.objects.get(id=int(num))
    all_show=Shows.objects.all()
    context={
        "shows_html":shows,
        "all_show_html":all_show,
    }
    return render(request,"show.html",context)

def edit_show(request, num):
    # print(Show.objects.get(id=id).release_date)
    context = {
        "show": Shows.objects.get(id=num),
        "date": str(Shows.objects.get(id=num).relase_date)
    }
    # print(context["show"].release_date)
    return render(request, "edit_show.html", context)

def submit_edit(request, num):
    selected = Shows.objects.get(id=num)
    if request.POST['title']:
        selected.title = request.POST['title']
    
    if request.POST['network']:
        selected.network = request.POST['network']
    
    if request.POST['relase_date']:
        selected.release_date = request.POST['relase_date']
    
    if request.POST['desc']:
        selected.description = request.POST['desc']
    selected.save()
    return redirect(f'/show/{num}')

def delete_show(request, num):
    Shows.objects.get(id=num).delete()
    return redirect('/')