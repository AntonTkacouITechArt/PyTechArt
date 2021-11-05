from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'pk': self.pk})


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

    def get_absolute_url(self):
        return reverse('department_detail', kwargs={
            'shop_pk': self.shop.id,
            'pk': self.id})


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # price = models.PositiveIntegerField(default=0)
    # price = models.FloatField()
    price = models.DecimalField(max_digits=100000000, decimal_places=3, validators=[validators.MinValueValidator()])
    is_sold = models.BooleanField(default=False)
    comments = ArrayField(base_field=models.CharField(max_length=200),
                          null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='item_relate',
        related_query_name='item_filter'
    )

    def __str__(self):
        return f"""id:{self.id} description:{self.description}price:{self.price
        } is_sold:{self.is_sold} department:{self.department} """

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={
            'shop_pk': self.department.shop.id,
            'dep_pk': self.department.id,
            'pk': self.pk})

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id', ]
        # constraints = [
        #     models.CheckConstraint(
        #         check=models.Q('price__gte' == 0),
        #         name='price_CK',
        #     ),
        # ]


class Statistics(models.Model):
    url = models.CharField(max_length=300)
    amount = models.PositiveIntegerField(default=0)

