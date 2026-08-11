from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    EventBudgetForm,
    EventForm,
    ExpenseForm,
    SponsorForm,
    SponsorshipForm,
)
from .models import Event, EventBudget, Expense, Sponsor, Sponsorship


def home(request):
    return redirect('event:event_list')


def event_list(request):
    events = Event.objects.select_related('category').prefetch_related('expenses', 'sponsorships').all()
    return render(request, 'event/event_list.html', {'events': events})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            EventBudget.objects.get_or_create(event=event)
            return redirect('event:event_list')
    else:
        form = EventForm()

    return render(request, 'event/event_form.html', {'form': form})


def event_detail(request, pk):
    event = get_object_or_404(Event.objects.select_related('category'), pk=pk)
    budget_form = EventBudgetForm()
    expense_form = ExpenseForm()
    sponsor_form = SponsorForm()
    sponsorship_form = SponsorshipForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'budget':
            budget_form = EventBudgetForm(request.POST)
            if budget_form.is_valid():
                budget, _ = EventBudget.objects.get_or_create(event=event)
                budget.total_budget = budget_form.cleaned_data['total_budget']
                budget.currency = budget_form.cleaned_data['currency']
                budget.notes = budget_form.cleaned_data['notes']
                budget.save()
                return redirect('event:event_detail', pk=event.pk)
        elif action == 'expense':
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense = expense_form.save(commit=False)
                expense.event = event
                expense.save()
                return redirect('event:event_detail', pk=event.pk)
        elif action == 'sponsor':
            sponsor_form = SponsorForm(request.POST)
            if sponsor_form.is_valid():
                sponsor = sponsor_form.save()
                sponsorship = Sponsorship.objects.create(
                    event=event,
                    sponsor=sponsor,
                    amount=request.POST.get('amount', 0),
                    sponsorship_type=request.POST.get('sponsorship_type', Sponsorship.SponsorshipTier.SUPPORT),
                    agreement_date=request.POST.get('agreement_date', event.event_date),
                    notes=request.POST.get('notes', ''),
                )
                return redirect('event:event_detail', pk=event.pk)
        elif action == 'sponsorship':
            sponsorship_form = SponsorshipForm(request.POST)
            if sponsorship_form.is_valid():
                sponsorship = sponsorship_form.save(commit=False)
                sponsorship.event = event
                sponsorship.save()
                return redirect('event:event_detail', pk=event.pk)

    context = {
        'event': event,
        'budget_form': budget_form,
        'expense_form': expense_form,
        'sponsor_form': sponsor_form,
        'sponsorship_form': sponsorship_form,
        'expenses': event.expenses.all(),
        'sponsorships': event.sponsorships.select_related('sponsor').all(),
        'budget': getattr(event, 'eventbudget', None),
    }
    return render(request, 'event/event_detail.html', context)
