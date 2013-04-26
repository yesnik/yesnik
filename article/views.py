from django.views.generic import DetailView, ListView
from article.models import Article


class ArticleListView(ListView):

    model = Article

    def get_queryset(self):

        tag = self.kwargs['tag']
        print tag
        return Article.objects.filter(tag__tag_url=tag)
        