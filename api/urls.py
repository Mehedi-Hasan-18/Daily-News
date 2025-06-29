from django.urls import path, include
from rest_framework_nested import routers
from article.views import (
    ArticleViewSet, ArticleImageViewSet, RatingsViewSet, CategoryViewSet, AuthorViewSet,
    MustReadArticleViewSet, DontMissArticleViewSet, PopularArticleViewSet,
    MustReadArticleImageViewSet, PopularArticleImageViewSet, DontMissArticleImageViewSet
)

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('mustread-articles', MustReadArticleViewSet, basename='mustread-articles')
router.register('dontmiss-articles', DontMissArticleViewSet, basename='dontmiss-articles')
router.register('popular-articles', PopularArticleViewSet, basename='popular-articles')
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)

# Article nested routes
article_router = routers.NestedSimpleRouter(router, 'articles', lookup='article')
article_router.register('images', ArticleImageViewSet, basename='images')
article_router.register('ratings', RatingsViewSet, basename='ratings')

# Must Read Article nested routes
must_read_article_router = routers.NestedSimpleRouter(router, 'mustread-articles', lookup='mustread_article')
must_read_article_router.register('images', MustReadArticleImageViewSet, basename='mustread-articles-images')

# Don't Miss Article nested routes
dont_miss_article_router = routers.NestedSimpleRouter(router, 'dontmiss-articles', lookup='dontmiss_article')
dont_miss_article_router.register('images', DontMissArticleImageViewSet, basename='dontmiss-articles-images')

# Popular Article nested routes
popular_article_router = routers.NestedSimpleRouter(router, 'popular-articles', lookup='popular_article')
popular_article_router.register('images', PopularArticleImageViewSet, basename='popular-articles-images')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(article_router.urls)),
    path('', include(must_read_article_router.urls)),
    path('', include(dont_miss_article_router.urls)),
    path('', include(popular_article_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]