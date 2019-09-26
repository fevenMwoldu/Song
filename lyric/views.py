from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Song
from .forms import SongForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user 

    custom_user = Song.objects.all()

    if custom_user is None:
        return HttpResponseRedirect('post')

    posts = Song.objects.all()

    
    return render(request, 'index.html', {"posts": posts})


@login_required(login_url='/accounts/login/')
def add_song(request):
    current_user = request.user

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.user = current_user
            custom_user.save()

            

            return HttpResponseRedirect('/')

    else:
        form = SongForm()

    return render(request, 'add_song.html', {"form": form})


def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_songs = Song.search_song(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"songs": searched_songs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})