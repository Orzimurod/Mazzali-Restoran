from django.urls import path
from orders.reservation.views import reservation_view
from restaurant.views import index_view, logout_view

urlpatterns = [
    path('', index_view, name='index'),
    path('logout', logout_view, name='logout'),
]
