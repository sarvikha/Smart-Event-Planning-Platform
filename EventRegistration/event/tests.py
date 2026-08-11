from datetime import time

from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Category, CompletedEvent, Event, Participant, Wishlist


class EventModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Technical', description='Technical events')
        self.event = Event.objects.create(
            category=self.category,
            title='Python Workshop',
            description='Intro to Django.',
            venue='Main Hall',
            event_date='2026-07-20',
            event_time=time(14, 0),
            status=Event.EventStatus.UPCOMING,
        )
        self.participant = Participant.objects.create(
            name='Alice',
            email='alice@example.com',
            phone='1234567890',
            event=self.event,
        )

    def test_event_status_choices(self):
        self.assertEqual(self.event.status, Event.EventStatus.UPCOMING)
        self.assertIn(self.event.status, dict(Event.EventStatus.choices))

    def test_wishlist_uniqueness(self):
        Wishlist.objects.create(participant=self.participant, event=self.event)
        with self.assertRaises(IntegrityError):
            Wishlist.objects.create(participant=self.participant, event=self.event)

    def test_completed_event_uniqueness(self):
        CompletedEvent.objects.create(event=self.event)
        with self.assertRaises(IntegrityError):
            CompletedEvent.objects.create(event=self.event)


class EventViewsTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Cultural', description='Cultural events')
        Event.objects.create(
            category=category,
            title='Music Night',
            description='Community music event.',
            venue='Auditorium',
            event_date='2026-08-01',
            event_time=time(18, 30),
            status=Event.EventStatus.UPCOMING,
        )

    def test_home_redirects_to_event_list(self):
        response = self.client.get(reverse('event:home'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('event:event_list'))

    def test_event_list_view_renders(self):
        response = self.client.get(reverse('event:event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upcoming Events')

    def test_event_create_view_displays_form(self):
        response = self.client.get(reverse('event:event_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Event')
