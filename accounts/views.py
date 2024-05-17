from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token




@api_view(['POST'])
def signup(request):
    serializer= UserSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
        user= User.objects.get(username= request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token= Token.objects.create(user=user)
        return Response({'user': serializer.data, 'token': token.key}, status=status.HTTP_201_CREATED)

    return Response({'massage':'missing values'})


@api_view(['POST'])
def login(request):
    user= get_object_or_404(User, username= request.data['username'])
    if not user.check_password(request.data['password']):
        return Response('missing user', status=status.HTTP_400_BAD_REQUEST)
    token, created=Token.objects.get_or_create(user=user)
    serializer= UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data}, status= status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def token_back(request):
    return Response('passed for {}'.format(request.user.email))

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

