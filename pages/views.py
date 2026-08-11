from django.shortcuts import render
from django.utils import timezone

from matches.models import Match
from training.models import Training


def homepage(request):
    next_match = Match.objects.filter(match_date__gte=timezone.now()).order_by('match_date').first()
    last_match = Match.objects.filter(match_date__lt=timezone.now()).order_by('-match_date').first()
    next_training = Training.objects.filter(training_date__gte=timezone.now()).order_by('training_date').first()
    return render(request, 'pages/home.html', {'next_match': next_match, 'last_match': last_match, 'next_training': next_training})