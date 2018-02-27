from django.conf.urls import url
from . import views #importing views file
urlpatterns = [
    url(r'^$', views.index), #root url in index file
    url(r'^process$', views.process),
    url(r'^reset$', views.reset),
]
