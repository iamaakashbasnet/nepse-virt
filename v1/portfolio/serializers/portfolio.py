from rest_framework import serializers

from v1.portfolio.models import Position


class PositionSerializer(serializers.ModelSerializer):
    stock = serializers.StringRelatedField()
    average_fill_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=True)

    class Meta:
        model = Position
        fields = '__all__'
