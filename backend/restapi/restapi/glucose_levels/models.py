from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user_id


class GlucoseLevel(models.Model):
    # If a user is deleted, all glucose levels associated with that user should be deleted as well.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=255)  # Gerät
    serial_number = models.CharField(max_length=255)  # Seriennummer
    device_timestamp = models.DateTimeField()  # Gerätezeitstempel
    record_type = models.IntegerField()  # Aufzeichnungstyp
    glucose_value_history = models.FloatField(
        null=True, blank=True
    )  # Glukosewert-Verlauf mg/dL

    def __str__(self):
        return f"{self.user.user_id} - {self.device} - {self.device_timestamp}"
