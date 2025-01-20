from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from uuid import uuid4

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = CloudinaryField('image', null= True, blank=True, use_filename = False)
    followers = models.ManyToManyField(User, related_name='follower')

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def follow(self, user):
        self.followers.add(user)

    def unfollow(self, user):
        self.followers.remove(user)

    def is_following(self, user):
        if user in self.followers.all():
            return True
        else:
            return False

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    content = models.TextField()
    photo = CloudinaryField('image', null=True, blank=True, use_filename = False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]

    def likes_count(self):
        return self.votes.filter(vote=1).count()

    def dislikes_count(self):
        return self.votes.filter(vote=-1).count()
    
    @property
    def total_votes(self):
        return self.likes_count() - self.dislikes_count()

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=((1, 'Like'), (-1, 'Dislike')), default=0)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} voted {self.vote} on {self.post}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
