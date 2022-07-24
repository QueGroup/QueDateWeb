from django.db import models
from django.contrib.auth.models import AbstractUser


class Interests(models.Model):
    id = models.AutoField(primary_key=True)
    interest_category_title = models.CharField(max_length=64, blank=False, verbose_name='категория интересов')


class UserProfile(AbstractUser):

    id = models.AutoField(primary_key=True)

    phone = models.CharField(
        verbose_name='номер телефона',
        max_length=10,
        blank=True
    )

    town = models.CharField(
        verbose_name='город',
        max_length=128,
        blank=True
    )

    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True
    )

    MALE = 'Man'
    FEMALE = 'Woman'
    ANY = 'Another'

    GENDER_CHOICES = (
        (MALE, 'WOMAN'),
        (FEMALE, 'Ж'),
        (ANY, 'ДРУГОЕ')
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name='пол',
        max_length=7
    )

    interest_choice = models.ManyToManyField(
        Interests
    )

    interest_text = models.CharField(
        blank=True,
        max_length=64,
        verbose_name='другая категория интересов'
    )


class UserProfileMoreInfo(models.Model):

    user = models.OneToOneField(
        UserProfile,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )

    bio = models.CharField(
        verbose_name='биография',
        max_length=5000,
        blank=True
    )

    verification_date = models.DateField(
        verbose_name='дата подтверждения аккаунта',
        null=True
    )

