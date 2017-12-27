from basicapp import views
from django.conf.urls import url

#Template tagging
app_name = 'basicapp'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]