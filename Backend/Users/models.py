from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin 
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone Number is required')
        user=self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self.create_user(phone_number, password, **extra_fields)
    
    

class UsersModel(AbstractBaseUser, PermissionsMixin):
   phone_number= models.CharField(max_length=12, unique=True)
   full_name= models.CharField( max_length=50)
   blood_group= models.CharField(max_length=50)
   password= models.CharField(max_length=50)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=True)
   is_superuser= models.BooleanField(default=False)
   
   objects=CustomUserManager()
   
   USERNAME_FIELD = 'phone_number'
   REQUIRED_FIELDS = ['full_name', 'blood_group', 'password']
   
   def __str__(self):
      return f"{self.full_name}-{self.phone_number}-{self.blood_group}"
