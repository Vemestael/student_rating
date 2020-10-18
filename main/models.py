from django.db import models


class Faculty(models.Model):
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name


class Rating(models.Model):
    faculty = models.ForeignKey("Faculty", on_delete=models.DO_NOTHING)

    date = models.DateField("Date", auto_now=False, auto_now_add=True)
    full_name = models.CharField("Full_name", max_length=255)
    session = models.FloatField()
    extra = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return [self.faculty, self.date, self.full_name, self.session, self.extra, self.total]


class ExtraPoint(models.Model):
    student_id = models.ForeignKey("Rating", on_delete=models.CASCADE)

    date = models.DateField("Date", auto_now=False, auto_now_add=True)
    point = models.IntegerField()
    description = models.TextField("Description")

    def __str__(self):
        return [self.student_id, self.date, self.point, self.description]


class Professor(models.Model):
    faculty = models.ForeignKey("Faculty", on_delete=models.DO_NOTHING)

    full_name = models.CharField("Full_name", max_length=255)

    def __str__(self):
        return [self.faculty, self.full_name]


class Sertificate(models.Model):
    student_id = models.ForeignKey("Rating", on_delete=models.CASCADE)

    sertificate = models.ImageField("Sertificate", upload_to='upoads/', height_field=1280, width_field=720)

    def __str__(self):
        return [self.student_id, self.sertificate]