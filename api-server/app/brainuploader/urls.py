"""
URL configuration for brainuploader project.

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
from django.urls import include, path
from rest_framework import routers
from brainuploader.views import FlashcardViewSet
from brainuploader.views import DeckViewSet
from django.views.generic.base import TemplateView
from brainuploader.views import SignUpView
from brainuploader.views import DeckViewSet
from brainuploader.views import FlashcardViewSet

# This sets up the router for the CRUD/query API
api_router = routers.DefaultRouter()
api_router.register(r'flashcards', FlashcardViewSet, "flashcard-detail")
api_router.register(r'decks', DeckViewSet, "deck-detail")

urlpatterns = [
    # Route the URLs for the CRUD/query API
    path('api/', include(api_router.urls)),

    # Route the URLs for Django admin interface
    path('admin/', admin.site.urls),

    # Route URLs for the account management interface
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),

    # Route the URL for the landing page
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]

