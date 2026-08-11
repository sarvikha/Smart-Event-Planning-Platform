from django.contrib import admin

from .models import (
    Category,
    CompletedEvent,
    Event,
    EventBudget,
    Expense,
    Participant,
    Sponsor,
    Sponsorship,
    Wishlist,
)

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(EventBudget)
admin.site.register(Expense)
admin.site.register(Participant)
admin.site.register(Sponsor)
admin.site.register(Sponsorship)
admin.site.register(Wishlist)
admin.site.register(CompletedEvent)