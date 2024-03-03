from django.db.models import *
from apps.employee.models import Employee, EmployeeSkill
from apps.employer.models import Employer

class Vacancy(Model):
    company = OneToOneField(Employer,
                            verbose_name="Company",
                            on_delete=CASCADE)
    title = CharField('Title of the vacancy', max_length=256)
    salary_from = PositiveSmallIntegerField(verbose_name="Salary starts form (USD)")
    salary_to = PositiveSmallIntegerField(verbose_name="Salary ends in (USD)")
    description = TextField('Description of the vacancy')
    required_skills = ManyToManyField(EmployeeSkill, verbose_name="Required skills")
    created_date = DateTimeField(auto_now_add=True, verbose_name='Vacancy publication date')

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

