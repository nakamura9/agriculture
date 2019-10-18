from django.db import models
from django.shortcuts import reverse
import datetime

class Project(models.Model):#process
    PROJECT_TYPES = [
        (1, 'Fixed Term'),#broiler chickens, 
        (2, 'Continuous')#egg layers, projects longer than 1 year
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('common.Profile', on_delete=models.CASCADE)
    start_date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=PROJECT_TYPES)

    def __str__(self):
        return self.name

    @property
    def type_string(self):
        return dict(self.PROJECT_TYPES)[self.type]

    @property
    def status(self):
        pass

    def get_absolute_url(self):
        return reverse("projects:project-details", kwargs={"pk": self.pk})
    

class Agent(models.Model):
    full_name = models.CharField(max_length=255)
    role = models.ForeignKey('projects.Role', on_delete=models.CASCADE)
    profile = models.ForeignKey('common.profile', on_delete=models.CASCADE, 
        null=True)

    def __str__(self):
        return self.full_name

class Role(models.Model):
    name = models.CharField(max_length=24)
    description= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class InputCategory(models.Model):
    name = models.CharField(max_length=24)
    description= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=24)
    symbol = models.CharField(max_length=6)
    description= models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Input(models.Model):
    description = models.CharField(max_length=255)
    unit_cost =models.DecimalField(max_digits=16, decimal_places=2)
    unit = models.ForeignKey('projects.unitofmeasure', on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.0)
    activity = models.ForeignKey('projects.activity', on_delete=models.CASCADE)
    #labour, medicine, fertelizer
    category = models.ForeignKey('projects.inputcategory', 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class ExpenseCategory(models.Model):
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    description = models.CharField(max_length=255)
    vendor =models.CharField(max_length=255, blank=True, default="")
    expense_category = models.ForeignKey('projects.expensecategory', 
        on_delete=models.CASCADE)
    activity = models.ForeignKey('projects.activity', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

class Activity(models.Model):#process stage
    project = models.ForeignKey('projects.project', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    estimated_cost = models.DecimalField(decimal_places=2, max_digits=16)
    actual_cost = models.DecimalField(decimal_places=2, max_digits=16, 
        blank=True, null=True)
    start_date = models.DateField()
    completed_date = models.DateField(null=True)
    responsible = models.ForeignKey('projects.agent', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:activity-details", kwargs={"pk": self.pk})
    
    @property
    def stage_num(self):
        num = 1
        for stage in self.project.activity_set.all():
            if stage.pk == self.pk:
                return num
            num += 1

        return num

    @property
    def status(self):
        if self.completed_date:
            return 'Complete'
        if datetime.date.today() < self.start_date:
            return 'Scheduled'

        return 'In Progress'



class Action(models.Model):# task taken as part of an activity
    date = models.DateField() 
    taken_by = models.ForeignKey('projects.agent', on_delete=models.CASCADE)
    description = models.TextField()
    estimated_cost = models.DecimalField(max_digits=16, decimal_places=2)
    activity = models.ForeignKey('projects.activity', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("projects:action-details", kwargs={"pk": self.pk})
    

class Milestone(models.Model):
    MILESTONE_STATUS = [
        (1, 'In Progress'),
        (2, 'Achieved'),
        (3, 'Failed'),
    ]
    date = models.DateField()
    review_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, default="")
    target = models.CharField(max_length=64)
    actual = models.CharField(max_length=64, blank=True, default="")
    review_comments = models.TextField(blank=True, default="")
    status = models.PositiveSmallIntegerField(choices=MILESTONE_STATUS, 
        default=1)
    activity = models.ForeignKey('projects.activity', on_delete=models.CASCADE, 
        null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:milestone-details", kwargs={"pk": self.pk})
    
    @property
    def status_string(self):
        return dict(self.MILESTONE_STATUS)[self.status]

class Produce(models.Model):
    name =models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    unit = models.ForeignKey('projects.unitofmeasure', null=True, 
        on_delete=models.SET_NULL)


class ProduceInventory(models.Model):
    profile = models.ForeignKey('common.profile', on_delete=models.CASCADE)
    location = models.TextField()



class ProduceInventoryItem(models.Model):
    inventory = models.ForeignKey('projects.produceinventory', 
        on_delete=models.CASCADE)
    produce = models.ForeignKey('projects.produce', on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.0)


class ProduceExtraction(models.Model):
    date = models.DateField()
    produce = models.ForeignKey('projects.produce', on_delete=models.CASCADE)
    quantity = models.FloatField()


    def increment_inventory(self):
        pass
