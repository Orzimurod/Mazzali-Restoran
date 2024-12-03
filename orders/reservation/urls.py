from django.urls import path
from orders.reservation.views import reservation_view

urlpatterns = [
   path('reservation/', reservation_view, name='reservation'),
]
