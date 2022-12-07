from django.urls import path
from .views import profile, sign_up, sign_in, sign_out

urlpatterns = [
    path('', profile, name='profile-view'),
    path('sign-up/', sign_up, name='sign-up-view'),
    path('sign-in/', sign_in, name='sign-in-view'),
    path('sign-out/', sign_out, name='sign-out-view'),
]
