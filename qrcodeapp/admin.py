from django.contrib import admin
from .models import QR_code

@admin.register(QR_code)
class QR_codeModelAdmin(admin.ModelAdmin):
    list_display = ('data', 'qr_code')
