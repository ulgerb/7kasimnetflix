from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify # türkçe karakterleri ve boşlukları okunucak hale dönüştürüyor

class UserInfo(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   tel = models.CharField(("Telefon Numarası"), max_length=50)
   password = models.CharField(("Kullanıcı Şifresi"), max_length=50)
   sub_active = models.BooleanField(("Abonelik Durumu")) 

   def __str__(self):
      return self.user.username
class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   userinfo = models.ForeignKey(UserInfo, verbose_name=("Kullanıcı Bilgiler"), on_delete=models.CASCADE, null=True)
   name = models.CharField(("Profil Adı"), max_length=50)
   image = models.ImageField(("Profil Resmi"), upload_to='profile')
   password = models.CharField(("Profil Şifre"), max_length=50, default="0000")
   password_active = models.BooleanField(("Şifre Aktif Et"), default=False)
   kid = models.BooleanField(("Çocuk Hesabı"), default=False)
   login_active = models.BooleanField(("Girişli Profil"), default=False)
   slug = models.SlugField(("Slug"), null=True, blank=True)
   
   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)
   
   def __str__(self):
      return self.user.username + " " + self.name
   