from django.contrib import admin
from tg_app.models import Media , Customer , City , Location , Event , Subscriber
# Register your models here.

admin.site.register( Media )
admin.site.register( Customer )
admin.site.register( City )
admin.site.register( Location )
admin.site.register( Event )
admin.site.register( Subscriber )
