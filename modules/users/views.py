from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import AuthTokenSerializer, CreateUserSerializable, Users
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView


class CustomAuthToken(APIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']
        return Response({
            'token': token.key,
        })


@permission_classes([IsAuthenticated, ])
class Exit(APIView):
    http_method_names = ['get', ]

    def get(self, request):
        if request.user:
            Token.objects.filter(user=request.user).delete()
        return Response({
            'detail': 'Te esperamos pronto.',
        })


@permission_classes([IsAuthenticated, ])
class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializable
    queryset = Users.objects.all()
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        serializer.save(pro=self.request.user)


@permission_classes([IsAuthenticated, ])
class UpdateUser(UpdateAPIView):
    serializer_class = CreateUserSerializable
    queryset = Users.objects.all()
    http_method_names = ['put', ]


@permission_classes([IsAuthenticated, ])
class ListUser(ListAPIView):
    serializer_class = CreateUserSerializable
    queryset = Users.objects.all()
    http_method_names = ['get', ]
