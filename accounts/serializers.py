from rest_framework import serializers
from .models import User


def clean_email(value):
    if "root" in value:
        raise serializers.ValidationError("root cant be in email")
    

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required= True, write_only= True)


    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only":True},
            "email": {"validators": (clean_email,)},
        }
    
    
    def create(self, validated_data):
        del validated_data["password2"]
        del validated_data["is_active"]
        del validated_data["is_admin"]
        return User.objects.create_user(**validated_data)


    def validate_username(self, value):
        if value=="root":
            raise serializers.ValidationError("username cant be `root`")
        return value


    def validate(self,data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords must match")
        
        if User.objects.filter(email=data["email"]):
            raise serializers.ValidationError("this email is already taken.")

        return data
    

class UserUpdateSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = "__all__"
    
    
