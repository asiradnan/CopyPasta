from django.shortcuts import  render, redirect
from .forms import MainForm
from .models import MainModel
from django.contrib import messages
from django_ratelimit.decorators import ratelimit

def home(request):
    return render(request, "home.html")

def copy(request):
    if request.method == "POST":
        key = request.POST.get("key")
        try:
            x = MainModel.objects.get(key=key)
            return render(request,"copy.html", {"object":x})
        except:
            return render(request, "copy.html", {"error":"Data not found"})

def paste(request):
    if request.method == "POST":
        key = request.POST.get("key")
        form = MainForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            return render(request, "pasted.html",{"key":key,"object":x})
        else:
            return render(request, "paste.html", {"form":form})
    form = MainForm()
    return render(request, "paste.html", {"form":form})

def edit(request, pk):
    obj = MainModel.objects.get(pk=pk)
    if request.method == "POST":
        form = MainForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return render(request,"copy.html", {"object":obj})
    else:
        form = MainForm(instance=obj)
    return render(request, "paste.html", {"form":form, "object":obj})

def delete(request, pk):
    if request.method == "POST":
        obj = MainModel.objects.get(pk=pk)
        if obj is None:
            messages.error(request, "Data not found")
            return render(request, "delete.html")
        obj.delete()
        messages.success(request, "Data deleted successfully")
    return redirect("home")