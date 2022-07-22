from datetime import datetime

import django.forms as form

import main.models as models


class AddRatingForm(form.ModelForm):
    class Meta:
        model = models.Rating
        fields = ["faculty", "full_name", "group", "session", "extra"]
        widgets = {
            "faculty": form.Select(attrs={'style': 'height: 30px;'}),
        }


FACULTY_CHOICES = [
    (1, 'Информационных технологий'),
    (2, 'Экономический'),
    (3, 'Энергетический'),
    (4, 'Металургийный'),
    (5, 'Социально-гуманитарный'),
    (6, 'Машиностроения и сварки'),
    (7, 'Транспортных технологий'),
    (8, 'Инженерной и языковой подготовки'),
]

SESSION_CHOICES = [
    ('summer', 'summer'),
    ('winter', 'winter'),
]


def get_year():
    year = datetime.now().year - 5
    year_choices = []
    for i in range(6):
        year_choices.append((str(year + i), str(year + i)))
    return year_choices


year_choices = get_year()


class FilterForm(form.Form):
    faculty = form.ChoiceField(
        widget=form.Select(attrs={'class': 'custom-select w-75', 'onchange': 'form.submit()'}),
        choices=FACULTY_CHOICES,
        initial=1
    )
    session = form.ChoiceField(
        widget=form.RadioSelect(attrs={'onchange': 'form.submit()'}),
        choices=SESSION_CHOICES,
        initial='summer')
    year_picker = form.ChoiceField(
        widget=form.Select(attrs={'onchange': 'form.submit()'}),
        choices=year_choices
    )
    dysplayed = form.ChoiceField(choices=[
        (10, '10'),
        (25, '25'),
        (50, '50'),
        (100, '100'),
    ], widget=form.Select(attrs={'onchange': 'form.submit()'}), initial=10)
