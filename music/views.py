from django.http import Http404
#shorter and easier way of loading templates
from django.shortcuts import render, get_object_or_404
##No need for httpresponse, sonce we are using render
from django.http import HttpResponse
#first way of loading templates
# #from django.template import loader
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {"all_albums": all_albums}
    return render(request, 'music/index.html', context)
    # template = loader.get_template('music/index.html')
    # context = {"all_albums": all_albums,}
    # return HttpResponse (template.render(context, request))

def detail(request, album_id):
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("<-<-<- ___ Album does not exist ! ! ! ___ ->->->")
    ## following line is a shorter way of dispyaing 404
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {"album": album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "!!! You did not select a valid song"
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {"album": album})





















