from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    image = models.FileField(upload_to='imageboard/post_images/')
    subject = models.TextField(max_length=40)
    description = models.TextField(max_length=600)
    date_added = models.DateField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['-date_added',]

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        return super(Post, self).save(*args, **kwargs)

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='replies')
    text = models.TextField(max_length=400)

    class Meta:
        verbose_name_plural = 'replies'

    def __str__(self):
        return self.text
