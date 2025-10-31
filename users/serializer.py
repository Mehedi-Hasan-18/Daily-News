from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['email','password','first_name','last_name' ,'membership_date','phone_number']
        
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name='CustomUser'
        fields = ['id','email','first_name','last_name' ,'membership_date','phone_number','is_staff']
        read_only_fields = ['is_staff']