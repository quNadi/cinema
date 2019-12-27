from django.db import models





class Movie(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=200,db_index=True)
    image= models.ImageField(upload_to='movie/%Y/%m/%d', blank=True)
    description=models.TextField(blank=True)
    release_date = models.PositiveIntegerField()
    duration = models.DurationField(null=False)
    avaiable = models.BooleanField(default=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return '{} ({})'.format(self.title, self.release_date)
