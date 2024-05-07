from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Service(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например: Web development"
    )
    description = RichTextUploadingField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="service", verbose_name="Фото", 
        help_text="Загружайте только jpg и png формат изображении"
    )
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return f"ID: {self.id} ----- Название: {self.title}"
    
    class Meta:
        verbose_name_plural = 'Услуги'