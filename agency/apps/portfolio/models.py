from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Portfolio(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например Заголовок: Сегодня все пришли на урок"
    )
    description = RichTextUploadingField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="news", verbose_name="Фото", 
        help_text="Загружайте только jpg и png формат изображении"
    )
    link = models.CharField(
        max_length=255, verbose_name="ссылка на проект", 
        help_text="Например: https://www.youtube.com/", 
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Портфолио'


class Partners(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например Заголовок: Сегодня все пришли на урок"
    )
    image = models.ImageField(
        upload_to="partners", verbose_name="Лого", 
        help_text="Загружайте только jpg и png формат изображении"
    )
    link = models.CharField(
        max_length=255, verbose_name="ссылка на страницу партнера", 
        help_text="Например: https://www.site.com/ или https://www.instagram.com/edzn_bey/?hl=ru", 
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.title} ---- {self.link}"
    
    class Meta:
        verbose_name_plural = 'Партнеры'