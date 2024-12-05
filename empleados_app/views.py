from django.shortcuts import render, redirect
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleados(request):
    losEmpleados=Empleados.objects.all()

    return render(request,"gestionarEmp.html", {"misempleados":losEmpleados})

def registrarEmp(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre_empleado=request.POST["txtnombre"]
    telefono_empleado=request.POST["txttelefono"]
    correo_electronico=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    puesto_empleado=request.POST["txtpuesto"]
    fecha_contratacion=request.POST["txtfecha"]
    guardarVenta=Empleados.objects.create(id_empleado=id_empleado,nombre_empleado=nombre_empleado ,telefono_empleado=telefono_empleado,  correo_electronico=correo_electronico, direccion=direccion,puesto_empleado=puesto_empleado,fecha_contratacion=fecha_contratacion)
    return redirect("Empleados")

def seleccionarEmp(request,id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmp.html", {"misempleados": empleados})

def editarEmp(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre_empleado=request.POST["txtnombre"]
    telefono_empleado=request.POST["txttelefono"]
    correo_electronico=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    puesto_empleado=request.POST["txtpuesto"]
    fecha_contratacion=request.POST["txtfecha"]
    
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    empleados.id_empleado=id_empleado
    empleados.nombre_empleado=nombre_empleado
    empleados.telefono_empleado=telefono_empleado
    empleados.correo_electronico=correo_electronico
    empleados.direccion=direccion
    empleados.puesto_empleado=puesto_empleado
    empleados.fecha_contratacion=fecha_contratacion
    empleados.save()
    return redirect("Empleados")

def borrarEmp(request, id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    empleados.delete()

    return redirect("Empleados")