from django.shortcuts import render
from django.http import HttpResponse
from tg_app.models import Customer , Subscriber , City , Event, Media
from random import random
from django.utils import timezone
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

TIME_DELTA = 10800

# Create your views here.
def user_details( request , user_id ):
    data = { 'rating' : 0 , 'subscription_list' : [] }
    try:
        user = Customer.objects.get( user_id = user_id )
    except:
        user = Customer.objects.create( user_id = user_id )
    subscriptions = Subscriber.objects.filter( customer = user )
    data['rating'] = user.rating
    for  subscription in subscriptions:
        data['subscription_list'].append( subscription.city.key )
    return HttpResponse( str(data) )

def get_cities( request , user_id ):
    cities = City.objects.all()
    data = { "Cities" : [] }
    for city in cities:
        city_data = {}
        city_data["key"] = str(city.key)
        city_data["name"] = city.name
        city_data["main_photo_url"] = city.main_photo_url.media_url
        data["Cities"].append( city_data )
    return HttpResponse( str(data) )

def get_events( request , user_id ):
    arts = Event.objects.filter( type = "arts" )
    events = Event.objects.filter( type = "events" )
    exhibitions = Event.objects.filter( type = "exhibitions" )
    data = {
                'arts' : { 'live' : [] , 'upcoming' : []  },
                'events' : { 'live' : [] , 'upcoming' : []  },
                'exhibitions' : { 'live' : [] , 'upcoming' : []  }
        }
    for ev in arts:
        to_push = {}
        to_push["id"] = ev.event_key
        to_push["main_photo_url"] = ev.main_photo_url.media_url
        to_push["title"] = ev.title
        to_push["about"] = ev.about
        to_push["address_line"] = ev.location.__str__()
        to_push["city_key"] = ev.city.key
        to_push["seen_by"] = ev.seen_by
        to_push["posted_on"] = ev.posted_on.strftime("%d %b %I:%M %r")
        to_push["start_time"] = ev.start_time.strftime("%d %b %I:%M %r")
        to_push["added_by"] = ev.added_by.user_id
        to_push["rating"] = round( 2 + 3 * random.random() , 1 )
        if( ( timezone.now() - ev.start_time() ).total_seconds() < 0 ):
            data['arts']['upcoming'].append( to_push )
        elif( ( timezone.now() - ev.start_time() ).total_seconds() < TIME_DELTA ):
            data['arts']['live'].append( to_push )
    return HttpResponse( str( data ) )

def subscribe_city( request , user_id , city ):
    try:
        subscriber = Subscriber.objects.get( customer = Customer.objects.get( user_id = user_id ) , city = City.objects.get( key = int(city) ) )
        subscriber.delete()
    except:
        subscriber = Subscriber.objects.create(customer = Customer.objects.get( user_id = user_id ) , city = City.objects.get( key = int(city) ) )
        subscriber.save()
    return HttpResponse('done')

def get_attractions( request , user_id = None , city = None ):
    pass

def get_blogs( request , city ):
    pass

def get_magical_moments( request , city ):
    pass

def get_food_items( request , city ):
    pass

def get_event_detail( request , event_id ):
    pass

@csrf_exempt
def add_event( request ):
    title = request.POST["title"]
    about = request.POST["about"]
    city_key = request.POST["city_key"]
    added_by = request.POST["added_by"]
    year = request.POST["year"]
    month = request.POST["month"]
    day = request.POST["day"]
    hour = request.POST["hour"]
    minute = request.POST["minute"]
    type = request.POST["type"]
    start_time = datetime.strptime( "%Y %m %d %H %M" , str(year) + " " + str(month) + " " + str(day) + " " + str(hour) + " " + str(minute) )
    event = Event.object.create( title = title , type = type , added_by = Customer.object.get( user_id = added_by ) , city_key = City.object.get( key = city_key ) , start_time = start_time  , main_photo_url = Media.objects.all()[0] , about = about )
    event.save()
    return HttpResponse("added")

def delete_event( request , event_id ):
    pass

def get_blog( request , blog_id ):
    pass