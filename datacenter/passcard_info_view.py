from datacenter.models import Passcard, Visit, format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    # Программируем здесь
    this_passcard_visits = []
    for attendance in visits:
        this_passcard_visit = {
            'entered_at': attendance.entered_at,
            'duration': format_duration(Visit.get_duration(attendance)),
            'is_strange': Visit.is_visit_long(attendance)
        }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
