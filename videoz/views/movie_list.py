from django.views.generic import TemplateView, ListView

from videoz import Movie, VideoFile


class MovieList(ListView):
    template_name = 'movie_list.html'

    def get_queryset(self):
        return Movie.objects.all()


class VideoList(ListView):
    template_name = 'video_file_list.html'

    def get_queryset(self):
        list = VideoFile.objects.all()
        if 'movie' in self.request.GET:
            list = list.filter(movie_id=self.request.GET['movie'])
        return list