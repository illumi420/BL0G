# to map the URL for the views we made
# When a Request for a page on the  BL0G app is made
# the Django controller takes over to look for the corresponding view via this file
# and then return the HTML response or a 404 not found error, if not found.
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
