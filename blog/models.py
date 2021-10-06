from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):                              # Blog-Post
    title = models.CharField(max_length=200)

    # generating a valid URL, generally using data already obtained.
    slug = AutoSlugField(populate_from='title')

    thumbnails = models.ImageField(upload_to="", null=True, blank=True)
    overview = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()

    def __str__(self):
        return self.title
