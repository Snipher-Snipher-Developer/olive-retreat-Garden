from django.urls import path, include

from assets import views

urlpatterns = [
    path('booking/', views.BookedEvents.as_view())
]
