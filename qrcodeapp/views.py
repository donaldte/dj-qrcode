from django.shortcuts import render
from .models import QR_code

# Create your views here.

def index(request, *args, **kwargs):
    context = {}
    if request.method == "POST":
        data = request.POST.get('data')
        obj = QR_code.objects.create(data=data)
        qr_code = obj.qr_code
        context = {
            'qr_code': qr_code
        }
    return render(request, 'index.html', context)