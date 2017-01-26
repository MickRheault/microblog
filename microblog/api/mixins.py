from django.shortcuts import get_object_or_404

from rest_framework.response import Response


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