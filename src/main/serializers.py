from rest_framework import serializers
import main.models as models


class ExtraPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExtraPoint
        fields = ['student_id', 'date', 'point', 'description', 'certificate']