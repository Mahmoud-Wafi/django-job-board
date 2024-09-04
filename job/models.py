from django.db import models
from django.utils.text import slugify 

# Create your models here.
GENDER_TYPE=(
    ( "Male","Male")
    ,("Female","Female")
    )
JOB_TYPE=(
    ( "Full Time","Full Time")
    ,("Part Time","Part Time")
    )
       
class Category(models.Model):
    nama=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nama
def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return f"Jobs/{instance.id}.{extension}"

class Job(models.Model):
    
    title= models.CharField(max_length=50)
    # location= models.CharField(max_length=100)
    job_type= models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField()
    publishAt=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary= models.DecimalField(max_digits=10 , decimal_places=2)
    category=models.ForeignKey('Category' , on_delete=models.CASCADE)
    experience=models.IntegerField(default=1)
    gender=models.CharField( max_length= 10 , choices=GENDER_TYPE)
    image = models.ImageField(upload_to=image_upload)
    
    slug= models.SlugField(null=True , blank=True)
    
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)
    
    
    
    def __str__(self) -> str:
        return self.title