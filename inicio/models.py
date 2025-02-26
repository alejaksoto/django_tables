from django.contrib.auth.models import AbstractUser
from django.db import models
from empresas.models import Empresa


class Usuario(AbstractUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)  # Permitir NULL
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    access_token = models.TextField()
    client_id = models.CharField(max_length=255, null=True, blank=True)  # Nuevo campo
    client_secret = models.CharField(max_length=255, null=True, blank=True)  # Nuevo campo
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=255)
    ROLES = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]
    rol = models.CharField(max_length=50, choices=ROLES, default='staff')
    

    def es_super_admin(self):
        return self.rol == 'super_admin'

    def es_admin(self):
        return self.rol == 'admin'
    
    def tiene_permiso(self, permiso):
        if self.rol and permiso in self.rol.permisos:
            return self.rol.permisos[permiso]
        return False
    
    def __str__(self):
        return self.username

class Meta:
        db_table = "inicio_usuario"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


        
class Flujomensajes(models.Model):
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    tipo = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    numero_cliente = models.CharField(max_length=255)
    

    