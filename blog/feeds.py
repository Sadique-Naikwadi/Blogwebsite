import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostFeed(Feed):
    title = 'My Blog - Latest Posts'
    link = reverse_lazy('blog:post-list')
    description = 'Updates on new posts of my blog'

    # def link(self):
    #     return reverse_lazy('blog:post-list')

    def items(self):
        return Post.objects.all()[:5]
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish