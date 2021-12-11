from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(null=True, max_length=50, verbose_name='Краткое описание')
    content = models.TextField(null=True, blank=True,verbose_name='Полное описание')
    basePrice = models.FloatField(null=True, blank=True,verbose_name='Базовая цена')
    currentPrice = models.FloatField(null=True, blank=True,verbose_name='Текущая цена')
    capacity = models.FloatField(null=True, blank=True,verbose_name='Количество на складе')
    article = models.FloatField(null=True, blank=True,verbose_name='Артикул')
    minCapacity = models.FloatField(null=True, blank=True,verbose_name='Мин. кол-во в заказе')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['title']


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.CharField(max_length=50, verbose_name='e-mail')
    adress = models.TextField(null=True, blank=True,verbose_name='Адрес')

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['name']


class Order(models.Model):
    client = models.ForeignKey('Client', null=True, on_delete=models.PROTECT, verbose_name='Клиент')
    good = models.ForeignKey('Bb', null=True, on_delete=models.PROTECT, verbose_name='Товар')
    order = models.CharField(max_length=50, verbose_name='Номер заказа')
    paymentMethod = models.CharField(max_length=12, verbose_name='Способ оплаты')
    shipMethod = models.CharField(max_length=50, verbose_name='Способ доставки')
    currentPrice = models.FloatField(null=True, blank=True,verbose_name='Текущая цена')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['date']
