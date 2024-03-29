from django.contrib import admin
from django.urls import path,include
# from .views import StudentView

from .views import StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentView.as_view()),
    path('student/<int:rollno>', StudentView.as_view()),
]
