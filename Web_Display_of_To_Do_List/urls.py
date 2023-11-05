"""
URL configuration for Web_Display_of_To_Do_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path # Adds the re_path for use to regex the path for home view
from Web_Display_of_To_Do_List_App import views # Adds access to the views file in the hello world app directory
from Web_Display_of_To_Do_List_App import views as to_do_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('to_do/',to_do_view.to_do, name='to do list'),

    # Grabs the home view that is seup in the views.py file
    re_path(r'^$', views.home, name='home')
]
