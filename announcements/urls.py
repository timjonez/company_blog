from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/<int:pk>', views.AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/', views.CreateAnnouncementView.as_view(), name='create_announcement'),
    path('announcement/<int:pk>/edit/', views.AnnouncementUpdateView.as_view(), name='announcement_edit'),
    path('announcement/<int:pk>/remove/', views.AnnouncementDeleteView.as_view(), name='announcement_remove'),
]
