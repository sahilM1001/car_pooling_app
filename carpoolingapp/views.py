from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='car_pooling_app')
print('Successfully connected to database')
cur = conn.cursor()
states ={
    'logged_in_user': 0
}
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

from django.views.decorators.csrf import csrf_exempt
#function/API to signup in the system 
@csrf_exempt
def signupReq(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("==========================")
    print("received req: ", body)
    print("==========================")
    if request.method == "POST":
        cur.execute("INSERT INTO `user` (`user_name`, `user_pwd`, `user_email`,`user_mobile_no`) VALUES ('{}', '{}', '{}', '{}')".format(
            body['user_name'],
            body['user_pwd'],
            body['user_email'],
            body['user_mobile_no']
        ))
        conn.commit()
    return HttpResponse("<h1>Request Successful</h1>")

#function/API to login to the system based on the user email and password
@csrf_exempt 
def loginReq(request):
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("==========================")
    print("received req: ", body)
    print("==========================")
    content = body['email']
    if request.method == 'POST':
        print("REQUEEESSSTTT METHODDDD IS POSTTTTT")
        print("request post: ", request.POST)
        admin_email = body['email']
        admin_pass = body['password']
        
        cur.execute("SELECT `user_id`, `user_email`, `user_pwd` FROM `user` WHERE `user_email` = '{}' AND `user_pwd` = '{}' ".format(admin_email,admin_pass))
        data = cur.fetchone()
        if data is not None:
            
            print(data)
            loggedInUser = data[0]
            print("loggedInUser: ", loggedInUser)
            states['logged_in_user'] = data[0]
            #return HttpResponse("<h1>Login Successful</h1>")
            if len(data) > 0:
                #Fetch Data
                loggedInUser_id = data[0]
                
                #Session Create Code
                request.session['user_id'] = loggedInUser_id
               
                #Cookie Code
                return HttpResponse("<h1>Login Successful</h1>")

#view function to render login page
@csrf_exempt
def loginView(request):
    print("inside the login view")
    
    return render(request,'login/login.html')

@csrf_exempt
def signupView(request):
    return render(request,'login/signup.html')

#function/API to update user details
@csrf_exempt
def userDetails(request):
    if request.method == "GET":
        cur.execute("SELECT * FROM `user` WHERE user_id ='{}'".format(request.session['user_id']))
        #request.session['user_id']
        data = cur.fetchall()
        dataArr = []
        print("-------------------------")
        print(data)
        print("-------------------------")        
        temp = {
            'user_name': data[0][1],
            'user_pwd': data[0][2],
            'user_email': data[0][3],
            'user_mob': data[0][4],
            'u_id': data[0][0]
        }
        return JsonResponse(temp)
    
    if request.method == "PUT":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print("==========================")
        print("received req: ", body)
        print("==========================")
        print("request.session['user_id']: ", request.session['user_id'])
        if "user_name" in body:
            cur.execute("UPDATE `user` SET user_name = '{}' WHERE user_id = '{}'".format(body['user_name'],request.session['user_id']))
            conn.commit()
        if "user_pwd" in body:
            cur.execute("UPDATE `user` SET user_pwd = '{}' WHERE user_id = '{}'".format(body['user_pwd'],request.session['user_id']))
            conn.commit()
        if "user_email" in body:
            cur.execute("UPDATE `user` SET user_email = '{}' WHERE user_id = '{}'".format(body['user_email'],request.session['user_id']))
            conn.commit()
        if "user_mobile_no" in body:
            cur.execute("UPDATE `user` SET user_mobile_no = '{}' WHERE user_id = '{}'".format(body['user_mobile_no'],request.session['user_id']))
            conn.commit()
    return HttpResponse("<h1>Details Updated Successfully</h1>")

@csrf_exempt
def updateUserView(request):
    return render(request,"home/updateProfile.html")
#function/API to load homepage and available trips for the same day
@csrf_exempt
def home(request):
    #query to load all available trips for the user on a specific day
    print("Home page request called")
    import datetime   
    dt = datetime.datetime.now()

    #cur.execute("SELECT * FROM `trip_details` WHERE trip_date = '{}'".format(str(dt).split(" ")[0]))
    cur.execute("SELECT * FROM `trip_details`")
    data = cur.fetchall()
    print("==========================")
    print("received response data: ", data)
    print("==========================")
    dataArr = []
    for i in data:
        temp = {
            'trip_details_id': i[0],
            'trip_from':i[1],
            'trip_to': i[2],
            'trip_date': i[3],
            'trip_driver_id': i[4],
            'trip_car_number': i[5],
            'trip_total_spots': i[6],
            'trip_charges_per_person': i[7],
            'trip_spots_available': i[8],
            'trip_time': i[9],
            'trip_route_details': i[10]
        }
        dataArr.append(temp)
    returnDic = {
        'data': dataArr
    }
    return JsonResponse(returnDic)

@csrf_exempt
def homeView(request):
    print("Homepage view called")
    return render(request, 'home/home.html')
    

#function/API to add new trip to the system
@csrf_exempt
def addTrip(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================")
        cur.execute("INSERT INTO `trip_details` (`trip_from`, `trip_to`, `trip_date`, `trip_driver_id`, `trip_car_number`, `trip_total_spots`, `trip_charges_per_person`, `trip_spots_available`, `trip_time`, `trip_route_details`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            reqBody['trip_from'],
            reqBody['trip_to'],
            reqBody['trip_date'],
            request.session['user_id'],
            reqBody['trip_car_number'],
            reqBody['trip_total_spots'],
            reqBody['trip_charges_per_person'],
            reqBody['trip_spots_available'],
            reqBody['trip_time'],
            reqBody['trip_route_details']

        ))
        conn.commit()
        return HttpResponse("<h1>Trip Details Added Successfully</h1>")

@csrf_exempt
def addTripView(request):
    print("add trip view called")
    return render(request, 'home/addTrip.html')
#function/API to book a trip from the available trips
@csrf_exempt
def bookTrip(request):
    print("INSIDE BO")
    print("request session: ", request.session)
    print("request session user_id: ", )
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================")
        #print("logged in user: ", states)
        
        cur.execute("INSERT INTO `trips` (`passenger_u_id`, `trip_charges_paid`, `trip_status`,`trip_details_id`) VALUES ('{}', '{}', '{}', '{}')".format(
            request.session['user_id'],
            reqBody['trip_charges_paid'],
            reqBody['trip_status'],
            reqBody['trip_details_id']
        ))
        cur.execute("UPDATE `trip_details` SET `trip_spots_available` = `trip_spots_available` - 1 WHERE `trip_details_id` = {} AND `trip_spots_available` > 0".format(reqBody['trip_details_id']))
        conn.commit()
        return HttpResponse("<h1>Trip Booked Successfully</h1>")

#function/API to view different available trips
@csrf_exempt
def viewTrips(request):
    if request.method == 'GET':
        """ body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================") """
        print("inside view trips")
        import datetime   
        dt = datetime.datetime.now()
        #cur.execute("SELECT trips.trip_id, trips.trip_charges_paid, trips.trip_status, trips.trip_details_id, trip_details.trip_from,trip_details.trip_to, trip_details.trip_date, trip_details.trip_car_number, trip_details.trip_route_details, trip_details.trip_time, trip_details.trip_driver_id FROM `trips` JOIN `trip_details` ON trips.trip_details_id = trip_details.trip_details_id WHERE trips.passenger_u_id = '{}' AND trip_details.trip_date = '{}'".format(request.session['user_id'],str(dt).split(" ")[0]))
        cur.execute("SELECT trips.trip_id, trips.trip_charges_paid, trips.trip_status, trips.trip_details_id, trip_details.trip_from,trip_details.trip_to, trip_details.trip_date, trip_details.trip_car_number, trip_details.trip_route_details, trip_details.trip_time, trip_details.trip_driver_id FROM `trips` JOIN `trip_details` ON trips.trip_details_id = trip_details.trip_details_id WHERE trips.passenger_u_id = '{}'".format(request.session['user_id']))
        data = cur.fetchall()
        print("data fetched: ", data)
        #[(3, 100, 'Booked', 1, 'Juhapura', 'CG Road', datetime.date(2023, 3, 5), 'GJ01RN5249', 'Through Paldi')]
        dataArr = []
        for i in data:
            temp = {
                'trip_id': i[0],
                'trip_charges_paid':i[1],
                'trip_status': i[2],
                'trip_details_id': i[3],
                'trip_from': i[4],
                'trip_to': i[5],
                'trip_date': i[6],
                'trip_car_number': i[7],
                'trip_route_details': i[8],
                'trip_time': i[9],
                'trip_driver_id': i[10]
                
            }
            dataArr.append(temp)
        returnDic = {
            'data': dataArr,
            'logged_in_user': request.session['user_id']
        }
        return JsonResponse(returnDic)

def viewTripView(request):
    return render(request, 'home/viewTrip.html')

#function/API to add ratings to a trip
@csrf_exempt
def addRatings(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================")
        cur.execute("INSERT INTO `ratings` (`r_given_by`, `r_given_to`, `r_for_trip`,`r_ratings`) VALUES ('{}', '{}', '{}', '{}')".format(
            reqBody['r_given_by'],
            reqBody['r_given_to'],
            reqBody['r_for_trip'],
            reqBody['r_ratings']
        ))
        conn.commit()
        return HttpResponse("<h1>Trip Ratings Given Successfully</h1>")
    
#function/API to view ratings given to you
@csrf_exempt
def viewRatings(request):
    if request.method == 'GET':
        """ body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================") """
        print("inside view ratings")
        cur.execute("SELECT * FROM `ratings` WHERE r_given_to = '{}'".format(1))
        data = cur.fetchall()
        print("data fetched: ", data)
        return HttpResponse("<h1>Trip Ratings Fetch Successfully</h1>")


#function to cancel trip
@csrf_exempt
def cancelTrip(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================")

        cur.execute("UPDATE `trip_details` SET `trip_spots_available` = `trip_spots_available` + 1 WHERE `trip_details_id` = {} ".format(reqBody['trip_details_id']))
        cur.execute("UPDATE `trips` SET `trip_status` = 'Cancelled' WHERE `trip_id` = {} ".format(reqBody['trip_id']))
        conn.commit()
        #pass
        return HttpResponse("<h1>Trip Canceled</h1>")

@csrf_exempt
def logoutReq(request):
    print()
    user_id = request.session['user_id']
    print("request.session: ", request.session)
    print("request session user_id: ", request.session['user_id'])
    del request.session['user_id']
    request.session.modified = True
    return redirect("/carpooling/view/login")

#function to render my Profile Page
@csrf_exempt
def myProfileView(request):
    return render(request, "home/myProfile.html")

#API function for my profile page
@csrf_exempt
def myProfile(request):
    uid = request.session['user_id']
    if request.method == "GET":
        cur.execute("SELECT user_id, user_name, user_email, user_mobile_no FROM `user` WHERE user_id = '{}'".format(uid))
        uData = cur.fetchone()
        returnDict = {
            'uData': uData
        } 

        cur.execute("SELECT COUNT(*) FROM `trip_details` WHERE trip_driver_id = '{}'".format(uid))
        trip_details_count = cur.fetchall()
        returnDict['trip_details_count'] = trip_details_count

        cur.execute("SELECT * FROM `trip_details` WHERE trip_driver_id = '{}' ORDER BY trip_date DESC LIMIT 5".format(uid))
        trip_details = cur.fetchall()
        returnDict['last_five_trips'] = trip_details

        print("return dict: ", returnDict)

        cur.execute("SELECT AVG(r_ratings) FROM `ratings` WHERE r_given_to = {}".format(int(uid)))
        avg_ratings = cur.fetchall()
        returnDict['avg_ratings'] = avg_ratings

        print("return dict: ", returnDict)
        return JsonResponse(returnDict)