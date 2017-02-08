from django.shortcuts import render, render_to_response, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
import datetime

from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView
from django.core.cache import cache

from blog.models import Post
from comment.forms import CommentForm


def current_datetime(request, year=datetime.datetime.now().year):
    cache.clear()
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now
    if request.method == "GET":
        html = "<html><body><h1>It is now %s.</h1> %s </body></html>" % (now, year)
    return HttpResponse(html)

# @cache_page(60 * 15, key_prefix="site1", cache="filecache")
def get_index(request):
    posts = Post.objects.filter(publish=True)
    # return render(request, 'index.html', {'nowwwww': now})
    return render(request, 'index.html', locals())

def blog(request):
    posts = Post.objects.filter(publish=True)
    # return render(request, 'index.html', {'nowwwww': now})
    return render(request, 'blog/articles.html', locals())

def get_post(request, id):
    post = get_object_or_404(Post, id=id, publish=True)
    form = CommentForm()
    return render(request, 'blog/blog.html', {'post': post, 'form': form})

# def google(request):
#     return redirect('http://google.kg')


class GoogleView(RedirectView):
    url = 'http://google.kg/'
# Create your views here.
