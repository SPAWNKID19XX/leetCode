'''🔹 Задача 1. Базовый API
📋 Условие:

Создай APIView (не ViewSet),
которая возвращает список всех пользователей и позволяет создавать нового пользователя.

Требования:

Используй User из django.contrib.auth.models

GET → вернуть список пользователей (id, username, email)

POST → создать нового пользователя (username, email, password)

Добавь простую валидацию: если username уже существует → вернуть ошибку 400

💡 Подсказка:

сериализатор можно написать на основе Serializer, не ModelSerializer

код должен быть полностью рабочим (view + serializer)

не пиши urls.py, пока не нужно — только core logic


🔹 Task 1. Basic API
📋 Requirements:

Create an APIView (not a ViewSet) that returns a list of all users and allows creating a new user.

Specifications:

Use the User model from django.contrib.auth.models

GET → return a list of users (id, username, email)

POST → create a new user (username, email, password)

Add simple validation: if a username already exists → return a 400 Bad Request error

💡 Hint:

You can build the serializer using Serializer (not ModelSerializer)

The code should be fully functional (view + serializer)

Don’t write urls.py yet — focus only on the core logic
'''

#views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.
    """
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        Return new user in DB
        """
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


#serializers
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only = True)
    username = serializers.CharField()
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password)) 
        instance.save()
        return instance