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
    
    def validate_username(self, value):
        if value=="root":
            raise serializers.ValidationError("username cant be `root`")
        return value


    def validate(self,data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords must match")
        return data
    
