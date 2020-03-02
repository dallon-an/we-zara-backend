from django.db import models

class MainCategory(models.Model):
    gender = models.CharField(max_length = 20)

    class Meta:
        db_table = 'main_categories'

class SubCategory(models.Model):
    clothes_type  = models.CharField(max_length = 45)
    main_category = models.ForeignKey(MainCategory, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'sub_categories'

class Clothes(models.Model):
    name          = models.CharField(max_length = 45)
    main_category = models.ForeignKey(MainCategory, on_delete = models.SET_NULL, null = True)
    sub_category  = models.ForeignKey(SubCategory, on_delete = models.SET_NULL, null = True)
    price         = models.IntegerField(default = 0)
    description   = models.TextField(max_length = 500, default='')
    composition   = models.TextField(max_length = 300, default='')
    bestseller    = models.BooleanField(default = False)
    new           = models.BooleanField(default = False)
    size          = models.ManyToManyField('Size', through = 'ClothesSize')
    color         = models.ManyToManyField('Color', through = 'ClothesColor')
    care          = models.ManyToManyField('Care', through = 'ClothesCare')
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'clothes'

class ClothesImage(models.Model):
    clothes    = models.ForeignKey('Clothes', on_delete = models.SET_NULL, null = True)
    color      = models.ForeignKey('Color', on_delete = models.SET_NULL, null = True)
    main_image = models.URLField(max_length = 200)
    image1     = models.URLField(max_length = 200, null = True)
    image2     = models.URLField(max_length = 200, null = True)
    image3     = models.URLField(max_length = 200, null = True)
    image4     = models.URLField(max_length = 200, null = True)
    image5     = models.URLField(max_length = 200, null = True)
    image6     = models.URLField(max_length = 200, null = True)
    image7     = models.URLField(max_length = 200, null = True)

    class Meta:
        db_table = 'clothes_images'

class Size(models.Model):
    name = models.CharField(max_length = 20)

    class Meta:
        db_table = 'sizes'

class ClothesSize(models.Model):
    clothes = models.ForeignKey('Clothes', on_delete = models.SET_NULL, null = True)
    size    = models.ForeignKey('Size', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'clothes_sizes'

class Color(models.Model):
    name = models.CharField(max_length = 20)

    class Meta:
        db_table = 'colors'

class ClothesColor(models.Model):
    clothes = models.ForeignKey('Clothes', on_delete = models.SET_NULL, null = True)
    color   = models.ForeignKey('Color', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'clothes_colors'

class Care(models.Model):
    name = models.TextField(max_length = 1000, default = '')

    class Meta:
        db_table = 'cares'

class ClothesCare(models.Model):
    clothes = models.ForeignKey('Clothes', on_delete = models.SET_NULL, null = True)
    care    = models.ForeignKey('Care', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'clothes_cares'

class New(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete = models.SET_NULL, null = True)
    image         = models.URLField(max_length = 200)
    created_at    = models.DateTimeField(auto_now_add = True, null = True)
    updated_at    = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        db_table = 'news'
