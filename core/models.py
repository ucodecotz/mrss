from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.utils import timezone

PROBLEM_TYPE = (
    ('H', 'Hardware problem'),
    ('S', 'Software problem'),
    ('N', 'Network problem'),
)
DEVICE_TYPE_CHOICE = (
    ('A', 'Android'),
    ('I', 'Ios')
)

DEVICE_BRAND_CHOICE = (
    ('T', 'Teckno'),
    ('S', 'Samsung'),
    ('U', 'Huawei'),
    ('O', 'Oppo'),

)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.FileField(upload_to='user_profile')

    class Meta:
        verbose_name_plural = ' Uer profile'

    def __str__(self):
        return str(self.user.username)


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class Problems(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='Pro_image', null=True, blank=True)
    # Problem_code = models.CharField(max_length=200, null=True, blank=True)
    problem_type = models.CharField(max_length=200,
                                    choices=PROBLEM_TYPE, null=True, blank=True)
    # solution = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    created_on = models.DateTimeField(default=timezone.now)
    device_type = models.CharField(max_length=200, choices=DEVICE_TYPE_CHOICE, null=True, blank=True)
    device_brand = models.CharField(max_length=200, choices=DEVICE_BRAND_CHOICE, null=True, blank=True)
    problem_desc = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Problems'

    def __str__(self):
        return self.title


class Solution(models.Model):
    problem_id = models.ForeignKey(Problems,
                                   on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE)
    content = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Solutions'

    def __str__(self):
        return self.user.user


class Comments(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    solution_id = models.ForeignKey(Solution, on_delete=models.CASCADE,
                                    null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return str(self.user)


# eg.

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title
