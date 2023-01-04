from django.urls import path
from api.views import UserView

namespace = 'api'

urlpatterns = [
    path('user', UserView.as_view()),
]
