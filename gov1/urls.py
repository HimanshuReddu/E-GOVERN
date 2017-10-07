from django.conf.urls import url
from . import views
from .views import ComplaintCreate,ComplaintList,BirthCreate,DeathCreate,ComplaintDelete,ComplaintUpdate,ComplaintShow
urlpatterns = [
    # /home/
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
   # url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^complaint/$', ComplaintCreate.as_view(), name='complaint'),
    url(r'^touristplaces/$', views.touristplaces, name='touristplaces'),
    url(r'^school/$', views.school, name='school'),
    url(r'^gallery/', ComplaintList.as_view(), name='aboutlist'),
    url(r'^hospital/$', views.hospital, name='hospital'),
    url(r'^gallary/$', views.gallary, name='gallary'),
    url(r'^birth/$', BirthCreate.as_view(), name='birth'),
    url(r'^death/$', DeathCreate.as_view(), name='death'),
    url(r'^edit/(?P<pk>\d+)/$', ComplaintDelete.as_view(), name='delete'),
    url(r'^delete/(?P<pk>\d+)/$', ComplaintUpdate.as_view(), name='update'),
    url(r'^show/', ComplaintShow.as_view(), name='show'),
]

