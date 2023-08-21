from django import forms
from news.models import Categories, News


class CreateCategoriesModelForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"


class CreateNewsModelForm(forms.ModelForm):
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=Categories.objects.all().values_list("id", "name"),
        label="Categoria",
    )

    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].label = "URL da Imagem"
