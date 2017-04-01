from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import GuessNumbers
from .form import PostForm1

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Nicekkong World</h1>")
    lottos = GuessNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos":lottos})


def post(request):
    if(request.method == "POST"):
        # Save Data
        form = PostForm1(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('/lotto')
    else:
        form = PostForm1()
        return render(request, "lotto/form.html", {"form" : form})


def detail(request, lottoKey):

    lotto = GuessNumbers.objects.get(pk = lottoKey)
    return render(request, "lotto/detail.html", {"lotto":lotto})