from django.views.generic import TemplateView, ListView
 
from django.db.models import Q

from .models import Player
 
 
class HomePageView(TemplateView):
    template_name = 'home.html'
 
class SearchResultsView(ListView):
    model = Player
    template_name = 'search_results.html'
 
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Player.objects.filter(
            Q(nickname__icontains=query) | Q(team__icontains=query)
        )
        return object_list