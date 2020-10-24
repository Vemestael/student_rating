import django.forms as form
import main.models as models


class AddRatingForm(form.ModelForm):
    class Meta:
        model = models.Rating
        fields = ["faculty", "full_name", "group", "session", "extra"]
        widgets = {
            "faculty": form.Select(attrs={'style': 'height: 30px;'}),
        }