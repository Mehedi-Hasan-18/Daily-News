from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article,Category,Author,ArticleImage,Ratings
from .serializer import ArticleSerializer,CategorySerializer,AuthorSerializer,ArticleImageSerializer,SimpleUserSerializer,RatingSerializer
from .permission import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category_id']
    search_fields = ['headline','body','category__name','author__name']
    
    @swagger_auto_schema(
        operation_summary="List all articles",
        operation_description="Retrieve a list of all articles with author and category info.",
        tags=["articles"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an article",
        operation_description="Get detailed information about a specific article by ID.",
        tags=["articles"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create an article",
        operation_description="Create a new article. Admin access only.",
        tags=["articles"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an article",
        operation_description="Update the entire article object. Admin only.",
        tags=["articles"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update an article",
        operation_description="Update one or more fields of an article. Admin only.",
        tags=["articles"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an article",
        operation_description="Delete an article by ID. Admin only.",
        tags=["articles"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class ArticleImageViewSet(ModelViewSet):
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article_id']
    
    def get_queryset(self):
        return ArticleImage.objects.filter(article_id = self.kwargs.get('article_pk'))
    
    def perform_create(self, serializer):
        serializer.save(article_id = self.kwargs.get('article_pk'))
        
    @swagger_auto_schema(
        operation_summary="List images of an article",
        operation_description="Retrieve all images attached to a specific article.",
        tags=["Article Images"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an article image",
        operation_description="Get a single article image by ID.",
        tags=["Article Images"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create an article image",
        operation_description="Upload a new image to a specific article. Admin only.",
        tags=["Article Images"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an article image",
        operation_description="Replace an image of the article. Admin only.",
        tags=["Article Images"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update an article image",
        operation_description="Update image metadata (e.g., caption). Admin only.",
        tags=["Article Images"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an article image",
        operation_description="Remove an image from the article. Admin only.",
        tags=["Article Images"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
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
    
    
    @swagger_auto_schema(
        operation_summary="List article ratings",
        operation_description="List all ratings for a specific article. Authenticated users only.",
        tags=["Ratings"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a rating",
        operation_description="Get a specific rating by ID.",
        tags=["Ratings"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a rating",
        operation_description="Submit a rating for an article. Authenticated users only.",
        tags=["Ratings"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a rating",
        operation_description="Fully update a rating. Authenticated users only.",
        tags=["Ratings"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a rating",
        operation_description="Update part of the rating details. Authenticated users only.",
        tags=["Ratings"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a rating",
        operation_description="Delete a user’s rating. Authenticated users only.",
        tags=["Ratings"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    @swagger_auto_schema(
        operation_summary="List categories",
        operation_description="Retrieve a list of all article categories.",
        tags=["Categories"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a category",
        operation_description="Get details of a specific category by ID.",
        tags=["Categories"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a category",
        operation_description="Add a new article category. Admin only.",
        tags=["Categories"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a category",
        operation_description="Update an existing category. Admin only.",
        tags=["Categories"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a category",
        operation_description="Partially update a category’s fields. Admin only.",
        tags=["Categories"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a category",
        operation_description="Remove a category by ID. Admin only.",
        tags=["Categories"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    @swagger_auto_schema(
        operation_summary="List authors",
        operation_description="Get a list of all article authors.",
        tags=["Authors"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an author",
        operation_description="Get detailed information about a specific author.",
        tags=["Authors"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create an author",
        operation_description="Add a new author. Admin access only.",
        tags=["Authors"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an author",
        operation_description="Update an author's information. Admin only.",
        tags=["Authors"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update an author",
        operation_description="Partially update an author’s information. Admin only.",
        tags=["Authors"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an author",
        operation_description="Delete an author from the system. Admin only.",
        tags=["Authors"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
