from rest_framework import serializers
from index.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['created_at','updated_at']