from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post
from hitcount.views import HitCountDetailView


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date')
    template_name = 'index.html'


class PostDetail(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    count_hit = True
