from django.shortcuts import render
from reservation.forms import ReservationForm



def reserv(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table.state = False
            reservation.table.save()
            reservation.save()
            return render(request, 'success.html')  # Вернуть страницу с сообщением об успешном создании бронирования
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})


def reserv_success(request):
    return render(request, 'success.html', {})

