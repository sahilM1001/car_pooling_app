from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello, name='Hello Page'),#done
    path('home', views.home, name='Home Page'),#done
    path('login', views.loginReq, name='Login Request'),#done
    path('signup', views.signupReq, name='Signup Request'),#done
    path('bookTrip', views.bookTrip, name='Trip Booking'),#done
    path('addTrip', views.addTrip, name='Add Trip'),#done
    path('cancelTrip', views.loginReq, name='Cancel Trip'),
    path('rateTrip', views.addRatings, name='Rate Trip'),#done
    path('viewRatings', views.viewRatings, name='View Ratings'),#done
    path('updateDetails', views.updateUserDetails, name='Update User Details'),#done
    path('viewTrips', views.viewTrips, name='View Trips')#done
    
]