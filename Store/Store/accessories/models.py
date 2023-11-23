from django.db import models
from django.utils.text import slugify

class Accesorie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2, default=0.0 )
    slug=models.SlugField(null=False,blank=False,unique=True)
    image=models.ImageField(upload_to='accessories/',null=False,blank=False)
    create_at=models.DateField(auto_now_add=True)
    count=models.IntegerField(null=False,blank=False,default=0)


    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self,self.title)
        super(Accesorie,self).save(*args,**kwargs)