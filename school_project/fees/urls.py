



from django.urls import path
from . import views

urlpatterns = [
    path('feeslearndj/',views.feeslearndj),
    path('feeslearnpython/',views.feeslearnpython)
]


