from django.shortcuts import get_object_or_404, render

from .models import Training


def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'training/training_list.html', {'trainings': trainings}  )

def training_detail(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    return render(request, 'training/training_detail.html', {'training': training})
