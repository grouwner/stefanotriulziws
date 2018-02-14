from django.db import models
from django.utils import timezone


class Gallery(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo_galleria = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, default='', )
    Gallery_Thumb = models.ImageField(max_length=255, upload_to='../static/', default='')
    # photo = models.ManyToManyField(Photo, blank=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titolo_galleria

    class Meta(object):
        ordering = ['my_order']

class Photo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo_photo = models.CharField(max_length=250)
    Upload_photo = models.ImageField(max_length=255, upload_to='static/', default='')
    gallery = models.ManyToManyField(Gallery, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titolo_photo