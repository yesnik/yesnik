from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from article.models import Article
from article.views import ArticleListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yesnik.views.home', name='home'),
    # url(r'^yesnik/', include('yesnik.foo.urls')),


    url(r'^$', ListView.as_view(
        queryset=Article.objects.order_by('-published'),
        context_object_name='article_list',
        template_name='article/article_list.html'),
        name='article_list'),


    url(r'^(?P<tag>[a-z]+)/$', ArticleListView.as_view(), name='tag_article_list'),


    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
        model=Article,
        context_object_name='article',
        template_name='article/article.html'),
        name='article_detail'),

)
