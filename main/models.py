from django.db import models

FACULTY_CHOICES = {
    1: 'Информационных технологий',
    2: 'Экономический',
    3: 'Энергетический',
    4: 'Металургийный',
    5: 'Социально-гуманитарный',
    6: 'Машиностроения и сварки',
    7: 'Транспортных технологий',
    8: 'Инженерной и языковой подготовки'
}


class Faculty(models.Model):
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return FACULTY_CHOICES[self.id]


class Rating(models.Model):
    faculty = models.ForeignKey("Faculty", on_delete=models.DO_NOTHING)

    date = models.DateField("Date", auto_now=False, auto_now_add=True)
    full_name = models.CharField("Full_name", max_length=255)
    group = models.CharField("Group", max_length=10)
    session = models.FloatField()
    extra = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return "%s | %s | %s | %s | %s | %s | %s" % (self.faculty,
            self.date, self.full_name, self.group, self.session, self.extra, self.total)


class ExtraPoint(models.Model):
    student_id = models.ForeignKey("Rating", on_delete=models.CASCADE)

    date = models.DateField("Date", auto_now=False, auto_now_add=True)
    point = models.IntegerField()
    description = models.TextField("Description")

    def __str__(self):
        return "%s | %s | %s | %s" % (self.student_id, self.date, self.point, self.description)


class InviteKey(models.Model):
    invite_key = models.CharField("InviteKey", max_length=255)

    def __str__(self):
        return self.invite_key


class ExelFile(models.Model):
    uploaded_by_user = models.CharField("User", max_length=255, default='admin')
    exel_file = models.FileField("ExelFile", upload_to="./files/excel/")
    date = models.DateField("Date", auto_now=False, auto_now_add=True)

    def __str__(self):
        return "%s | %s | %s" % (self.uploaded_by_user, self.exel_file, self.date)
