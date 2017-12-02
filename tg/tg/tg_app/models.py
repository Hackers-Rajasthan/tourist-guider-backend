from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Media( models.Model ):
    media_url = models.CharField( max_length = 255 , unique = True )
    media_type = models.CharField( max_length = 255 )
    def __str__(self):
        return self.media_type + " : " + self.media_url

class Customer( models.Model ):
#    name = models.CharField( max_length = 255 )
    user_id = models.CharField( max_length = 255 , primary_key = True )
    rating = models.FloatField( default = 0 )
#    about = models.CharField( max_length = 1000 )
    def __str__(self):
        return self.user_id


class City( models.Model ):
    key = models.AutoField( primary_key = True )
    name = models.CharField( max_length = 255 )
    main_photo_url = models.ForeignKey( Media )
    def __str__(self):
        return self.name

class Location( models.Model ):
    latitude = models.CharField( max_length = 255 )
    longitude = models.CharField( max_length = 255 )
    address_line = models.CharField( max_length = 1000 )
    postal_code = models.IntegerField()
    city = models.ForeignKey( City )
    def __str__(self):
        return self.address_line + " , " + self.city.__str__() + " - " + str(self.postal_code)

class Event( models.Model ):
    event_key = models.AutoField( primary_key = True )
    title = models.CharField( max_length = 255 )
    type = models.CharField( max_length = 255 )
    added_by = models.ForeignKey( Customer )
    city_key = models.ForeignKey( City )
    seen_by = models.IntegerField( default = 0 )
    posted_on = models.DateTimeField( default = timezone.now() )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    main_photo_url = models.ForeignKey( Media )
#    location = models.ForeignKey( Location )
    about = models.CharField( max_length = 1000 )
    def __str__(self):
        return self.title + " , " + " , start-time : " + str( self.start_time )

class Subscriber( models.Model ):
    city = models.ForeignKey( City )
    customer = models.ForeignKey( Customer )
    def __str__(self):
        return self.customer.__str__() + " : " + self.city.__str__()

