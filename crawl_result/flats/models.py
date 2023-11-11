from django.db import models

# Create your models here.
class Flat(models.Model):
    """Defines how are data stored in database."""
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)

    class Meta:
        """ Let the model know that the data are stored in table 'flats'."""
        db_table = 'flats'

    def __str__(self):
        return self.title
