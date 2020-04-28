from django.contrib import admin
from .models import Simple,Languages,Framework,Movies,Actors, Entry, AccessRecord
# Register your models here.

admin.site.register(Simple)
admin.site.register(Languages)
admin.site.register(Framework)
admin.site.register(Movies)
admin.site.register(Actors)
admin.site.register(Entry)
admin.site.register(AccessRecord)