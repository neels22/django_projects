




from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/',views.create_student,name='add_student'),
    path('',views.display_student,name='display_student'),
    # path('',views.create_student,name='display_student'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    