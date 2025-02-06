"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main.views import main_main
from leaderboard.views import leaderboard_main
from description.views import description_main
from gallery.views import gallery_main
from rule.views import rule_main
from build_ranking.views import build_ranking_main


urlpatterns = [
    path('wltpwltp', admin.site.urls),
    path('', main_main),
    path('leaderboard', leaderboard_main),
    path('description', description_main),
    path('gallery', gallery_main),
    path('rules', rule_main),
    path('build_ranking', build_ranking_main),
]
