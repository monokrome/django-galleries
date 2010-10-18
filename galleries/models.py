from django.db import models
from imagekit.models import ImageModel
from django.template.defaultfilters import slugify
import random

class Effect(models.Model):
    class Meta(object):
        abstract = True

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __repr__(self):
        return self.name

class Photo(ImageModel):
    class IKOptions:
        spec_module = 'boundless.django.galleries.image_specs'
        chache_dir = 'galleries/cache'
        image_field = 'original_image'
        save_count_as = 'num_views'
        cache_dir = 'galleries/__cache__'

    title = models.CharField(max_length=64, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    original_image = models.ImageField(upload_to='galleries')
    num_views = models.PositiveIntegerField(editable=False, default=0)

    def thumbnail_url(self):
        return self.thumbnail.url

    def display_url(self):
        return self.display.url

    def __unicode__(self):
        return '%s: %s' % (self.pk, self.title,)

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)

        super(Photo,self).save(*args, **kwargs)

class Gallery(models.Model):
    class Meta(object):
        verbose_name_plural = 'galleries'

    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, blank=True)
    photos = models.ManyToManyField(Photo, related_name='galleries', null=True,\
         blank=True)
    parent = models.ForeignKey('self', related_name='subgalleries', blank=True, \
        null=True)

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)

        super(Gallery,self).save(*args, **kwargs)

    def random_photo(self):
        photos = self.photos.all()

        try:
            return photos[random.randrange(len(photos))]
        except:
            return None

    def __unicode__(self):
        return self.title

