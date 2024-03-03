from django.db.models import *
from image_optimizer.fields import OptimizedImageField

class EmployeeSkill(Model):
    name = CharField('Skill', max_length=64)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class Employee(Model):
    fullname = CharField('Fullname', max_length=128)
    about = TextField('About the employee')
    experience = PositiveSmallIntegerField('Experience in years')
    skills = ManyToManyField(EmployeeSkill, verbose_name="skills")
    email = EmailField('Email')
    number = CharField(max_length=13)
    photo = OptimizedImageField(verbose_name="Employee Photo",
                                upload_to="employee_photos",
                                optimized_image_output_size=(500,500),
                                optimized_image_resize_method='cover')


