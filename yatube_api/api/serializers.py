from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Group, Comment, Follow, Post, User


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализирует поля объекта Post.
    Переопределено поле автора для отображения имени
    а не id.
    """
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализует поля объекта Group."""
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализирует поля объекта Comment.
    Переопределено отображение полей
    author и post.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализирует поля объекта Folllow.
    Переопределены отображения полей user, following,
    а также применен валидатор для проверки уникальности
    вышеуказанных полей объекта. Определен метод,
    запрещающий оформить объект подписки на самого себя.
    """
    user = serializers.CharField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя')
        return value
