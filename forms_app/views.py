from django.shortcuts import render
from .forms import BasicUserForm,CheckForm,ValidationForm,SubmitForm


# Create your views here.

def index_forms_app(request):
    return render(request,'forms_html/index.html')

# iti afiseaza o fereastra normala cu o forma simpla
def form_name_view_post(request):
    post_form = SubmitForm()
    if request.method == 'POST':
        post_form = SubmitForm(request.POST)

        if post_form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+post_form.cleaned_data['name'])
            print("EMAIL: "+post_form.cleaned_data['email'])
            print("TEXT: "+post_form.cleaned_data['text'])

    return render(request,'forms_html/basic_forms.html',{'post_form':post_form})

#iti verifica sa nu ai botzi in spate care sa-ti sparga site-ul
def form_name_view_validation(request):
    valid_form = ValidationForm()
    if request.method == 'POST':
        valid_form = ValidationForm(request.POST)

        if valid_form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+valid_form.cleaned_data['name'])
            print("EMAIL: "+valid_form.cleaned_data['email'])
            print("TEXT: "+valid_form.cleaned_data['text'])

    return render(request,'forms_html/validators.html',{'valid_form':valid_form})

#functie care verifica sa se potriveasca anumite criterii pe campurile formei
def form_name_view_check(request):
    check_form = CheckForm()
    if request.method == 'POST':
        check_form = CheckForm(request.POST)

        if check_form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+check_form.cleaned_data['name'])
            print("EMAIL: "+check_form.cleaned_data['email'])
            print("TEXT: "+check_form.cleaned_data['text'])

    return render(request,'forms_html/check.html',{'check_form':check_form})

#functie care ne ajuta sa scriem in baza de date direct din forma realizata
def users_views(request):
    user_model_form = BasicUserForm()

    if request.method == "POST":
        user_model_form = BasicUserForm(request.POST)
        if user_model_form.is_valid():
            user_model_form.save(commit=True)
            return index_forms_app(request) #aici te duce pe pagina de index care se numeste 'index_forms_app'
        else:
            print('ERROR FORM INVALID')

    return render(request,'forms_html/user_model_form.html',{'user_model_form':user_model_form})