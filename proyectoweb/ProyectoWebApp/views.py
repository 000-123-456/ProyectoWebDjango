from django.shortcuts import render, HttpResponse


#prueba
# Create your views here.
 
def home(request):

  return render(request, "ProyectoWebApp/home.html")




