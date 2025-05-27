from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article,Category,Author,ArticleImage,Ratings
from .serializer import ArticleSerializer,CategorySerializer,AuthorSerializer,ArticleImageSerializer,SimpleUserSerializer,RatingSerializer
from .permission import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class ArticleImageViewSet(ModelViewSet):
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        return ArticleImage.objects.filter(article_id = self.kwargs.get('article_pk'))
    
    def perform_create(self, serializer):
        serializer.save(article_id = self.kwargs.get('article_pk'))
    
class  RatingsViewSet(ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    
    def get_queryset(self):
        return Ratings.objects.filter(article_id = self.kwargs.get('article_pk'))
    
    def get_serializer_context(self):
        return {'article_id':self.kwargs.get('article_pk')}
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]
