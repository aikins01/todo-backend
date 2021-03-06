from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    STATUS = (
       (False, ('In Progress')),
       (True, ('Completed')),
   )
    PRIORITY = (
       (1, ('High')),
       (2, ('Medium')),
       (3, ('Low')),
   )
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False, choices=STATUS)
    date_created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    priority = models.PositiveSmallIntegerField(choices=PRIORITY,default=1)

    class Meta:
        ordering = ["-date_created","priority"]

    def _str_(self):
        return self.title