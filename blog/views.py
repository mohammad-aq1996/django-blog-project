from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category, Tag, Blogger, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all().order_by('-created_at')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created_at')[:3]
        context['blogger'] = Blogger.objects.get(id=1)
        return context


class PostCategory(PostListView):
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__slug=self.kwargs['slug'])
        return context


class SearchView(PostListView):
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        q = self.request.GET.get('search')
        context['posts'] = Post.objects.filter(title__icontains=q)
        return context


class PostTag(PostListView):
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(PostTag, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(tags__slug=self.kwargs['tag'])
        return context


def post_detail_view(request, pk):
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
