from django.urls import path
from blog import views
from blog.views import Posts, AddPost, ShowPost

urlpatterns = [
    path('', Posts.as_view(), name='post'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('shovpost/<int:pk>/', ShowPost.as_view(), name='shovpost')
]