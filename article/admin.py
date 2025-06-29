from django.contrib import admin
from .models import Article,Category,Author,ArticleImage,Ratings,DontMissArticle,PopularArticle,MustReadArticle,MustReadArticleImage,DontMissArticleImage,PopularArticleImage

# Register your models here.
admin.site.register(Article)
admin.site.register(DontMissArticle)
admin.site.register(PopularArticle)
admin.site.register(MustReadArticle)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(ArticleImage)
admin.site.register(MustReadArticleImage)
admin.site.register(DontMissArticleImage)
admin.site.register(PopularArticleImage)
admin.site.register(Ratings)
