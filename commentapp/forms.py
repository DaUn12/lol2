from django.forms import ModelForm

from commentapp.models import Comment


class CommnetCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

