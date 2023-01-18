from django.db import models
from django.utils.translation import gettext_lazy as _

def vehicule_photo_directory_path(instance, filename):
    """ Vehicule Photo will be uploaded
        to MEDIA_ROOT/vehicule/<__str__/<filename>
    """
    return f'vehicule/{instance.__str__()}/{filename}'

# Create your models here.
class Vehicule(models.Model):
    """
        Vehicule Model for the system
    """

    class State(models.TextChoices):
        """
            Vehicule States
        """
        AVAILABLE =  'available', _('Available')
        OCCUPIED =   'occupied', _('Occupied')
        MAINTENANCE= 'maintenance', _('Maintenance')

    branch = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    short_name = models.CharField(max_length=20)
    # location GPS requires atleast 6 decimal places to get exact location
    # Default location to COZCYT
    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   blank=True, null=True,
                                   default=22.761202,
                                   )
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   blank=True, null=True,
                                   default=-102.579088,
                                   )

    state = models.CharField(
        max_length=20,
        choices=State.choices,
        default=State.AVAILABLE,
    )
    # TODO card_num (num or string)
    is_active = models.BooleanField(default=True, blank=True)
    photo = models.ImageField(upload_to=vehicule_photo_directory_path,
                                      blank=True,
                                      default='static/default-vehicule-photo.png'
                                      )
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.branch} {self.model} {self.year}'

    @property
    def is_available(self):
        return self.state == self.State.AVAILABLE


    class Meta:
        constraints = [
            # -90 <= latitude < 90
            models.CheckConstraint(
                check = models.Q(latitude__gte=-90) & models.Q(latitude__lt=90),
                name = 'check_latitude_bounds',
            ),
            # -180 <= longitude < 180
            models.CheckConstraint(
                check = models.Q(longitude__gte=-180) & models.Q(longitude__lt=180),
                name = 'check_longitude_bounds',
            )
        ]

