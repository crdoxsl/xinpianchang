from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^home/',views.Home),
    url(r'^register/', views.Register),
    url(r'^video/', views.Video),
]