from django.urls import reverse
from django.test import TestCase, Client
from .models import Post, Comment, Profile, Vote  # Import all relevant models
from .forms import PostCreation
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='testuser@gmail.com', username='crack', password='testpassword')
        self.client.force_login(self.user)
        self.post = Post.objects.create(user=self.user, content='Test Content') # Correctly create post

    def test_get_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_post_new_post(self):
        post_data = {
            'content': 'New test post content',  # Use 'content' here
            'submit-post': 'submit'
        }
        response = self.client.post(reverse('home'), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Post.objects.count(), 2)
        new_post = Post.objects.last()
        self.assertEqual(new_post.content, 'New test post content') #check the content

    def test_post_new_comment(self):
        comment_data = {
            'comment': 'Test Comment',
            'submit-comment': self.post.id,
        }
        response = self.client.post(reverse('home'), data=comment_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.post_id, self.post.id)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content, 'Test Comment')

    def test_post_invalid_post(self):
        post_data = {
            'content': '',  # Invalid data (empty content)
            'submit-post': 'submit'
        }
        response = self.client.post(reverse('home'), data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'content', 'This field is required.')

    def test_like_post(self):
        like_data = {'vote': 1}  # 1 for like
        response = self.client.post(reverse('like_post', kwargs={'pk': self.post.pk}), data=like_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Vote.objects.filter(post=self.post, vote=1).count(), 1)

    def test_dislike_post(self):
        dislike_data = {'vote': -1}  # -1 for dislike
        response = self.client.post(reverse('like_post', kwargs={'pk': self.post.pk}), data=dislike_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Vote.objects.filter(post=self.post, vote=-1).count(), 1)

    def test_create_profile(self):
        self.assertEqual(Profile.objects.count(), 1)  # Check if profile is created on user creation