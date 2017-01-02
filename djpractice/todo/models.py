from __future__ import unicode_literals
from django.db import models


class BaseContent(models.Model):

    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                         default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def switch(self):
        self.active = {2: 0, 0: 2}[self.active]
        self.save()


class Task(BaseContent):

    STATE_CHOICES = ((0, 'ToDo'), (1, 'Doing'), (2, 'Done'))
    PRIORITY_CHOICES = ((0, 'Low'), (1, 'Medium'), (2, 'High'))

    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.PositiveIntegerField(choices=STATE_CHOICES,
                                        default=0)
    priority =  models.PositiveIntegerField(choices=PRIORITY_CHOICES,
                                            default=1)
    due_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name
