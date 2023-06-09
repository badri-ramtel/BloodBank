from django.shortcuts import render, redirect
from main_app.models import Blood_Bank

# Create your views here.
def home(request):
    bloodbank = Blood_Bank.objects.all()  
    return render(request, 'main_app/home.html', {'bloodbank' : bloodbank })

def add(request):
    if request.method == 'GET':
        return render(request, 'main_app/add.html')
    
    else:
        print('@@@@@@@@@@@@@@@@@')
        print(request.POST)
        bname = request.POST['bank_name']
        address = request.POST['address']
        pnumber = request.POST['phone_number']
        cname = request.POST.get('contact_person_name')
        map = request.POST['map']
        email = request.POST['email']
        

        Blood_Bank.objects.create(bank_name = bname, address = address, phone_number = pnumber, contact_person_name = False, map = map, email = email)

        return redirect('mainapp-home')

