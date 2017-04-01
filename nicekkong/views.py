from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import MyNumbers
from .form import PostForm


def index(request):
    print(str(request))
    # return render(request, "lotto/default.html", {"lottos": lottos})
    myNumbers = MyNumbers.objects.all()
    # print(myNumbers[1].name)
    return render(request, "nicekkong/index.html", {"myNumbers": myNumbers})


def insert(request):
    if(request.method == "POST"):
        form = PostForm(request.POST)
        if form.is_valid():
            myNumber = form.save(commit=False)
            myNumber.setCreateDate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, "nicekkong/insert.html", {"form": form})
