from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(name="name", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(name="name", max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Items"
        ordering = ("name", "price", "created_at", "created_by")
