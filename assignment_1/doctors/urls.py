



from django.urls import path

from . import views

urlpatterns = [
    path('med/',views.medication),
    path('view_pat/',views.view_pat),

]

