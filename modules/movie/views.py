from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateMoviesSerializable, Movies, ListMoviesSerializable
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView


@permission_classes([IsAuthenticated, ])
class CreateMovie(CreateAPIView):
    serializer_class = CreateMoviesSerializable
    queryset = Movies.objects.all()
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        serializer.save(pro=self.request.user)


@permission_classes([IsAuthenticated, ])
class UpdateMovie(UpdateAPIView):
    serializer_class = CreateMoviesSerializable
    queryset = Movies.objects.all()
    http_method_names = ['put', ]


@permission_classes([IsAuthenticated, ])
class DeleteMovie(DestroyAPIView):
    serializer_class = CreateMoviesSerializable
    queryset = Movies.objects.all()
    http_method_names = ['delete', ]


class ListMovie(ListAPIView):
    serializer_class = ListMoviesSerializable
    queryset = Movies.objects.all()
    http_method_names = ['get', ]
