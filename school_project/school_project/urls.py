"""
URL configuration for school_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Import include

from . import views


# from course import views #one way to import
 
# from course.views import learnreact #another way to import


# from course import views as vs

# from fees import views as fs

# from Admin import views as ads



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dj/',views.learndj),
    # path('dj1/',views.learnpython),
    # path('dj2/',learnreact),
    # path('fees/',fs.feeslearndj),
    # path('fees2/',fs.feeslearnreact),
    # path('fees3/',fs.feesprintstring),
    # path('ad1/',ads.adminlearndj),
    # path('ad2/',ads.adminlearnreact),
    # path('ad3/',ads.adminlearnpython),
    # path('dj3/',vs.printstring),



     path('fees/', include('fees.urls')),
     path('', views.homepage),
    
]


