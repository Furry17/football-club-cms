from django.shortcuts import render
from django.utils import timezone

from matches.models import Match


def homepage(request):
    next_match = Match.objects.filter(match_date__gte=timezone.now()).order_by('match_date').first()
    return render(request, 'pages/home.html', {'next_match': next_match})