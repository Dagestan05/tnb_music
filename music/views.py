from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic

from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    #to overwrite default 'object_list'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    ''' this form lets users to create new albums.
    When doinng new template for this view create a new html with lowercase name of model,
    underscore form, ex.: album_form'''
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    ##after deleting and album his command down below will redirect us to music:index page
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    ##form_class is the blueprnt for our form
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #displays a blank form, i.e. before filling the info, i.e first time
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    ##processes form data, i.e. already filled data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            ##bellow code takes the data but dosnt save it to DB, but uses it locally
            user = form.save(commit=False)
            ## clean (normalized) data. Data formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            ##bellow code sets users password
            user.set_password(password)
            ## finally save the user
            user.save()

            ##returns user objects if there s such a user and credentials are correct
            user = authenticate(username = username, password = password)

            if user is not None:
                ## before they login we need to check if they are active, , not banned or etc
                if user.is_active:
                    login(request, user)
                    ## we need to redirect them somewhere after their login is successful
                    return redirect('music:index')

        ##if their login is not successful, we will tell them to try again
        return render(request, self.template_name, {'form': form})














































#BEFORE USING CLAS BASED VIEWS

# from django.http import Http404
# #shorter and easier way of loading templates
# from django.shortcuts import render, get_object_or_404
# ##No need for httpresponse, sonce we are using render
# from django.http import HttpResponse
# #first way of loading templates
# # #from django.template import loader
# from .models import Album, Song
#
#
# def index(request):
#     all_albums = Album.objects.all()
#     context = {"all_albums": all_albums}
#     return render(request, 'music/index.html', context)
#     # template = loader.get_template('music/index.html')
#     # context = {"all_albums": all_albums,}
#     # return HttpResponse (template.render(context, request))
#
# def detail(request, album_id):
#     # try:
#     #     album = Album.objects.get(id=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("<-<-<- ___ Album does not exist ! ! ! ___ ->->->")
#     ## following line is a shorter way of dispyaing 404
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {"album": album})
#
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "!!! You did not select a valid song"
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {"album": album})
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
