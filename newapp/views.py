from django.views.generic import (
    TemplateView , 
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView
)
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin



from .models import CustomUser , Post
from .forms import CustomUserAddForm , CustomUserLoginForm , CreatePostForm

class HomePageView(TemplateView):
    template_name = 'newapp/homepage.html'


class SignUpView(SuccessMessageMixin,CreateView):
    form_class = CustomUserAddForm
    model = CustomUser
    template_name = 'users/signup.html'
    success_url = reverse_lazy('homepage')
    success_message = 'User has been created'

class LogOutView(SuccessMessageMixin,LogoutView):
    template_name='users/logout.html'

class LoginUserView(SuccessMessageMixin,LoginView):
    model = CustomUser
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('homepage')
    success_message = 'You have been logged in!'

class ShowAllPost(ListView):
    model = Post
    context_object_name='posts'
    template_name = 'newapp/postlist.html'


class CreatePostView(SuccessMessageMixin,CreateView):
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy('postlist')
    template_name = 'newapp/post.html'
    success_message = 'Post has been created!'


    def get_context_data(self, **kwargs):
        kwargs['name']= 'Add'
        return super().get_context_data(**kwargs)

class PostDetailView(DetailView):
    model = Post
    context_object_name='post'
    template_name = 'newapp/postdetail.html'

class PostDeleteView(SuccessMessageMixin,DeleteView):
    model =Post
    context_object_name='post'
    template_name = 'newapp/postdelete.html'
    success_url = reverse_lazy('postlist')
    success_message = 'Post has been deleted'

class PostUpdateView(SuccessMessageMixin,UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'newapp/post.html'
    success_url = reverse_lazy('postlist')
    success_message = 'Post has been updated!'


    def get_context_data(self, **kwargs):
        kwargs['name']= 'Update'
        return super().get_context_data(**kwargs)

