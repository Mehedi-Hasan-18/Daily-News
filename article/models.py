from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator,MinValueValidator
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='article')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='article')
    publishing_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline
    
class MustReadArticle(models.Model):
    headline = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='mustReadArticle')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='mustReadArticle')
    publishing_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline
class DontMissArticle(models.Model):
    headline = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='dontMissArticle')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='dontMissArticle')
    publishing_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline
class PopularArticle(models.Model):
    headline = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='popularArticle')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='popularArticle')
    publishing_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline

class ArticleImage(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='images')
    image = CloudinaryField('image',null=True, blank=True)

class MustReadArticleImage(models.Model):
    article = models.ForeignKey(MustReadArticle, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', null=True, blank=True)

class DontMissArticleImage(models.Model):
    article = models.ForeignKey(DontMissArticle, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', null=True, blank=True)

class PopularArticleImage(models.Model):
    article = models.ForeignKey(PopularArticle, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', null=True, blank=True)
    
class Ratings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='ratings')
    value = models.PositiveIntegerField(validators=[MaxValueValidator(4),MinValueValidator(0)])
    
    def __str__(self):
        return f'Review By {self.user.first_name} on {self.article.headline}'