from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Post
from .forms import CommentForm
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


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
