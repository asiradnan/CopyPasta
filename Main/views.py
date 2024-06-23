from django.shortcuts import render, get_object_or_404
from .forms import MainForm
from .models import MainModel


def home(request):
    return render(request, "home.html")

def copy(request):
    if request.method == "POST":
        key = request.POST.get("key")
        try:
            x = get_object_or_404(MainModel, key=key)
            return render(request, "copy.html", {"data":x.data})
        except:
            return render(request, "copy.html", {"error":"Data not found"})

def paste(request):
    if request.method == "POST":
        key = request.POST.get("key")
        form = MainForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            return render(request, "pasted.html",{"key":key})
        else:
            return render(request, "paste.html", {"form":form})
    form = MainForm()
    return render(request, "paste.html", {"form":form})

