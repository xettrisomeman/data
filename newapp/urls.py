from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.HomePageView.as_view() , name='homepage'),
    path('signup/' , views.SignUpView.as_view(),name='signup'),
    path('logout/' , views.LogOutView.as_view() , name='logout'),
    path('login/' , views.LoginUserView.as_view() , name='login'),
    path('posts/' , views.ShowAllPost.as_view() , name='postlist'),
    path('addpost/' , views.CreatePostView.as_view() , name='addpost'),
    path('posts/<int:pk>/' , views.PostDetailView.as_view() , name='postdetail'),
    path('posts/delete/<int:pk>/' , views.PostDeleteView.as_view(),name='postdelete'),
    path('posts/update/<int:pk>/' , views.PostUpdateView.as_view() ,name='update'),
    


]
