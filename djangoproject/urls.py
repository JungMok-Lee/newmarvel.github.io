"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name='home'),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/introduce', blog.views.introduce, name='introduce'),
    path('blog/introduce/maker', blog.views.maker, name='maker'),
    path('blog/introduce/aboutmarvel', blog.views.aboutmarvel, name="aboutmarvel"),
    path('blog/introduce/motivation', blog.views.motivation, name="motivation"),
    path('blog/introduce/process', blog.views.process, name="process"),

    path('blog/movie', blog.views.movie, name='movie'),
    path('blog/movie/trailer', blog.views.trailer, name='trailer'),
    path('blog/movie/audience', blog.views.audience, name="audience"),
    path('blog/movie/plan', blog.views.plan, name="plan"),
    path('blog/movie/news', blog.views.news, name="news"),

    path('blog/character', blog.views.character, name='character'),
    path('blog/character/captainamerica', blog.views.captain, name='captain'),
    path('blog/character/ironman', blog.views.ironman, name="ironman"),
    path('blog/character/blackwidow', blog.views.blackwidow, name="blackwidow"),
    path('blog/character/wintersoldier', blog.views.wintersoldier, name="wintersoldier"),
]