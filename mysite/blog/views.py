from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Post, Category, Tag, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect


class PostListView(ListView):
    """
        List of published posts
        Display four posts per page
        Displays all tags, categories, blog owner profiles, and the last three posts
    """
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-published_at')[:3]
        return context


class PostDetail(View):
    """
        Details about a particular post with the option to leave a comment
        The superuser can edit and delete post on this page if they are logged in.
    """
    form_class = CommentForm
    template_name = 'blog/single-blog.html'

    def get(self, request, **kwargs):
        context = dict()
        context['post'] = Post.objects.get(id=self.kwargs['pk'])
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created_at')[:3]
        context['posts'] = Post.objects.all()
        context['comments'] = Comment.objects.filter(post__title=context['post'].title, status__exact='publish').order_by('-created_at')
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            post = Post.objects.get(id=self.kwargs['pk'])
            comment = Comment(post=post,
                              name=name,
                              email=email,
                              title=title,
                              message=message)
            comment.save()
            return self.get(request)
        return render(request, self.template_name, {'error': 'ایمیل شما صحیح نمیباشد.'})


class PostCategory(PostListView):
    """
        This page inherits from 'PostListView' for elements such as tags, search box, etc.
        Display posts containing specific category slug
        Also, there is no pagination and all posts appear on one page

    """
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__slug=self.kwargs['category'])
        return context


class SearchView(PostListView):
    """
        This page inherits from 'PostListView' for elements such as tags, categories, etc.
        Get information about search box and return posts whose titles contain search box information
        Also, there is no pagination and all posts appear on one page

    """
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        context['posts'] = Post.objects.filter(title__icontains=search)
        return context


class PostTag(PostListView):
    """
        This page inherits from 'PostListView' for elements such as tags, categories, etc.
        Display posts containing specific tags slug
        Also, there is no pagination and all posts appear on one page
    """
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(PostTag, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(tags__slug=self.kwargs['tag'])
        return context


def login_view(request):
    """
        If request is: 'get', login page only reload. Otherwise, request is 'post. then, it gets username and password
            from login template form
        If there was any user and that user was active, then user can log in. Otherwise, you can see the errors in
            the relevant template.
    """
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
                return render(request, 'blog/../templates/blog/login.html', {'error': error})
        else:
            error = 'نام کاربری یا رمز عبور اشتباه میباشد.'
            return render(request, 'blog/../templates/blog/login.html', {'error': error})
    else:
        return render(request, 'blog/../templates/blog/login.html')


@login_required
def logout_view(request):
    """
        Logout view function.
        This simply uses the built-in 'logout' method then redirects to the post list page
    """
    logout(request)
    return redirect('blog:post_list')


class PostDraftListView(LoginRequiredMixin, PostListView):
    """
        List of Draft posts.
        Login is required. If the user isn't logged in, it will automatically redirect to the login page.
        After login, the user can see draft posts. Also publish, update or delete a post
    """
    login_url = '/login/'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('-created_at')


class PostCreateView(LoginRequiredMixin, CreateView):
    """
        Creating new post
        Login is required. If user isn't logged in, it will automatically redirect to the login page
        After login superuser can add post
    """
    login_url = '/login/'
    redirect_field_name = 'blog/blog.html'
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
        Updating posts
        Login is required. If user isn't logged in, it will automatically redirect to the login page
        After login superuser can edit posts
    """
    login_url = '/login/'

    form_class = PostForm
    model = Post
    template_name = 'blog/create_post.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
        Deleting posts
        Login is required. If user isn't logged in, it will automatically redirect to the login page
        After login superuser can delete posts
    """
    login_url = 'login'
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy('blog:post_list')













# def post_detail_view(request, pk):
#     """
#     Return specific post that specify by primary key and contain comment section in this page
#     Also, returns all tags, categories, 3 recent post, and admin profile.
#     """
#     context = dict()
#     context['post'] = Post.objects.get(id=pk)
#     context['tags'] = Tag.objects.all()
#     context['categories'] = Category.objects.all()
#     context['recent'] = Post.objects.all().order_by('-created_at')[:3]
#     context['posts'] = Post.objects.all()
#     context['comments'] = Comment.objects.filter(post__title=context['post'].title, status__exact='publish').order_by('-created_at')
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             title = form.cleaned_data['title']
#             message = form.cleaned_data['message']
#             comment = Comment(post=context['post'],
#                               name=name,
#                               email=email,
#                               title=title,
#                               message=message)
#             comment.save()

#     return render(request, 'blog/single-blog.html', context)



















