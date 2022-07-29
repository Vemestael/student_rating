from rest_framework import serializers

import main.models as models


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'


class ExtraPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExtraPoint
        fields = '__all__'


class InviteKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InviteKey
        fields = '__all__'


class ExcelFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExcelFile
        fields = '__all__'


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Certificate
        fields = '__all__'
