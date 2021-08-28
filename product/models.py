from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class OptionValue(models.Model):
    value = models.CharField(max_length=255)
    option = models.ForeignKey(Option, related_name="values", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.option.name}] {self.value}"


class ListProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    options = models.ManyToManyField(Option, blank=True)
    fixed_options = models.ManyToManyField(OptionValue, blank=True)
    is_set = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name}"


class Quantity(models.Model):
    quantity = models.IntegerField()
    values = models.ManyToManyField(OptionValue, related_name="quantities")

    def __str__(self):
        if self.values.first():
            return f"[{self.values.first().option.name}] "+"/".join([value.value for value in self.values.all()])
        else:
            return f"[]"
