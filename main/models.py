from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.name

class Personalskill(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    def __str__(self):
        return self.name

class Profisionalskill(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()

class Categoriya(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()
    number = models.IntegerField()
    def __str__(self):
        return self.name

class Blog(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    data = models.DateField(auto_now=True)
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.name
