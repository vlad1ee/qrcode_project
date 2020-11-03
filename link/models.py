from django.db import models


class Specification(models.Model):
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    company_description = models.TextField(null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    deadline = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30)
    document = models.FileField(upload_to='specifications/', null=True,
                                blank=True)
    created_at = models.DateField(auto_now_add=True)
