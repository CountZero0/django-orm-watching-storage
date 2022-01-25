from datacenter.models import Visit, format_duration
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    storage_visits = Visit.objects.filter(leaved_at=None)
    visits = []
    for attendance in storage_visits:

        non_closed_visits = {
            'who_entered': attendance.passcard.owner_name,
            'entered_at': attendance.entered_at,
            'duration': format_duration(Visit.get_duration(attendance)),
        }
        visits.append(non_closed_visits)
    context = {
        'non_closed_visits': visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
