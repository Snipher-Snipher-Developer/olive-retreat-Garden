from django.urls import path, include

from oliver import views

urlpatterns = [
    path('booking/', views.BookedEvents.as_view())
]
