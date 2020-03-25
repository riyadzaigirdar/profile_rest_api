from rest_framework import serializers
from .models import UserProfile,profileFeed


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
       }
    
    def create(self,validated_data):
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'], 
        )
        user.save()

        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = profileFeed
        fields = '__all__'
        extra_kwargs = {
            'user_profile':{
                'read_only':True
            }
        }
