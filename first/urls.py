"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog.views import current_datetime, get_index, GoogleView
from django.conf import settings
from django.conf.urls.static import static

from comment.views import CommentViews
#from page.views import get_page


urlpatterns = [
    url(r'^$', get_index, name='index_page'),
    url(r'^current_datatime/$', current_datetime),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLSmi
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^posts/', include('blog.urls', namespace="posts")),
    url(r'^post/', include('blog.urls', namespace="post")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^comments_add/(?P<id>\d+)/$', CommentViews.as_view(), name="comment_add"),
    #url(r'^page/(?P<slug>\S+)/$', get_page, name="page"),
    url(r'^i18n/', include('django.conf.urls.i18n')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
