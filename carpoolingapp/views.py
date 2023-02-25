from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='car_pooling_app')
print('Successfully connected to database')
cur = conn.cursor()
loggedInUser = 0
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

from django.views.decorators.csrf import csrf_exempt

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
            print("DATA IS NOT NONEEEE")
            print(data)
            loggedInUser = data[0]
            return HttpResponse("<h1>Login Successful</h1>")
            if len(data) > 0:
                #Fetch Data
                admin_db_id = data[0]
                admin_db_email = data[1]
                print(admin_db_id)
                print(admin_db_email)
                #Session Create Code
                request.session['admin_id'] = admin_db_id
                request.session['admin_email'] = admin_db_email
                #Session Create Code
                #Cookie Code
                #response = redirect(index)
                """ response.set_cookie('admin_id', admin_db_id)
                response.set_cookie('admin_email', admin_db_email)
                return response """
                #Cookie Code
            else:
                pass
                #return render(request, 'login/signup.html')         
        
        #return render(request, 'login/signup.html')
        
       # return redirect(dashboard) 
    #else:
        #return render(request, 'login/signup.html')

@csrf_exempt
def home(request):
    #query to load all available trips for the user on a specific day
    print("Home page request called")
    import datetime   
    dt = datetime.datetime.now()

    cur.execute("SELECT * FROM `trip_details` WHERE trip_date = '{}'".format(str(dt).split(" ")[0]))
    data = cur.fetchall()
    print("==========================")
    print("received response data: ", data)
    print("==========================")
    return HttpResponse(data)

@csrf_exempt
def addTrip(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================")
        cur.execute("INSERT INTO `trip_details` (`trip_details_id`, `trip_from`, `trip_to`, `trip_date`, `trip_driver_id`, `trip_car_number`, `trip_total_spots`, `trip_charges_per_person`, `trip_spots_available`, `trip_time`, `trip_route_details`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            2,
            reqBody['trip_from'],
            reqBody['trip_to'],
            reqBody['trip_date'],
            1,
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
def bookTrip(request):
    print("INSIDE BO")
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        reqBody = json.loads(body_unicode)
        print("==========================")
        print("received req: ", reqBody)
        print("==========================")
        cur.execute("INSERT INTO `trips` (`trip_id`, `passenger_u_id`, `trip_charges_paid`, `trip_status`,`trip_details_id`) VALUES ('{}','{}', '{}', '{}', '{}')".format(
            reqBody['trip_id'],
            reqBody['passenger_u_id'],
            reqBody['trip_charges_paid'],
            reqBody['trip_status'],
            reqBody['trip_details_id']
        ))
        conn.commit()
        return HttpResponse("<h1>Trip Booked Successfully</h1>")