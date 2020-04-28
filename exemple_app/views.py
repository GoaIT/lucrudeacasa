from django.shortcuts import render,redirect
from .forms import EntryForm
from .models import Entry, Simple


# Create your views here.

def index_exemple_app(request):
    entries = Entry.objects.all()
    simple_item = Simple.objects.all()
    context = {'entries':entries,'simple_item':simple_item}
    return render(request,'exemple_app/index.html',context) 

def new_entry(request):
    if request.method == "POST":
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            entry_form.save()
            print(entry_form)
            return redirect('index')    #ma redirectioneaza pe pagina index
    else:
        entry_form = EntryForm()   
    
    context = {'entry_form': entry_form} 
    
    return render(request, 'exemple_app/add.html', context)

