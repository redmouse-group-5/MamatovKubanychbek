from django.conf.urls import url
from blog.views import current_datetime, get_post, blog

urlpatterns = [
    #url(r'^$', current_datetime),
    url(r'^$', blog, name='articles'),
    url(r'^(?P<id>[0-9]+)/$', get_post, name='post'),
    url(r'^(?P<year>[0-9]{4})/$', current_datetime, name='post_year'),
]