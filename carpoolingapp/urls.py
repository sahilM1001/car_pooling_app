from django.urls import path
from . import views

urlpatterns = [
    #api paths 
    path('',views.hello, name='Hello Page'),#done
    path('api/home', views.home, name='Home Page'),#done
    path('api/login', views.loginReq, name='Login Request'),#done
    path('api/signup', views.signupReq, name='Signup Request'),#done
    path('api/bookTrip', views.bookTrip, name='Trip Booking'),#done
    path('api/addTrip', views.addTrip, name='Add Trip'),#done
    path('api/cancelTrip', views.cancelTrip, name='Cancel Trip'),
    path('api/rateTrip', views.addRatings, name='Rate Trip'),#done
    path('api/viewRatings', views.viewRatings, name='View Ratings'),#done
    path('api/updateDetails', views.updateUserDetails, name='Update User Details'),#done
    path('api/viewTrips', views.viewTrips, name='View Trips'),#done
    path('api/logout', views.logoutReq, name='Logout Trips'),#done
    path('api/myProfile', views.myProfile, name='My Profile'),#done
    
    
    #view paths
    path('view/login', views.loginView, name='Login View'),#done
    path('view/signup', views.signupView, name='Signup View'),#done
    path('view/home', views.homeView, name='Home View'),#done
    path('view/addTrip', views.addTripView, name='Add Trip View'),#done
    path('view/viewTrips', views.viewTripView, name='View Trips View'),#done
    path('view/myProfile', views.myProfileView, name='My Profile View'),#done

]