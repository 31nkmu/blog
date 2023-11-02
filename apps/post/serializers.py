from rest_framework import serializers
from .models import Post, PostImages
from ..category.models import Category


class PostListSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'category','owner', 'preview', 'category_name')

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'preview', 'images')

    def create(self, validated_data):
        # print(self, '!!!!!')
        print(validated_data, 'validated_data')
        print(self.context, 'asdasd')
        request = self.context.get('request')
        post = Post.objects.create(**validated_data)
        images_data = request.FILES.getlist('images')
        print(images_data, 'imagggessss')
        for image in images_data:
            PostImages.objects.create(image=image, post=post)
        return post
    


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source="category.name")
    images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"

        