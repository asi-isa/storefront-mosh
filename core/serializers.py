from djoser.serializers import UserCreateSerializer as BaseCreateSerializer


class UserCreateSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]
