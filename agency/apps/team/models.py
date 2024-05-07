from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

class Team(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например: Кума Кумович"
    )
    position = models.CharField(
        max_length=255, verbose_name="Должность", 
        help_text="Например: Senior Backend developer"
        )
    description = RichTextUploadingField(verbose_name="о себе")
    image = models.ImageField(
        upload_to="team", verbose_name="Фото", 
        help_text="Загружайте только jpg и png формат изображении"
    )
    age = models.IntegerField(verbose_name="Возраст")
    department = models.CharField(
        max_length=255, verbose_name="Департамент", help_text="Например: Android департамент"
    )
    experience = models.CharField(max_length=255, verbose_name="Стаж", help_text="3 года")
    phone = models.CharField(max_length=255, verbose_name="Телефон", help_text="+996771 771 771")
    email = models.CharField(max_length=255, verbose_name="email", help_text="kuma@gmail.com")
    address = models.CharField(max_length=255, verbose_name="адрес", help_text="Level 2, 11 York St, Sydney 2000")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="60px">'.format(self.image.url))
        
    class Meta:
        verbose_name_plural = 'Команда'


class SocialMedia(models.Model):
    ICON_CHOICES = [
        ('odnoklassniki', 'odnoklassniki'),
        ('instagram', 'instagram'),
        ('facebook', 'facebook'),
        ('linkedin', 'linkedin'),
        ('telegram', 'telegram'),
        ('whatsapp', 'whatsapp'),
        ('evernote', 'evernote'),
        ('twitter', 'twitter'),
        ('youtube', 'youtube'),
        ('skype', 'skype'),
        ('vk', 'vk'),
    ]
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    icon_socmedia = models.CharField(verbose_name="выбери что будет", choices=ICON_CHOICES, max_length=100)
    link = models.CharField(
        verbose_name="Ссылка на соцсети или мессенджеры", 
        help_text="https://www.instagram.com/edzn_bey/ или https:t.me/edzn21",
        max_length=255
    )
    def __str__(self):
        return f"имя: {self.team} /// ссылка: {self.link}"
    
    class Meta:
        verbose_name_plural = 'Соцсети и Мессенджеры'