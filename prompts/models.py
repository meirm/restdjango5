from typing import Iterable
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Category model for organizing prompts into categories.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    
    def save(self, *args, **kwargs):
        """
        Force name to Capitalized.
        """
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Prompt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    description = models.CharField(max_length=255, blank=True, default='', help_text="Describe the prompt.")
    starter_conversations = models.TextField(blank=True, default='',
        help_text="Provide some example sentences to start conversations.")
    categories = models.ManyToManyField(Category, related_name='prompts')
    owner = models.ForeignKey('auth.User', related_name='prompts', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']
        
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the content prompt.
        """
        options = {'title': self.title} if self.title else { 'title': 'Prompt' }
        super().save(*args, **kwargs)
        
        
        
class Vote(models.Model):
    prompt = models.ForeignKey(Prompt, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    vote = models.BooleanField()  # True for upvote, False for downvote
    created_at = models.DateTimeField(auto_now_add=True)