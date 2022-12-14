# Generated by Django 4.1.3 on 2022-11-12 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='наименование категории')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='SLUG')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CategoryColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(db_index=True, max_length=200, verbose_name='Категория по цвету')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='SLUG')),
            ],
            options={
                'verbose_name': 'Категория по цвету',
                'verbose_name_plural': 'Категория по цвету',
                'ordering': ('color',),
            },
        ),
        migrations.CreateModel(
            name='CategoryGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Категория по полу')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='SLUG')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория по полу',
                'ordering': ('gender',),
            },
        ),
        migrations.CreateModel(
            name='CategorySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(db_index=True, max_length=200, verbose_name='Категория по размеру')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='SLUG')),
            ],
            options={
                'verbose_name': 'Категория по размеру',
                'verbose_name_plural': 'Категория по размеру',
                'ordering': ('size',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='фото')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фото',
                'ordering': ('name', 'image'),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='наименование товара')),
                ('slug', models.SlugField(max_length=200, verbose_name='SLUG')),
                ('main_image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='главное фото')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('available', models.BooleanField(default=True, verbose_name='доступный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=' дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='категория')),
                ('color', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.categorycolor', verbose_name='ЦВЕТ')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.categorygender', verbose_name='Категория по полу')),
                ('image', models.ManyToManyField(blank=True, related_name='photos', to='store.image', verbose_name='фото')),
                ('size', models.ForeignKey(default='All Size', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.categorysize', verbose_name='РАЗМЕР')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
