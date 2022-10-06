from django.db import models
from webapp.models.base import BaseModel


class Tasks(BaseModel):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Summary'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    status = models.ForeignKey(
        to='webapp.Statuses',
        related_name='status',
        on_delete=models.PROTECT,
        verbose_name='Status'
    )
    type = models.ManyToManyField(
        to='webapp.Types',
        related_name='type',
        blank=False
    )

    def __str__(self):
        return f"{self.summary} - {self.status} - {self.type}"

    class Meta:
        db_table = "tasks"
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
