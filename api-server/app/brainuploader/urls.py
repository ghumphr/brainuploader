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
from brainuploader.views import FlashcardDetailAPIView, FlashcardQueryAPIView
from brainuploader.views import DeckDetailAPIView, DeckQueryAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/flashcards/', FlashcardQueryAPIView.as_view(), name='rest_query_flashcards'),
    path('rest/flashcard/<int:pk>/', FlashcardDetailAPIView.as_view(), name='rest_get_flashcard'),
    path('rest/decks/', DeckQueryAPIView.as_view(), name='rest_query_decks'),
    path('rest/deck/<int:pk>/', DeckDetailAPIView.as_view(), name='rest_get_deck'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
