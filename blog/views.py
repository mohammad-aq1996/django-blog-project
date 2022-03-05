from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Tag, Blogger, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/blog.html'
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    form_class = PostForm
    model = Post
    template_name = 'blog/create_post.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy('blog:post_list')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('blog:post_list')
            else:
                error = 'حساب کاربری شما فعال نمیباشد.'
                return render(request, 'blog/login.html', {'error': error})
        else:
            error = 'نام کاربری یا رمز عبور اشتباه میباشد.'
            return render(request, 'blog/login.html', {'error': error})
    else:
        return render(request, 'blog/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('blog:post_list')


class PostListView(ListView):
    """
    return descending(the newest post is first) list of all posts, tags, categories, 3 recent post, and admin profile.
    post list page contain 4 posts
    """
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Return descending list of all posts
        posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
        return posts

    def get_context_data(self, **kwargs):
        # Return tags, categories, 3 recent post, and admin profile.
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-published_at')[:3]
        context['blogger'] = Blogger.objects.get(id=1)
        return context


class PostDraftListView(LoginRequiredMixin, PostListView):
    login_url = '/login/'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('-created_at')


class PostCategory(PostListView):
    """
    inherit from 'PostListView' for other elements of this page.
    return posts that contain specific category slug
    also, there is no paginator and all of the posts display on one single page
    """
    paginate_by = 0

    def get_context_data(self, **kwargs):
        # Return posts that contain specific category slug
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__slug=self.kwargs['category'])
        return context


class SearchView(PostListView):
    """
    Get search box information and return posts their title contains search box information
    also, there is no paginator and all of the posts display on one single page
    """
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        q = self.request.GET.get('search')
        context['posts'] = Post.objects.filter(title__icontains=q)
        return context


class PostTag(PostListView):
    """
    inherit from 'PostListView' for other elements of this page.
    return posts that contain specific tags slug
    also, there is no paginator and all of the posts display on one single page
    """
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(PostTag, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(tags__slug=self.kwargs['tag'])
        return context


def post_detail_view(request, pk):
    """
    Return specific post that specify by primary key and contain comment section in this page
    Also, returns all tags, categories, 3 recent post, and admin profile.
    """
    context = dict()
    context['post'] = Post.objects.get(id=pk)
    context['tags'] = Tag.objects.all()
    context['categories'] = Category.objects.all()
    context['recent'] = Post.objects.all().order_by('-created_at')[:3]
    context['blogger'] = Blogger.objects.get(id=1)
    context['posts'] = Post.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            comment = Comment(post=context['post'],
                              name=name,
                              email=email,
                              title=title,
                              message=message)
            comment.save()

    return render(request, 'blog/single-blog.html', context)
