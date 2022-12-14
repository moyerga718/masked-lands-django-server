"""maskedlands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from maskedlandsapi.views import CharacterView
from maskedlandsapi.views import register_user, login_user
from maskedlandsapi.views import ArmorView
from maskedlandsapi.views import CharacterDevotionView
from maskedlandsapi.views import SpeciesView
from maskedlandsapi.views import CombatClassView
from maskedlandsapi.views import BackgroundView
from maskedlandsapi.views import SubclassView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'characters', CharacterView, 'character')
router.register(r'armor', ArmorView, 'armor')
router.register(r'devotion', CharacterDevotionView, 'devotion')
router.register(r'species', SpeciesView, 'species')
router.register(r'classes', CombatClassView, 'class')
router.register(r'backgrounds', BackgroundView, 'background')
router.register(r'subclasses', SubclassView, 'subclass')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
