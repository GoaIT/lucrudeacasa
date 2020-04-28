from django import forms
from django.core import validators
from .models import UserModel

#!!!!!!!!!!!!! modele de forms.FORM !!!!!!!!!!!!!!!
#forma simpla
class SubmitForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

################################################################

# am creat o metoda care sa valideze numele sa inceapa cu litera 'z'
# aici putem face orice functie dorim noi ca si criteriu
# vezi lectia 136, Sectiunea 18, din DjangoBootcamp Web Development
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Numele trebuie sa inceapa cu Z")

#o forma care valideaza anumite campuri.
#aici sunt detaliate cateva metode de validare a campurilor
class ValidationForm(forms.Form):
    #am adaugat criteriul de validare pe campul dorit
    name = forms.CharField(validators=[check_for_z])    
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    #definim n boocatcher pentru robotii care vor sa ne sparga site-ul.
    #totul este in spate, in fisierul html
    botcatcher = forms.CharField(required=True,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)],)

#####################################################################

#forma care verifica campurile dupa anumite criterii
#in cazul de fata verifica ca mail-urile sa fie identice
#tu poti defini ce vrei tu folosind metoda clean()
class CheckForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    #aici mai poti face pe fiecare camp in parte
    #cauta pe net metoda clean() sa vezi cum se foloseste.
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Mail-urile nu se potrivesc!")

####################################################################

#!!!!!!!!!!!!! modele de forms.ModelForm !!!!!!!!!!!!!!!
#acestea merg incorporate cu bazele de date

class BasicUserForm(forms.ModelForm):
    #!!AICI ADAUGI VALIDATORII DE CAMP DEFININD CAMPURILE!!
    #ex:  nume = forms.CharField(validators=[])
    class Meta:
        model = UserModel 
        fields = '__all__'    
        # exclude = ['nume_camp1','nume_camp2']
        # fields = ('nume_camp1','nume_camp2')

