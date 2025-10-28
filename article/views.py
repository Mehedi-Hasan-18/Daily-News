from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article,Category,Author,ArticleImage,Ratings,MustReadArticle,DontMissArticle,PopularArticle,MustReadArticleImage,PopularArticleImage,DontMissArticleImage
from .serializer import ArticleSerializer,CategorySerializer,AuthorSerializer,ArticleImageSerializer,SimpleUserSerializer,RatingSerializer,MustReadArticleSerializer,DontMissArticleSerializer,PopularArticleSerializer,MustReadArticleImageSerializer,DontMissArticleImageSerializer,PopularArticleImageSerializer
from .permission import IsAdminOrReadOnly
from .pagination import ArticlePagination, ImagePagination
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404

# --------------------------ArticleViewSet---------------------
class MustReadArticleViewSet(ModelViewSet):
    queryset = MustReadArticle.objects.all()
    serializer_class = MustReadArticleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category_id']
    search_fields = ['headline','body','category__name','author__name']
    pagination_class = ArticlePagination
    
    @swagger_auto_schema(
        operation_summary="List Must Read articles",
        operation_description="Retrieve a list of all Must Read articles with author and category information.",
        tags=["Must Read Articles"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a Must Read article",
        operation_description="Get detailed information about a specific Must Read article by ID.",
        tags=["Must Read Articles"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Must Read article",
        operation_description="Create a new Must Read article. Admin access only.",
        tags=["Must Read Articles"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a Must Read article",
        operation_description="Update the entire Must Read article object. Admin only.",
        tags=["Must Read Articles"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Must Read article",
        operation_description="Update one or more fields of a Must Read article. Admin only.",
        tags=["Must Read Articles"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Must Read article",
        operation_description="Delete a Must Read article by ID. Admin only.",
        tags=["Must Read Articles"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class DontMissArticleViewSet(ModelViewSet):
    queryset = DontMissArticle.objects.all()
    serializer_class = DontMissArticleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category_id']
    search_fields = ['headline','body','category__name','author__name']
    pagination_class = ArticlePagination
    
    @swagger_auto_schema(
        operation_summary="List Don't Miss articles",
        operation_description="Retrieve a list of all Don't Miss articles with author and category information.",
        tags=["Don't Miss Articles"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a Don't Miss article",
        operation_description="Get detailed information about a specific Don't Miss article by ID.",
        tags=["Don't Miss Articles"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Don't Miss article",
        operation_description="Create a new Don't Miss article. Admin access only.",
        tags=["Don't Miss Articles"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a Don't Miss article",
        operation_description="Update the entire Don't Miss article object. Admin only.",
        tags=["Don't Miss Articles"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Don't Miss article",
        operation_description="Update one or more fields of a Don't Miss article. Admin only.",
        tags=["Don't Miss Articles"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Don't Miss article",
        operation_description="Delete a Don't Miss article by ID. Admin only.",
        tags=["Don't Miss Articles"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class PopularArticleViewSet(ModelViewSet):
    queryset = PopularArticle.objects.all()
    serializer_class = PopularArticleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category_id']
    search_fields = ['headline','body','category__name','author__name']
    pagination_class = ArticlePagination
    
    @swagger_auto_schema(
        operation_summary="List Popular articles",
        operation_description="Retrieve a list of all Popular articles with author and category information.",
        tags=["Popular Articles"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a Popular article",
        operation_description="Get detailed information about a specific Popular article by ID.",
        tags=["Popular Articles"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Popular article",
        operation_description="Create a new Popular article. Admin access only.",
        tags=["Popular Articles"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a Popular article",
        operation_description="Update the entire Popular article object. Admin only.",
        tags=["Popular Articles"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Popular article",
        operation_description="Update one or more fields of a Popular article. Admin only.",
        tags=["Popular Articles"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Popular article",
        operation_description="Delete a Popular article by ID. Admin only.",
        tags=["Popular Articles"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category_id']
    search_fields = ['headline','body','category__name','author__name']
    pagination_class = ArticlePagination
    
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
    
# ---------------ImageViewSet--------------------

    
class MustReadArticleImageViewSet(ModelViewSet):
    serializer_class = MustReadArticleImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = ImagePagination  
    
    def get_queryset(self):
        return MustReadArticleImage.objects.filter(article_id=self.kwargs.get('article_pk'))
    
    def perform_create(self, serializer):
        serializer.save(article_id=self.kwargs.get('article_pk'))
    
    @swagger_auto_schema(
        operation_summary="List Must Read article images",
        operation_description="Retrieve all images attached to a specific Must Read article.",
        tags=["Must Read Article Images"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a Must Read article image",
        operation_description="Get a single Must Read article image by ID.",
        tags=["Must Read Article Images"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Must Read article image",
        operation_description="Upload a new image to a specific Must Read article. Admin only.",
        tags=["Must Read Article Images"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a Must Read article image",
        operation_description="Replace an image of the Must Read article. Admin only.",
        tags=["Must Read Article Images"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Must Read article image",
        operation_description="Update image metadata for Must Read article. Admin only.",
        tags=["Must Read Article Images"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Must Read article image",
        operation_description="Remove an image from the Must Read article. Admin only.",
        tags=["Must Read Article Images"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class DontMissArticleImageViewSet(ModelViewSet):
    serializer_class = DontMissArticleImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = ImagePagination
    
    def get_queryset(self):
        return DontMissArticleImage.objects.filter(article_id=self.kwargs.get('article_pk'))
    
    def perform_create(self, serializer):
        serializer.save(article_id=self.kwargs.get('article_pk'))
    
    @swagger_auto_schema(
        operation_summary="List Don't Miss article images",
        operation_description="Retrieve all images attached to a specific Don't Miss article.",
        tags=["Don't Miss Article Images"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a Don't Miss article image",
        operation_description="Get a single Don't Miss article image by ID.",
        tags=["Don't Miss Article Images"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Don't Miss article image",
        operation_description="Upload a new image to a specific Don't Miss article. Admin only.",
        tags=["Don't Miss Article Images"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a Don't Miss article image",
        operation_description="Replace an image of the Don't Miss article. Admin only.",
        tags=["Don't Miss Article Images"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Don't Miss article image",
        operation_description="Update image metadata for Don't Miss article. Admin only.",
        tags=["Don't Miss Article Images"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Don't Miss article image",
        operation_description="Remove an image from the Don't Miss article. Admin only.",
        tags=["Don't Miss Article Images"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class PopularArticleImageViewSet(ModelViewSet):
    serializer_class = PopularArticleImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = ImagePagination
    
    def get_queryset(self):
        return PopularArticleImage.objects.filter(article_id=self.kwargs.get('article_pk'))
    
    def perform_create(self, serializer):
        serializer.save(article_id=self.kwargs.get('article_pk'))
    
    @swagger_auto_schema(
        operation_summary="List Popular article images",
        operation_description="Retrieve all images attached to a specific Popular article.",
        tags=["Popular Article Images"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a Popular article image",
        operation_description="Get a single Popular article image by ID.",
        tags=["Popular Article Images"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Popular article image",
        operation_description="Upload a new image to a specific Popular article. Admin only.",
        tags=["Popular Article Images"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a Popular article image",
        operation_description="Replace an image of the Popular article. Admin only.",
        tags=["Popular Article Images"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Popular article image",
        operation_description="Update image metadata for Popular article. Admin only.",
        tags=["Popular Article Images"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Popular article image",
        operation_description="Remove an image from the Popular article. Admin only.",
        tags=["Popular Article Images"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class ArticleImageViewSet(ModelViewSet):
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article_id']
    pagination_class = ImagePagination
    
    def get_queryset(self):
        return ArticleImage.objects.filter(article_id = self.kwargs.get('article_pk'))
    
    def perform_create(self, serializer):
        print("KWARGS:", self.kwargs)
        article = get_object_or_404(Article, pk=self.kwargs.get("article_pk"))
        serializer.save(article=article)
        
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
