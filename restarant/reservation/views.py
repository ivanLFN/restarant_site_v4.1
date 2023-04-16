from django.shortcuts import render
from reservation.forms import ContactForm


def reserv(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            pass
    else:
        form = ContactForm()

    return render(request, 'reservation.html', {'form': form})

