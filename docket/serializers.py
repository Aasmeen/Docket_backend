from rest_framework import (
    serializers as rest_serializers
)
from docket import (
    constants as docket_constants,
    models as docket_models
)

class DocketBase(rest_serializers.Serializer):
    name = rest_serializers.CharField()
    start_time = rest_serializers.TimeField()
    end_time = rest_serializers.TimeField()
    no_of_hours_worked = rest_serializers.IntegerField()
    rate_per_hour = rest_serializers.FloatField()
    supplier_name = rest_serializers.CharField()


class CreateDocket(DocketBase):
    po = rest_serializers.CharField(write_only=True)

    class Meta:
        model = docket_models.Docket

    def create(self, validated_data):
        po = validated_data.pop('po')
        validated_data['po_number'] = docket_constants.PO[
            validated_data['supplier_name']
        ][po]['po_number']
        validated_data['description'] = docket_constants.PO[
            validated_data['supplier_name']
        ][po]['description']
        return docket_models.Docket.objects.create(**validated_data)


class GetDocketList(DocketBase):
    po_number = rest_serializers.CharField()
    description = rest_serializers.CharField()

    class Meta:
        model = docket_models.Docket
        fields = '__all__'
