from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.utils import timezone
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


decorators = [user_passes_test(lambda u: u.is_superuser)]

# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article

@method_decorator(decorators, name='dispatch')
class CreateArticleView(CreateView):
    redirect_field_name = 'articles/article_detail.html'

    form_class = ArticleForm
    model = Article

@method_decorator(decorators, name='dispatch')
class ArticleUpdateView(UpdateView):
    redirect_field_name = 'articles/article_detail.html'
    form_class = ArticleForm
    model = Article

@method_decorator(decorators, name='dispatch')
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:article_list')

@method_decorator(decorators, name='dispatch')
class DraftListView(ListView):
    redirect_field_name = 'articles/article_draft_list.html'

    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__isnull=True).order_by('created_date')






@user_passes_test(lambda u: u.is_superuser)
def article_publish(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.publish()
    return redirect("articles:article_list")


@login_required
def add_comment_to_article(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('articles:article_detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'articles/comment_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('articles:article_detail', pk=comment.post.pk)


@user_passes_test(lambda u: u.is_superuser)
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('articles:article_detail', pk=post_pk)
