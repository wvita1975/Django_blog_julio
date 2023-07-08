from django.urls import path
from .views import PostListView , PostDetailView, PostUpdateView, PostCreateView, PostDeleteView

urlpatterns = [
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="detail_view"),
    path('post/new',PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete")
]
