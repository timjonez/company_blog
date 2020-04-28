from . import views
from django.urls import path

app_name = 'articles'


urlpatterns = [
    path('',views.ArticleListView.as_view(),name='article_list'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', views.CreateArticleView.as_view(), name='article_new'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('drafts/', views.DraftListView.as_view(), name='article_draft_list'),
    path('article/<int:pk>/remove/', views.ArticleDeleteView.as_view(), name='article_remove'),
    path('article/<int:pk>/publish/', views.article_publish, name='article_publish'),
    path('article/<int:pk>/comment/', views.add_comment_to_article, name='add_comment_to_article'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),


]
