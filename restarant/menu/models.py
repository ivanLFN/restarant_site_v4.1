from django.db import models

class MenuPosition(models.Model):
    title = models.CharField('Название', max_length=25)
    date = models.DateTimeField('Дата создания')
    anons = models.CharField('Короткое описание', max_length=35)
    path_to_img = models.CharField('Путь к картинке', max_length=100)
    price = models.IntegerField('Цена')
    tag = models.CharField('Тип еды', max_length=50, default='none')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Позиции товаров'
