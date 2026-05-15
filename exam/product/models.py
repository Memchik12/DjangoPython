from django.db import models

class Product(models.Model):
    # БАЗОВАЯ ИЕРАРХИЯ: РАСЫ
    RACE_CHOICES = [
        ('chaos', 'Хаос'),
        ('imperium', 'Империум'),
        ('space_marine', 'Космо Десант'),
        ('xenos', 'Ксеносы'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название')

    # ПОЛЕ 1: РАСА (Жесткий выбор)
    race_type = models.CharField(
        max_length=50,
        choices=RACE_CHOICES,
        verbose_name='Раса',
        default='xenos'  # Теперь по умолчанию Ксеносы
    )

    # ПОЛЕ 2: ФРАКЦИЯ / ОРДЕН (Свободный ввод, зависит от расы)
    faction = models.CharField(
        max_length=100,
        verbose_name='Фракция (Орден/Легион)',
        help_text='Например: Blood Angels, Black Legion, Necrons'
    )

    miniatures_count = models.PositiveIntegerField(verbose_name='Кількість мініатюр в наборі', default=1)
    set_type = models.CharField(max_length=100, verbose_name='Тип набору')
    material = models.CharField(max_length=100, verbose_name='Матеріал')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    image_main = models.ImageField(upload_to='products/', verbose_name='Главное фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.title} ({self.get_race_type_display()} - {self.faction})"
# Create your models here.
