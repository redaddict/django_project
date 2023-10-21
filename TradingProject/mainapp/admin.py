from django.contrib import admin
from mainapp.models import Nifty
# import import_export - use for csv import and export
from import_export.admin import ImportExportModelAdmin


class N_f1(ImportExportModelAdmin):
   list_display = ['BANKNIFTY','DATE','TIME','OPEN','HIGH','LOW','CLOSE','VOLUME']

# Register your models here.
admin.site.register(Nifty,N_f1)

