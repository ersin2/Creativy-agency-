from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Price(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например: Тариф Алилуя"
    )
    description = RichTextUploadingField(verbose_name="Описание")
    price = models.CharField(
        max_length=100, verbose_name="Цена", help_text="Например: 46$ / за месяц"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Цена'