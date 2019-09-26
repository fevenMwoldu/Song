from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Mezmur
from .forms import MezmurForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user 

    custom_user = Mezmur.objects.all()

    if custom_user is None:
        return HttpResponseRedirect('post')

    posts = Mezmur.objects.all()

    
    return render(request, 'index.html', {"posts": posts})


@login_required(login_url='/accounts/login/')
def add_song(request):
    current_user = request.user

    if request.method == 'POST':
        form = MezmurForm(request.POST, request.FILES)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.user = current_user
            custom_user.save()

            

            return HttpResponseRedirect('/')

    else:
        form = MezmurForm()

    return render(request, 'add_song.html', {"form": form})