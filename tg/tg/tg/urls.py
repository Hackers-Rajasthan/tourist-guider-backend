"""tg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tg_app.views import user_details , get_cities , get_events , get_attractions , get_blogs , get_magical_moments , get_food_items , get_event_detail , add_event , delete_event , get_blog, subscribe_city

urlpatterns = [
    url(r'^admin/', admin.site.urls),
## User
# 1. get user details
    url( r'^user/(?P<user_id>\w+)/$' , user_details ),

#2. get cities for a user
    url( r'^user/(?P<user_id>\w+)/cities/$' , get_cities ),   #//make_sure to have subscription true and false for each

#3. get all events for user
    url( r'user/(?P<user_id>\w+)/events/$' , get_events ),   #//proper categorization and ordering

#4. get attractions for a user, in a city
    url( r'user/(?P<user_id>\w+)/(?P<city>\w+)/attractions/$' , get_attractions ),

#4. toggle subscritption for a user, in a city
    url( r'user/(?P<user_id>\w+)/(?P<city>\w+)/subscribe/$' , subscribe_city ),

## City

#1. get attractions of a city
    url( r'city/(?P<city>\w+)/attractions/$' , get_attractions ),

#2. get blogs of a city
    url( r'city/(?P<city>\w+)/blogs/$' , get_blogs ),

#3. get events of a city
    url( r'city/(?P<city>\w+)/events/$' , get_events ),

#4. get magical moments of a city
    url( r'city/(?P<city>\w+)/magical_moments/$' , get_magical_moments ),

#5. get tried food of a city
    url( r'city/(?P<city>\w+)/food_items/$' , get_food_items ),

## Event
#1. get event detail
    url( r'event/(?P<event_id>\w+)/$' , get_event_detail ),

#2.1 add live event
#POST
    url( r'event/add/$' , add_event ),
#body={event}
#return {"id":"","message":"successful or failed"}

#2.2 delete live event
#DELETE
    url( r'event/(?P<event_id>\w+)/$' , delete_event ),
#body={"event":"id1"}
#return {message":"successful or failed"}

## Blog
#1. get blog detail
    url( r'blog/?P<blog_id>/$' , get_blog ),
]
