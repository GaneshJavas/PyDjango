# For taking response
from django.http import HttpResponse
# To render html file i.e., to send html files
from django.shortcuts import render

def home_page(request):
    # return HttpResponse("Finally I'm into the Development -- Homepage")
    return render(request, 'website/index.html')

def about_page(request):
    # return HttpResponse("Finally I'm into the Development -- About Page")
    return render(request,'website/about.html')

def contact_page(request):
    #return HttpResponse("Finally I'm into the Development -- Contact Page")
    return render(request,'website/contact.html')