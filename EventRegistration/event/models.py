from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    class EventStatus(models.TextChoices):
        UPCOMING = 'Upcoming', 'Upcoming'
        ONGOING = 'Ongoing', 'Ongoing'
        COMPLETED = 'Completed', 'Completed'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=EventStatus.choices,
        default=EventStatus.UPCOMING,
    )

    def __str__(self):
        return self.title

    @property
    def status_class(self):
        return {
            self.EventStatus.UPCOMING: 'badge bg-info',
            self.EventStatus.ONGOING: 'badge bg-warning text-dark',
            self.EventStatus.COMPLETED: 'badge bg-success',
        }.get(self.status, 'badge bg-secondary')

    @property
    def budget(self):
        return self.eventbudget.total_budget if hasattr(self, 'eventbudget') else Decimal('0.00')

    @property
    def total_expense(self):
        return self.expenses.aggregate(total=models.Sum('amount'))['total'] or Decimal('0.00')

    @property
    def total_sponsorship(self):
        return self.sponsorships.aggregate(total=models.Sum('amount'))['total'] or Decimal('0.00')

    @property
    def remaining_budget(self):
        return self.budget - self.total_expense

    @property
    def net_funding(self):
        return self.total_sponsorship - self.total_expense


class EventBudget(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='eventbudget')
    total_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
    )
    currency = models.CharField(max_length=10, default='USD')
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.event.title} budget"


class Expense(models.Model):
    class ExpenseCategory(models.TextChoices):
        VENUE = 'Venue', 'Venue'
        MARKETING = 'Marketing', 'Marketing'
        FOOD = 'Food', 'Food'
        LOGISTICS = 'Logistics', 'Logistics'
        EQUIPMENT = 'Equipment', 'Equipment'
        OTHER = 'Other', 'Other'

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=ExpenseCategory.choices, default=ExpenseCategory.OTHER)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    expense_date = models.DateField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-expense_date', '-id']

    def __str__(self):
        return f"{self.title} ({self.amount})"


class Sponsor(models.Model):
    name = models.CharField(max_length=150)
    organization = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Sponsorship(models.Model):
    class SponsorshipTier(models.TextChoices):
        TITLE = 'Title', 'Title'
        GOLD = 'Gold', 'Gold'
        SILVER = 'Silver', 'Silver'
        BRONZE = 'Bronze', 'Bronze'
        SUPPORT = 'Support', 'Support'

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sponsorships')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='sponsorships')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    sponsorship_type = models.CharField(max_length=20, choices=SponsorshipTier.choices, default=SponsorshipTier.SUPPORT)
    agreement_date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-agreement_date', '-id']

    def __str__(self):
        return f"{self.sponsor.name} - {self.event.title}"


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('participant', 'event')

    def __str__(self):
        return f"{self.participant.name} - {self.event.title}"


class CompletedEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    completed_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event'], name='unique_completed_event'),
        ]

    def __str__(self):
        return self.event.title