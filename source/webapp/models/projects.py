from django.db import models
from django.urls import reverse


class Projects(models.Model):
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date", blank=True, null=True)
    summary = models.CharField(verbose_name="Summary", max_length=100)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.summary}"

    # def get_absolute_url(self):
    #     return reverse("webapp:project_view", kwargs={'pk': self.pk})

    class Meta:
        db_table = "project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"
