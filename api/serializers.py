from django.contrib.auth.models import User

from rest_framework import serializers
from oauth2_provider.models import Application

from .models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField()
	client_id = serializers.CharField(write_only=True)
	client_secret = serializers.CharField(write_only=True)

	def get_full_name(self, obj):
		return '{} {}'.format(obj.first_name, obj.last_name)

	
	def validate(self, data):
		try:
			application = Application.objects.get(client_id=data['client_id'])
			if data['client_secret'] != application.client_secret:
				raise serializers.ValidationError('Invalid client secret key')
		except Application.DoesNotExist as e:
			raise serializers.ValidationError('client id does not exists')
		return data

	def create(self, validated_data):
		print('validated data')
		print(validated_data)
		user = User.objects.create(
        	username=validated_data['username'],
        	email=validated_data['email'],
        	first_name=validated_data['first_name'],
        	last_name=validated_data['last_name']
		)
		
		user.set_password(validated_data['password'])
		
		user.save()
		
		return user

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'full_name', 'email', 'password', 'client_id', 'client_secret']
		write_only_fields = ['password', 'client_id', 'client_secret']
		extra_kwargs = {
			'first_name': {
				'required': True
			},
			'last_name': {
				'required': True
			},
			'email': {
				'required': True
			},
			'password': {
				'required': True
			}
		}

class PostSerializer(serializers.ModelSerializer):
	author_name = serializers.SerializerMethodField()
	def get_author_name(self, obj):
		return  '{} {}'.format(obj.author.first_name, obj.author.last_name)

	class Meta:
		model = Post
		fields = ['id', 'title', 'description', 'likes', 'author', 'author_name', 'last_updated']

class CommentSerializer(serializers.ModelSerializer):
	author_name = serializers.SerializerMethodField()
	def get_author_name(self, obj):
		return  '{} {}'.format(obj.author.first_name, obj.author.last_name)

	class Meta:
		model = Comment
		fields = ['id', 'post_id', 'author', 'author_name', 'comment_body', 'likes', 'last_updated', 'parent_comment_id']