from rest_framework import (
    generics as rest_generics,
    viewsets as rest_viewsets,
    response as rest_response
)
from docket import (
    constants as docket_constants,
    models as docket_models,
    serializers as docket_serializers
)

class GetSupplierName(rest_viewsets.ViewSet):
    def list(self, request):
        return rest_response.Response(docket_constants.PO.keys())


class GetPOList(rest_generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        print('------------1')
        supplier_name = self.kwargs['supplier_name']
        return rest_response.Response(docket_constants.PO.get(supplier_name, {}).keys())


class CreateDocket(rest_generics.CreateAPIView):
    serializer_class = docket_serializers.CreateDocket


class GetDocketList(rest_generics.ListAPIView):
    queryset = docket_models.Docket.objects.all()
    serializer_class = docket_serializers.GetDocketList
