from django.db.models import *
from image_optimizer.fields import OptimizedImageField

class Employer(Model):
    name = CharField(
        'Employer',
        max_length=256
    )
    about = TextField('About employer', blank=True, null=True)
    foundation_date = PositiveSmallIntegerField(default=1, verbose_name='Year of foundation date')

    email = EmailField(verbose_name='Email')
    number = CharField(max_length=13)

    company_photo = OptimizedImageField(verbose_name='Company photo',
                                        upload_to="employer_photos/%Y/%m/%d",
                                        optimized_image_output_size=(100, 100),
                                        optimized_image_resize_method='cover')
    city = CharField('Location of company',
                     max_length=64)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"


