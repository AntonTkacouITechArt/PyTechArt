from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    staff_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id}{self.name} with staff {self.staff_amount}'

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ['id']


class Department(models.Model):
    sphere = models.CharField(max_length=200)
    staff_amount = models.PositiveIntegerField(default=0)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='department_relate',
        related_query_name='department_filter',
    )

    def __str__(self):
        return f'{self.id}-{self.sphere}-{self.shop}'

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['id']


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2),
    is_sold = models.BooleanField(default=False)
    comments = ArrayField(base_field=models.CharField(max_length=200))
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='item_relate',
        related_query_name='item_filter'
    )

    def __str__(self):
        return f"""id:{self.id} description:{self.description} 
        price:{self.price} is_sold:{self.is_sold} department:{self.department}"""

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id']
        constraints = [
            models.CheckConstraint(
                check=models.Q('price__gte' == 0),
                name='price_CK',
            )
        ]
