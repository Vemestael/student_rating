from django.db import models


class Faculty(models.Model):
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name


class Rating(models.Model):
    faculty = models.ForeignKey("Faculty", on_delete=models.DO_NOTHING)

    date = models.DateField("Date", auto_now=False, auto_now_add=True)
    full_name = models.CharField("Full_name", max_length=255)
    group = models.CharField("Group", max_length=10)
    session = models.FloatField()
    extra = models.IntegerField()
    total = models.FloatField()

    def get_faculty(self):
        return self.faculty.name

    def get_date(self):
        return self.date

    def get_full_name(self):
        return self.full_name

    def get_group(self):
        return self.group

    def get_session(self):
        return self.session

    def get_extra(self):
        return self.extra

    def get_total(self):
        return self.total

    def __str__(self):
        return "%s | %s | %s" % (self.faculty, self.group, self.full_name)


class ExtraPoint(models.Model):
    student_id = models.ForeignKey("Rating", on_delete=models.CASCADE)

    date = models.DateField("Date", auto_now=False, auto_now_add=True)
    point = models.IntegerField()
    description = models.TextField("Description")
    certificate = models.FileField("Certificate", upload_to="certificate")

    def get_student_id(self):
        return self.student_id.full_name

    def get_date(self):
        return self.date

    def get_point(self):
        return self.point

    def get_description(self):
        return self.description

    def get_certificate(self):
        return self.certificate

    def __str__(self):
        return "%s | %s | %s | %s | %s" % (
            self.student_id, self.date, self.point, self.description, self.certificate)


class InviteKey(models.Model):
    invite_key = models.CharField("InviteKey", max_length=255)

    def __str__(self):
        return self.invite_key


class ExelFile(models.Model):
    uploaded_by_user = models.CharField("User", max_length=255, default='admin')
    excel_file = models.FileField("ExelFile", upload_to="excel")
    date = models.DateField("Date", auto_now=False, auto_now_add=True)

    def get_uploaded_by_user(self):
        return self.uploaded_by_user

    def get_excel_file(self):
        return self.excel_file

    def get_date(self):
        return self.date

    def __str__(self):
        return "%s | %s | %s" % (self.uploaded_by_user, self.excel_file, self.date)


class Certificate(models.Model):
    uploaded_by_student = models.ForeignKey(Rating, on_delete=models.CASCADE)
    certificate_file = models.FileField("CertificateFile", upload_to="certificate")
    date = models.DateField("Date", auto_now=False, auto_now_add=True)

    def get_uploaded_by_student(self):
        return self.uploaded_by_student.full_name

    def get_certificate_file(self):
        return self.certificate_file

    def get_date(self):
        return self.date

    def __str__(self):
        return "%s | %s | %s" % (self.uploaded_by_student, self.certificate_file, self.date)
