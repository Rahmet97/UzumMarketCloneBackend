from django.urls import path

from users.views import SendVerificationCode

urlpatterns = [
    path('verification', SendVerificationCode.as_view(), name='verification'),
]
