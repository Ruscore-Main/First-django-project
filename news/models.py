from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Наименование')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата публикации')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Обновлено')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True, verbose_name = 'Фото')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано?')
    category = models.ForeignKey('Categories', on_delete = models.PROTECT, null = True, verbose_name = "Название категории")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']


class Categories(models.Model):
    title = models.CharField(max_length = 150, verbose_name = "Название категории", db_index = True)
    

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

    def __str__(self):
        return self.title
