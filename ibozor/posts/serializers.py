from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'desc', 'price', 'images')

    def create(self, validated_data):
        """
        Create and return a new `Posts` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Posts` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('desc', instance.desc)
        instance.code = validated_data.get('price', instance.price)
        instance.save()
        return instance
