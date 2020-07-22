"""from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length = 20, db_index = True, unique = True, verbose_name = 'Название')
    order = models.SmallIntegerField(default = 0, db_index = True, verbose_name ='Порядок')
    super_rubric = models.ForeignKey('SuperRubric',on_delete = models.PROTECT,
                                    null = True, blank = True, 
                                    verbose_name = 'Надрубрика')

class SuperRubricManager(models.Manager):
    def get_queryser(self):
        return super().get_queryset().filter(super_rubric__isnull=True)

class SuperRubric(Rubric):
    objects = SuperRubricManager()

    def __str__(self):
        return self.name
    class Meta:
        proxy = True
        ordering = ('order','name')
        verbose_name = 'Надрубрика'
        verbose_name_plural = 'Надрубрики'


class Post(models.Model):
    title = models.CharField(max_length = 40, 
                             verbose_name = 'Тема поста')
    rubric = models.ForeignKey(SubRubric, on_delete = models.PROTECT,
                              verbose_name = 'Рубрика')
    author = models.ForeignKey(User, on_delete = models.CASCADE, 
                               verbose_name = 'Автор объявления')
    is_active = models.BooleanField(default = True, db_index = True,
                                   verbose_name = 'Отображается или нет')
    main_image = models.ImageField(blank  =True, upload_to = get_timestamp_path,
                                  verbose_name='Заглавное изображение')"""