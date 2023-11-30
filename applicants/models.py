from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    math_rating = models.CharField(max_length=50)
    ukr_rating = models.CharField(max_length=50)
    hist_rating = models.CharField(max_length=50)
    selfpaying = models.BooleanField()
    motivation = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    def calculate_average_rating(self):
        return round((float(self.math_rating) * 0.5 +
                      float(self.ukr_rating) * 0.3 +
                      float(self.hist_rating) * 0.2), 2)


    def __str__(self):
        return (f"{self.name} {self.second_name}")