from django.db import models
from users.models import Profile as User


# from django.contrib.auth.models import  User

class Category(models.Model):
    title = models.CharField("Category Title", max_length=150)
    description = models.TextField("Category Description", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    title = models.CharField('Tag title', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Post(models.Model):
    title = models.CharField("Post Title", max_length=150)
    descriptions = models.TextField("Post Description")
    image = models.ImageField("Post Image", blank=True, upload_to='post_image/')
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    text = models.TextField('Comment Message')
    post = models.ForeignKey(Post, verbose_name="commented post", on_delete=models.CASCADE, related_name='comments')
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
