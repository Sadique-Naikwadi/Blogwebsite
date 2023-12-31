from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.9

    def items(self):
        return Post.objects.filter(status='PB')
    
    def lastmod(self, obj):
        return obj.updated_on
    

