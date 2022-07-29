from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

import main.models as models
import main.serializers as serializers


class FacultyAPI(ModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer


class RatingAPI(ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class ExtraPointAPI(ModelViewSet):
    queryset = models.ExtraPoint.objects.all()
    serializer_class = serializers.ExtraPointSerializer


class InviteKeyAPI(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.InviteKey.objects.all()
    serializer_class = serializers.InviteKeySerializer


class ExcelFileAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.ExcelFile.objects.all()
    serializer_class = serializers.ExcelFileSerializer


class CertificateAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
