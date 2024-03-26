from rest_framework import serializers
from prompts.models import Prompt, Category



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'description']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class PromptSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Prompt
        fields = ['url', 'id', 'owner',
                  'title', 'content',  'description', 'starter_conversations', 'categories']

