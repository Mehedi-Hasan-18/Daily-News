from rest_framework import serializers
from .models import Article,Category,Author,ArticleImage,Ratings
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','descriptions']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']
        
class ArticleImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ArticleImage
        fields = ['id','image']

class ArticleSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    author = AuthorSerializer()
    images = ArticleImageSerializer(many=True,read_only = True)
    class Meta:
        model = Article
        fields = ['id','headline','body','images','category','author','publishing_date','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']
    
class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_user_full_name')
    class Meta:
        model = get_user_model()
        fields = ['id','name']

    def get_user_full_name(self,obj):
        return obj.get_full_name()
    
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