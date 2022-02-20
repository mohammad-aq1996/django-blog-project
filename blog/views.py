from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category, Tag, Blogger, Comment
from .forms import CommentForm


class BlogListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        blogs = Post.objects.all().order_by('-created_at')
        return blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created_at')[:3]
        context['blogger'] = Blogger.objects.get(id=1)
        return context


class BlogCategory(BlogListView):
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(BlogCategory, self).get_context_data(**kwargs)
        context['blogs'] = Post.objects.filter(category__slug=self.kwargs['slug'])
        return context


class SearchView(BlogListView):
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        q = self.request.GET.get('search')
        context['blogs'] = Post.objects.filter(title__icontains=q)
        return context


class BlogTag(BlogListView):
    paginate_by = 0

    def get_context_data(self, **kwargs):
        context = super(BlogTag, self).get_context_data(**kwargs)
        context['blogs'] = Post.objects.filter(tags__slug=self.kwargs['tag'])
        return context


def blog_detail_view(request, pk):
    context = dict()
    context['blog'] = Post.objects.get(id=pk)
    context['tags'] = Tag.objects.all()
    context['categories'] = Category.objects.all()
    context['recent'] = Post.objects.all().order_by('-created_at')[:3]
    context['blogger'] = Blogger.objects.get(id=1)
    context['blogs'] = Post.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            comment = Comment(blog=context['blog'],
                              name=name,
                              email=email,
                              title=title,
                              message=message)
            comment.save()

    return render(request, 'blog/single-blog.html', context)
