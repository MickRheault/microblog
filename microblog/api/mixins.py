from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status


class ListSerializerMixin(object):
    def get(self, request, *args, **kwargs):
        serializer = self.serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return self.model.objects.all()


class LastListSerializerMixin(ListSerializerMixin):
    def get_queryset(self):
        return self.model.objects.all()[:int(self.kwargs.get('limit', 1))]


class DetailSerializerMixin(object):
    def get(self, request, *args, **kwargs):
        serializer = self.serializer(self.get_queryset())
        return Response(serializer.data)

    def get_queryset(self):
        return get_object_or_404(self.model, pk=int(self.kwargs['pk']))


class CreationMixin(object):
    def put(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(**{self.author_field_name: request.user})
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class DeleteMixin(object):
    def delete(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=int(kwargs['pk']), **{self.author_field_name: request.user})
        object.delete()

        return Response(status=status.HTTP_410_GONE)