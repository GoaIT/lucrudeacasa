from django.forms import ModelForm
from .models import Entry
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text',)  #aici poti folosi () cat si []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'textarea','placeholder':'Completeaza cu textul dorit...'})
    