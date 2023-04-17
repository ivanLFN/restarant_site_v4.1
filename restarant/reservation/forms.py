from django import forms
from reservation.models import Table, ReservationTable


class ReservationForm(forms.ModelForm):
    table = forms.ModelChoiceField(
        queryset=Table.objects.filter(state=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = ReservationTable
        fields = ['name', 'phone', 'email', 'date_time', 'count_person', 'table']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '0'}),
            # 'count_person': forms.NumberInput(attrs={'placeholder': 'count person'}),
        }


