
from django.core.exceptions import ValidationError
import sys
sys.path.append('/home/ardra/PycharmProjects/interact/interact_app')
from utils.util import *
from utils.mail_utils import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import MyModel, Post
from .serializers import InteractSerializer, PostSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrApp
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

#-----user login-----
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = MyModel.objects.get(email=email)
            print(user.password)
            if user.password == password:
                token, created = Token.objects.create(user=user)
                return Response({'token': token.key, 'message': 'Login successful'}, status=status.HTTP_200_OK)
            #if check_password(password, user.password):
                #return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except MyModel.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#-------------User registration-------
class UsersListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = MyModel.objects.filter(user = request.user.id)
        serializer = InteractSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def verify_email(request, key):
        key = request.META.get('KEY')
        if not key:
            raise ValidationError('Key is missing')

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'password':  request.data.get('password'),
        }
        password = password_validation(request.data.get('password'))
                #if not p:
                    #raise ValidationError('incorrect password format')
        confirm_password = request.data.get('confirm_password')
        #if not password == confirm_password:
            #raise ValidationError('mismatch in password')
        if not request.data.get('name') or not request.data.get('email') or not request.data.get('password'):
            raise ValidationError('required field is missing')
        #password = hashlib.md5(password.encode()).hexdigest()
        serializer = InteractSerializer(data=data)
        print('log')
        if serializer.is_valid():
            serializer.save()
            registered = send_verification_email()
            print(registered)
            if registered:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, *args, **kwargs):

        user_instance = self.get_object(user_id, request.id)
        if not user_instance:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        user_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class UsersDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, user_id, *args, **kwargs):

        user_instance = self.get_object(user_id, request.user.id)
        if not user_instance:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
             'name': request.data.get('name'),
            'email': request.data.get('email'),
            'password':  request.data.get('password'),
        }
        serializer = InteractSerializer(instance=user_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, user_id, *args, **kwargs):
    #     # instance = self.get_object()
    #     # self.perform_destroy(instance)
    #     # return Response(status=204)
    #
    #     user_instance = self.get_object(user_id, request.id)
    #     if not user_instance:
    #         return Response(
    #             {"res": "Object with user id does not exists"},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     user_instance.delete()
    #     return Response(
    #         {"res": "Object deleted!"},
    #         status=status.HTTP_200_OK
    #     )

#class PostViewSet(viewsets.ModelViewSet):
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer
class PostViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user.id
        print(user)
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'crested_by' : user
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated, IsOwnerOrApp]
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)













