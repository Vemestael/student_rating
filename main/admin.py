from django.contrib import admin
import main.models as models


class RatingAdmin(admin.ModelAdmin):
    list_display = ('get_faculty', 'get_date', 'get_full_name', 'get_group', 'get_session', 'get_extra', 'get_total',)


class ExcelAdmin(admin.ModelAdmin):
    list_display = ('get_uploaded_by_user', 'get_excel_file', 'get_date')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('get_uploaded_by_student', 'get_certificate_file', 'get_date')


admin.site.register(models.Faculty)
admin.site.register(models.Rating, RatingAdmin)
admin.site.register(models.ExtraPoint)
admin.site.register(models.InviteKey)
admin.site.register(models.ExelFile, ExcelAdmin)
admin.site.register(models.Certificate, CertificateAdmin)
