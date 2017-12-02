from django.conf.urls import url

urlpatters = [
        url(r'^$' , 'tg_app.views.test' , name='test' ),
    ]