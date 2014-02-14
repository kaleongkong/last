from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.client, name='client'),
    url(r'^users/add', views.add, name ='add'),
    url(r'^users/login', views.login, name ='login'),
    url(r'^TESTAPI/resetFixture',views.reset),
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
