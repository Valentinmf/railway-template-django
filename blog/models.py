from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    subtitle = models.TextField(blank=True, verbose_name="Sous-titre")
    category = models.CharField(max_length=255, blank=True, verbose_name="Catégorie")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    thumbnail = models.ImageField(blank=True, upload_to='blog', verbose_name="Bannière")
    body = RichTextField(blank=True, null=True)


    class Meta:
        ordering = ['created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
            return self.author.username if self.author else "L'auteur inconnu"

    def get_absolute_url(self):
        return reverse('blog:home')