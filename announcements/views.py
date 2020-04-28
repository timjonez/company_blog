from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Announcement
from .forms import AnnouncementForm
from django.utils import timezone
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
decorators = [user_passes_test(lambda u:u.is_superuser)]

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement

    def get_queryset(self):
        return Prayer.objects.filter(date__lte=timezone.now()).order_by('-date')

class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    model = Announcement

@method_decorator(decorators, name='dispatch')
class CreateAnnouncementView(CreateView):
    redirect_field_name = 'index.html'
    form_class = AnnouncementForm
    model = Announcement


@method_decorator(decorators, name='dispatch')
class AnnouncementUpdateView(UpdateView):
    redirect_field_name = 'announcements/announcement_list.html'
    form_class = AnnouncementForm
    model = Announcement

@method_decorator(decorators, name='dispatch')
class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = reverse_lazy('announcements:announcement_list')
