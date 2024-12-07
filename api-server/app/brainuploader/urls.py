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
# TODO: eventually, we want to use token authentication
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from django.views.generic.base import TemplateView
from brainuploader.views import SignUpView
from brainuploader.views import DeckViewSet
from brainuploader.views import FlashcardViewSet

router = routers.DefaultRouter()
router.register(r'flashcards', FlashcardViewSet, "flashcard-detail")
router.register(r'decks', DeckViewSet, "deck-detail")

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
#    path('api/flashcards/', FlashcardQueryAPIView.as_view(), name='rest_query_flashcards'),
#    path('api/flashcard/create/?deck=<int:pk>', FlashcardCreateAPIView.as_view(), name='flashcard_create_view'),
#    path('api/flashcard/<int:pk>/', FlashcardDetailAPIView.as_view(), name='flashcard_detail_view'),
#    path('api/decks/', DeckQueryAPIView.as_view(), name='rest_query_decks'),
#    path('api/deck/create/', DeckCreateAPIView.as_view(), name='deck_create_view'),
#    path('api/deck/<int:pk>/', DeckDetailAPIView.as_view(), name='deck_detail_view'),
# Note: We are not currently using token authentication, but as it offers enhanced security, it will be considerd for the future.
#    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

