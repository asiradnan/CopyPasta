from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import MainForm
from .models import MainModel


def home(request):
    return render(request, "home.html")

def copy(request):
    if request.method == "POST":
        key = request.POST.get("key")
        try:
            x = MainModel.objects.get(key=key)
            if (x.file):
                return render(request, "copy.html", {"data":x.data,"file":x.file})
            return render(request,"copy.html",{"data":x.data})
        except:
            return render(request, "copy.html", {"error":"Data not found"})

def paste(request):
    if request.method == "POST":
        key = request.POST.get("key")
        form = MainForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            print("Here")
            return render(request, "pasted.html",{"key":key})
        else:
            print(form)
            return render(request, "paste.html", {"form":form})
    form = MainForm()
    return render(request, "paste.html", {"form":form})


def preEdit(request):
    if request.method == "POST":
        key = request.POST.get("key")
        try:
            x = get_object_or_404(MainModel, key=key)
            print(x)
            request.session['key'] = key 
            return redirect(reverse('edit'))
        except:
            return render(request, "copy.html", {"error":"Data not found"})

def edit(request):
    obj = get_object_or_404(MainModel, key=request.session.get('key'))
    if request.method == "POST":
        key = request.POST.get("key")
        form = MainForm(request.POST, request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return render(request, "pasted.html",{"key":key})
        else:
            return render(request, "paste.html", {"form":form})
    form = MainForm(instance=obj)
    return render(request, "edit.html", {"form":form})
