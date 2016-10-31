from django.conf.urls import url
from . import views

app_name='facemash'
urlpatterns=[
    url(r'^$',views.Index.as_view(), name='index'),
    url(r'^submit/',views.selected, name='select'),
    ]
