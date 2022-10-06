from django.db import models

# Create your models here.
class contact_us(models.Model):
    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact_us"

class partners(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    category_id = models.IntegerField()
    image = models.ImageField(upload_to='partners',blank=True)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = "partners"

class partner_categories(models.Model):
    name = models.CharField(max_length=250)
    cat_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'partner_categories'

class clients(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients',blank=True)
    type_connect = models.CharField(max_length=255)

    class Meta:
        db_table = 'clients'
