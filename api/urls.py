from django.urls import path,include
from rest_framework_nested import routers
from article.views import ArticleViewSet,ArticleImageViewSet,RatingsViewSet,CategoryViewSet,AuthorViewSet

router = routers.DefaultRouter()
router.register('articles',ArticleViewSet,basename='articles')
router.register('categories',CategoryViewSet)

article_router = routers.NestedSimpleRouter(router,'articles', lookup = 'article')
article_router.register('images',ArticleImageViewSet,basename='article-images')
article_router.register('ratings',RatingsViewSet,basename='article-ratings')
article_router.register('authors',AuthorViewSet,basename='article-authors')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(article_router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
]
