from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Laptop(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='laptops')
    model = models.CharField(max_length=255)
    serial_number = models.CharField(blank=True, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='laptops')
    published_date = models.DateField(null=True, blank=True)
    issue_description = models.TextField(blank=True)
    received_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} {self.model}"


class Repair(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='repairs')
    diagnosis = models.TextField()
    cost = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Repair for {self.laptop}'

