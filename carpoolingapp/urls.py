from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello, name='Hello Page'),
    path('home', views.home, name='Home Page'),
    path('login', views.loginReq, name='Login Request'),
    path('bookTrip', views.bookTrip, name='Trip Booking'),
    path('addTrip', views.addTrip, name='Add Trip'),
    path('cancelTrip', views.loginReq, name='Cancel Trip'),
    path('rateTrip', views.loginReq, name='Rate Trip'),
    path('viewRatings', views.loginReq, name='View Ratings'),
    path('updateDetails', views.loginReq, name='Update User Details'),
    path('viewTrips', views.loginReq, name='View Trips')
    
]