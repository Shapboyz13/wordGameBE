from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)


urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

]
