from django.contrib import admin
from .models import Enterpreneur

class EnterpreneurAdmin(admin.ModelAdmin):
    
    model = Enterpreneur

    def has_add_permission(self, request, obj=None):
        return False
	

# Register your models here.

admin.site.register(Enterpreneur, EnterpreneurAdmin)