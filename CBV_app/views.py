from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

# Create your views here.

class IndexView(TemplateView): 
    template_name = 'cbv_app_html/index.html'

    #functie care iti permite sa mai adaugi continut in pagina folosint 'template tag'
    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # !!! ListView returneaza ca si atribut context_object_name 'school_list'
    # Django creaza un fisier html cu denumirea 'school_list.html'

    model = models.School
    #atributul care se va folosi in fisierele html pentru a apela lista de obiecte din tabela
    context_object_name = 'schools' 
    template_name = 'cbv_app_html/school_list.html'

class SchoolDetailView(DetailView):
    # !!! DetailView returneaza ca si atribut context_object_name doar 'school'
    context_object_name = 'school_details'  #aceasta valoare se va folosi in fisierele htm
    model = models.School
    template_name = 'cbv_app_html/school_detail.html'


class SchoolCreateView(CreateView):
    # CreateView cauta fisierul html school_form.html. 
    # !!! CreateView returneaza ca si atribut context_object_name 'form' si nu poate fi modificat
    template_name = 'cbv_app_html/school_form.html'
    fields = ["name","principal","location"]
    model = models.School


class SchoolUpdateView(UpdateView):
    # aceasta clasa o folosesti la un buton pe pagina DetailView a obiectului creat
    fields = ["name","principal"]
    model = models.School
    #adaugi 'template_name' ca sa stii pe ce pagina sa mergi sa faci modificarile la obiect
    template_name = 'cbv_app_html/school_form.html'


class SchoolDeleteView(DeleteView):
    # !!! DeleteView returneaza ca si atribut context_object_name doar 'school'
    model = models.School
    success_url = reverse_lazy("cbv_app:list")
    template_name = 'cbv_app_html/school_confirm_delete.html'

# cum se foloseste Views
class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')