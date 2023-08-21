from django.db import models

class Endorser(models.Model):
    """Module that captures the name and surname of all endorsers and stores it in the database.
    """

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.surname}'