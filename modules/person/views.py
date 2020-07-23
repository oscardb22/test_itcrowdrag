from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CreatePersonsSerializable, Persons
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView


@permission_classes([IsAuthenticated, ])
class CreatePerson(CreateAPIView):
    serializer_class = CreatePersonsSerializable
    queryset = Persons.objects.all()
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        serializer.save(pro=self.request.user)


@permission_classes([IsAuthenticated, ])
class UpdatePerson(UpdateAPIView):
    serializer_class = CreatePersonsSerializable
    queryset = Persons.objects.all()
    http_method_names = ['put', ]


class ListPerson(ListAPIView):
    serializer_class = CreatePersonsSerializable
    queryset = Persons.objects.all()
    http_method_names = ['get', ]

    def perform_create(self, serializer):
        serializer.save(pro=self.request.user)


@permission_classes([IsAuthenticated, ])
class DeletePerson(DestroyAPIView):
    serializer_class = CreatePersonsSerializable
    queryset = Persons.objects.all()
    http_method_names = ['delete', ]
