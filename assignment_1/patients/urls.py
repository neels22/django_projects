



from django.urls import path

from . import views

urlpatterns = [
    path('',views.schedule),
    path('history/',views.history),
    path('notifications/',views.notification),
]

