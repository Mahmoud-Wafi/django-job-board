from django.db import models

# Create your models here.
GENDER_TYPE=(
    ( "Male","Male")
    ,("Female","Female")
    )
JOB_TYPE=(
    ( "Full Time","Full Time")
    ,("Part Time","Part Time")
    )
       
       
    
class Job(models.Model):
    
    title= models.CharField(max_length=50)
    # location= models.CharField(max_length=100)
    job_type= models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField()
    publishAt=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary= models.DecimalField(max_digits=10 , decimal_places=2)
    # category=models.CharField(max_length=30) 
    experience=models.IntegerField(default=1)
    gender=models.CharField( max_length= 10 , choices=GENDER_TYPE)
    
    
    
    
    
    def __str__(self) -> str:
        return self.title