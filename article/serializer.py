from rest_framework import serializers
from .models import Article,Category,Author,ArticleImage,Ratings,MustReadArticleImage,DontMissArticleImage,PopularArticleImage,PopularArticle,DontMissArticle,MustReadArticle
from django.contrib.auth import get_user_model
from rest_framework.fields import DateTimeField

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','descriptions']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']
        
# ----------------------ArticleImage------------------------
        
class ArticleImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ArticleImage
        fields = ['id', 'image']
class MustReadArticleImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = MustReadArticleImage
        fields = ['id','image']
class DontMissArticleImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = DontMissArticleImage
        fields = ['id','image']
class PopularArticleImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = PopularArticleImage
        fields = ['id','image']
        
        
# ------------Article--------------
class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()
    images = ArticleImageSerializer(many=True,read_only = True)
    publishing_date = DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    class Meta:
        model = Article
        fields = ['id','headline','body','images','category','types','author','publishing_date','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']
        
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        author_data = validated_data.pop('author')

        try:
            category = Category.objects.get(name=category_data['name'])
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")

        try:
            author = Author.objects.get(name=author_data['name'])
        except Author.DoesNotExist:
            raise serializers.ValidationError("Author with this name does not exist.")

        article = Article.objects.create(
            category=category,
            author=author,
            **validated_data
        )

        return article
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        author_data = validated_data.pop('author', None)

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if category_data:
            for attr, value in category_data.items():
                setattr(instance.category, attr, value)
            instance.category.save()

        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()

        instance.save()
        return instance
class MustReadArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()
    images = ArticleImageSerializer(many=True,read_only = True)
    class Meta:
        model = MustReadArticle
        fields = ['id','headline','body','images','category','author','publishing_date','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        author_data = validated_data.pop('author')

        try:
            category = Category.objects.get(name=category_data['name'])
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")

        try:
            author = Author.objects.get(name=author_data['name'])
        except Author.DoesNotExist:
            raise serializers.ValidationError("Author with this name does not exist.")

        must_read_article = MustReadArticle.objects.create(
            category=category,
            author=author,
            **validated_data
        )

        return must_read_article
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        author_data = validated_data.pop('author', None)

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if category_data:
            for attr, value in category_data.items():
                setattr(instance.category, attr, value)
            instance.category.save()

        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()

        instance.save()
        return instance
class DontMissArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()
    images = DontMissArticleImageSerializer(many=True,read_only = True)
    class Meta:
        model = DontMissArticle
        fields = ['id','headline','body','images','category','author','publishing_date','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        author_data = validated_data.pop('author')

        try:
            category = Category.objects.get(name=category_data['name'])
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")

        try:
            author = Author.objects.get(name=author_data['name'])
        except Author.DoesNotExist:
            raise serializers.ValidationError("Author with this name does not exist.")

        dont_miss_article = DontMissArticle.objects.create(
            category=category,
            author=author,
            **validated_data
        )

        return dont_miss_article
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        author_data = validated_data.pop('author', None)

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if category_data:
            for attr, value in category_data.items():
                setattr(instance.category, attr, value)
            instance.category.save()

        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()

        instance.save()
        return instance
class PopularArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()
    images = PopularArticleImageSerializer(many=True,read_only = True)
    class Meta:
        model = PopularArticle
        fields = ['id','headline','body','images','category','author','publishing_date','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        author_data = validated_data.pop('author')

        try:
            category = Category.objects.get(name=category_data['name'])
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")

        try:
            author = Author.objects.get(name=author_data['name'])
        except Author.DoesNotExist:
            raise serializers.ValidationError("Author with this name does not exist.")

        popular_article = PopularArticle.objects.create(
            category=category,
            author=author,
            **validated_data
        )

        return popular_article
        
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        author_data = validated_data.pop('author', None)

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if category_data:
            for attr, value in category_data.items():
                setattr(instance.category, attr, value)
            instance.category.save()

        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()

        instance.save()
        return instance
        
# --------------Users------------------
    
class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_user_full_name')
    class Meta:
        model = get_user_model()
        fields = ['id','name']

    def get_user_full_name(self,obj):
        return obj.get_full_name()
    
# -----------------------Ratings-------------------
    
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model = Ratings
        fields = ['id','value','user','article']
        read_only_fields = ['user','article']
        
    def get_user(self,obj):
        return SimpleUserSerializer(obj.user).data
        
    def create(self,validated_data):
        article_id = self.context.get('article_id')
        return Ratings.objects.create(article_id= article_id, **validated_data)