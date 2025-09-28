from django.conf import settings
from django.db import models

class Petition(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def yes_count(self):
        return PetitionVote.objects.filter(petition=self, vote=True).count()


class PetitionVote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote = models.BooleanField(default=True)   # only "yes" for now

    class Meta:
        unique_together = ("petition", "user")