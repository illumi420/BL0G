from django.shortcuts import render

from django.views import generic
from .models import Post
from hitcount.views import HitCountDetailView

# Create your views here.


# def index(request):                      # insert_me test
#     my_dict = {"insert_me": "I am from views.py"}
#     return render(request, 'index.html', context=my_dict)


class PostList(generic.ListView):        # Listing posts in Home-Page
    queryset = Post.objects.filter(status=1).order_by('-date')
    template_name = 'index.html'


class PostDetail(HitCountDetailView):    # Opens a post
    model = Post
    template_name = 'post_detail.html'
    count_hit = True
