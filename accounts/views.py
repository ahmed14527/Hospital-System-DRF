
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        request_body=AuthTokenSerializer,
        operation_description="User login API",
        responses={
            200: 'OK',
            400: 'Bad Request',
        },
    )
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        # Generate or retrieve the token for the user
        token, _ = Token.objects.get_or_create(user=user)

        # Check if the user is a superuser
        is_superuser = user.is_superuser

        # Return the token and superuser status in the response
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'is_superuser': is_superuser
        }, status=status.HTTP_200_OK)
        
        
        
class LogoutView(APIView):
    @swagger_auto_schema(
        operation_description="User logout API",
        responses={
            200: openapi.Response(description="OK"),
        },
    )
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"details": "Successfully logged out"}, status=status.HTTP_200_OK)


