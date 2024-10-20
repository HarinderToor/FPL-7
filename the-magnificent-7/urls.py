
from django.urls import path

from api.views import Magnificence7APIView, TeamsMagnificence7APIView

urlpatterns = [
    path('magnificent-7/', Magnificence7APIView.as_view(), name='magnificent-7/'),
    path('magnificent-7/<str:team_name>/', TeamsMagnificence7APIView.as_view(), name='team-magnificent-7/')
]
