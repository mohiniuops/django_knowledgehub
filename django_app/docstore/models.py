from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class appcat(models.Model):
    app=models.CharField("AppName",max_length=300)

    def __str__(self):
        return self.app


app_cat_o=appcat()

class doccat(models.Model):
    doccat_name=models.CharField("DocType",max_length=300)
    def __str__(self):
        return self.doccat_name


class app_name(models.Model):

    app=models.ForeignKey(appcat,max_length=300,default=None,on_delete=models.CASCADE)
    btitle=models.CharField("Title",max_length=300)
    pdf=models.FileField(upload_to='books/pdfs/')
    date_created=models.DateField(auto_now_add=True,blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    doc_type=models.ForeignKey(doccat,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.app

applist=app_name.objects.raw('SELECT * FROM app')
