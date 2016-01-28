from django.views.generic import TemplateView, ListView

from videoz import Movie, VideoFile


class VideoPlayer(TemplateView):
    template_name = 'video_player.html'

    def get_context_data(self, **kwargs):
        data = super(VideoPlayer, self).get_context_data(**kwargs)
        pk = kwargs['pk']
        data['video']=VideoFile.objects.get(pk=pk)
        return data
