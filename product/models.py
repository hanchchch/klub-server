from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.category}] {self.name}"


class Option(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name="options", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.product.name}] {self.name}"

class OptionValue(models.Model):
    name = models.CharField(max_length=255)
    option = models.ForeignKey(Option, related_name="values", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.option.name}] {self.name}"


class Quantity(models.Model):
    quantity = models.IntegerField()
    values = models.ManyToManyField(OptionValue, related_name="quantities")

    def __str__(self):
        return f"{self.values.first().option.product.name}"+"/".join([value.name for value in self.values.all()])


class SetProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="sets")
