from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model



User=get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=100, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField('Изображение', upload_to='media/')

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%I:%M:%S%p')
            return format_html('<span style="color: #9cdd05; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime('%d.%m.%Y в %I:%M:%S%p')

    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%I:%M:%S%p')
            return format_html('<span style="color: #0d6efd; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime('%d.%m.%Y в %I:%M:%S%p')

    @admin.display(description='Изображения')
    def img(self):
        if self.image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img alt="Card title" width="50" height="50" class="img-fluid rounded-start" src="{}">'
                '</a>',
                self.image.url, self.image.url)
        else:
            return format_html('<span style="color: #b30500; font-weight: bold;">Нет изображения</span>')

    def __str__(self):
        return f'Advertisement(id={self.id}), title={self.title}, price={self.price}'

    class Meta:
        db_table = 'advertisement'


