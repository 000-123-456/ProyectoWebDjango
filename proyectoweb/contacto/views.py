from django.shortcuts import render,redirect
from .forms import FormularioContacto
# Create your views here.
def contacto(request):

   formulario_contacto=FormularioContacto()

   if request.method=="POST":
      formulario_contacto=FormularioContacto(data=request.post)
      if formulario_contacto.is_valid():
         nombre=request.post.get("nombre")
         email=request.post.get("email")
         contenido=request.post.get("contenido")

         return redirect("/contacto/?aseptado")
      
   return render(request, "contacto/contacto.html", {'miformulario':formulario_contacto})