from django import forms

from .models import Event, EventBudget, Expense, Sponsor, Sponsorship


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'category',
            'title',
            'description',
            'venue',
            'event_date',
            'event_time',
            'status',
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class EventBudgetForm(forms.ModelForm):
    class Meta:
        model = EventBudget
        fields = ['total_budget', 'currency', 'notes']
        widgets = {
            'total_budget': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'currency': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'category', 'amount', 'expense_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'expense_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['name', 'organization', 'email', 'phone', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        fields = ['sponsor', 'amount', 'sponsorship_type', 'agreement_date', 'notes']
        widgets = {
            'sponsor': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'sponsorship_type': forms.Select(attrs={'class': 'form-select'}),
            'agreement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
