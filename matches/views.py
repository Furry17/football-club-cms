from django.shortcuts import get_object_or_404, render

from .models import Match


def match_list(request):
    matches = Match.objects.all().order_by("-match_date")
    return render(request, 'matches/match_list.html', {'matches': matches})

def match_detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, "matches/match_detail.html", {'match': match})
