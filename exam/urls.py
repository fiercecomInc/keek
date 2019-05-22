from django.conf.urls import url
from . import views

app_name = 'exam'

urlpatterns = [
    url(r'^take$',views.exam,name="exam_start" ),

]
