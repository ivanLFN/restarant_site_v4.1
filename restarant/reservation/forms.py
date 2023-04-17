from django import forms
from reservation.models import Table, ReservationTable


class ReservationForm(forms.ModelForm):

    table = forms.ModelChoiceField(
        queryset=Table.objects.filter(state=True),
        widget=forms.Select(attrs={'class': 'form-control reserv-obj'})
    )
    
    class Meta:
        model = ReservationTable
        fields = ['name', 'phone', 'email', 'date_time', 'count_person', 'table']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'reserv-obj'}),
            'phone': forms.NumberInput(attrs={'class': 'reserv-obj'}),
            'email': forms.EmailInput(attrs={'class': 'reserv-obj'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '0', 'class': 'reserv-obj'}),
            'count_person': forms.NumberInput(attrs={'class': 'reserv-obj'}),
            'table': forms.Select(attrs={'class': 'form-control reserv-obj'}),
        }


