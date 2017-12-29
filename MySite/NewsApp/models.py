from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="{% media %} '/media/'")

    def __str__(self):
        return self.title



'''class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_date = models.DateField(u'date',auto_now=True)
    comments_article = models.ForeignKey(Articles)
    #comments_author = models.ForeignKey(User)'''