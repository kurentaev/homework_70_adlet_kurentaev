from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from webapp.managers import TaskProjectManager


class Projects(models.Model):
    start_date = models.DateField(
        verbose_name="Start date"
    )
    end_date = models.DateField(
        verbose_name="End date",
        blank=True,
        null=True
    )
    summary = models.CharField(
        verbose_name="Summary",
        max_length=100
    )
    description = models.TextField(
        verbose_name="Description"
    )
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        default=False,
        null=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Delete time',
        null=True,
        default=None
    )
    users = models.ManyToManyField(
        to=User,
        related_name='projects',
        blank=True,
        verbose_name='User'
    )

    objects = TaskProjectManager()

    def __str__(self):
        return f"{self.summary}"

    class Meta:
        db_table = "project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
