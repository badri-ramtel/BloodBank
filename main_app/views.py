from django.shortcuts import render, redirect
from main_app.models import Blood_Bank
from django.contrib import messages

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
        cname = request.POST.get('contact_person_name', True)
        map = request.POST['map']
        email = request.POST['email']
        

        Blood_Bank.objects.create(bank_name = bname, address = address, phone_number = pnumber, contact_person_name = cname, map = map, email = email)

        messages.success(request, 'added successfully')

        return redirect('mainapp-home')
    
def edit(request):
    bloodbank = Blood_Bank.objects.get()
    if request.method == 'GET':
        return render(request, 'edit.html', {'bloodbank' : bloodbank})

    else:
        print('@@@@@@@@@@@@@@@@@')
        print(request.POST)
        bloodbank.bank_name = request.POST['bank_name']
        bloodbank.address = request.POST['address']
        bloodbank.phone_number = request.POST['phone_number']
        bloodbank.contact_person_name = request.POST.get['contact_person_name']
        bloodbank.map = request.POST['map']
        bloodbank.email = request.POST['email']

        bloodbank.save()

        return redirect('mainapp-home')


def delete(request):
    pass

