from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'home'),
    url(r'^cours/(?P<cours_id>\d+)$', 'afficher_cours'),
)
