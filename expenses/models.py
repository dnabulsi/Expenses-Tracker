from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django import forms

EXPENSES_TYPE = (
    ('income','INCOME'),
    ('fixed_expenses', 'FIXED EXPENSES'),
    ('personal_expenses', 'PERSONAL EXPENSES'),
    ('debt_expenses', 'DEBT EXPENSES'),
)

# Create your models here.
class Profile(models.Model):
    # CASCADE = if user is deleted, delete the profile. if a profile is deleted, don't delete the user.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img.thumbnail((300,300))
            img.save(self.image.path)

class Expense(models.Model):
    date = models.DateField()
    expense_type = models.CharField(max_length=17, choices=EXPENSES_TYPE)
    amount = models.IntegerField()
    description = models.CharField(max_length=100)
    
    # if the user creates a post then the user is deleted, then the post is deleted as well.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.date}:{self.description} by {self.author}')

    def get_absolute_url(self):
        return reverse(f'{self.date.year}/{self.date.month}', kwargs={'pk': self.pk})