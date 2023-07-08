from django.urls import path
from .views import SingUpView

urlpatterns = [
    path('sing_up/',SingUpView.as_view(),name='sing_up'),
]