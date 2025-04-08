from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events'),
    path('registrations/',views.registrations,name='registrations'),
    path('event/', views.event, name='event'),
    path('info/',views.info,name='info'),
    path('register/',views.register,name='register'),
    path('payment/',views.payment,name='payment'),
    path('registrationDetails/',views.registrationDetails,name='registrationDetails'),
    path('technical/', views.technical_events, name='technical_events'),
    path('non-technical/', views.non_technical_events, name='non_technical_events'),
    path('sports/', views.sports_events, name='sports_events'),
    path('e-sports/', views.e_sports_events, name='e_sports_events'),
]