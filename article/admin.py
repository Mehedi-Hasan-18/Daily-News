from django.contrib import admin
from .models import Article,Category,Author,ArticleImage,Ratings

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(ArticleImage)
admin.site.register(Ratings)
