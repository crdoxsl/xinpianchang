from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    uname = models.CharField(max_length=30,default='')
    email = models.EmailField(max_length=50)
    img = models.ImageField(upload_to='static/img', default='static/img/default.png')

    @classmethod
    def createuser(cls, username, password, email):
        u = cls(username = username, password = password, email = email)
        return u

class Follow(models.Model):
    uid = models.IntegerField()
    fuid = models.IntegerField(default='')

    @classmethod
    def createfollow(cls, uid, fuid):
        f = cls(uid=uid, fuid=fuid)
        return f



class Vedio(models.Model):
    src = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    img = models.CharField(max_length=200)

