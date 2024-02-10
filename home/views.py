from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("Hello")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("Projects")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("Contact")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        instance = Contact(name=name, email=email, phone=phone, message=message)
        instance.save()
        print('The data has been saved successfully')
        
    return render(request, 'contact.html')