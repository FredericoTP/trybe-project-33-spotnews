from django import forms
from news.models import Categories


class CreateCategoriesModelForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
