from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields="__all__"
        
    def create(self, validated_data):
        user=User.objects.create_user(
            phone_number=validated_data['phone_number'],
            full_name=validated_data['full_name'],
            blood_group=validated_data['blood_group'],
            password=validated_data['password']
        )
        return user