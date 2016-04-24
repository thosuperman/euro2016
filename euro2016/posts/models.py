from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save # Right before the model is save do something
from django.utils.text import slugify


# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = upload_location, blank = True, null = True)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs = {"slug": self.slug})
        #return "/posts/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp"]

def create_slug(instance, new_slug = None):
    # converts "first post" => "first-post"
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    queryset = Post.objects.filter(slug = slug).order_by("-id")
    slug_exists = queryset.exists()
    if slug_exists:
        new_slug = "%s-%s" % (slug, queryset.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug

# any time a post is saved, this function will be called before saving
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender = Post)
