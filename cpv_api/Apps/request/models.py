from django.db import models
from django.utils.translation import gettext_lazy as _
#from Apps.vehicule.models import Vehicule
import uuid
from django.contrib.auth import get_user_model
from django.conf import settings

from Apps.vehicule.models import Vehicule



def request_license_photo_directory_path(instance, filename):
    """ Profile Photo will be uploaded
        to MEDIA_ROOT/request/<id>/license/<filename>
    """
    return f'request/{instance.id}/license/{filename}'

def request_vehicule_photo_directory_path(instance, filename):
    """ Profile Photo will be uploaded
        to MEDIA_ROOT/request/<id>/vehicule/<filename>
    """
    return f'request/{instance.id}/vehicule/{filename}'

def request_gas_photo_directory_path(instance, filename):
    """ Profile Photo will be uploaded
        to MEDIA_ROOT/request/<id>/gas/<filename>
    """
    return f'request/{instance.id}/gas/{filename}'


class Request(models.Model):
    """
        Request Model for system
    """

    class State(models.TextChoices):
        """
            Request States
        """
        APPROVED = 'approved', _('Approved')
        DENIED   = 'denied', _('Denied')
        PENDING  = 'pending', _('Pending')
        FINISHED = 'finished', _('Finished')

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    vehicule = models.OneToOneField(
        #'Apps.vehicule',
        Vehicule,
        on_delete=models.SET_NULL,
        null=True,
    )
    state = models.CharField(
        max_length=20,
        choices=State.choices,
        default=State.PENDING,
    )
    # TODO approved by admin
    # admin_feedback_comment = models.TextField()

    # Photo user license
    user_license_photo = models.ImageField(upload_to=request_license_photo_directory_path,
                                           #blank=True,
                                          )
    # Photo vehicule
    vehicule_photo = models.ImageField(upload_to=request_vehicule_photo_directory_path,
                                       #blank=True,
                                      )
    # Photo gas charge *optional
    gas_photo = models.ImageField(upload_to=request_gas_photo_directory_path,
                                      blank=True,
                                      null=True,
                                      )
    mileage_initial = models.PositiveSmallIntegerField()
    mileage_final = models.PositiveSmallIntegerField(blank=True)
    comment = models.TextField(default='', blank=True)
    #description = models.TextField(default='', help_text="Describe your vehicule use")

    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user} {self.created_at} {self.id}'

    @property
    def can_be_deleted(self):
        return self.state == "pending" or self.state == "denied"




    class Meta:
        constraints = [
            #models.CheckConstraint(name='Cannot finished a request without a filling the final mileage!'),
            #                    check=models.Q( models.F('mileage_final')=='' ),
            models.CheckConstraint(name='Final Mileage is smaller than Initial Mileage!',
                                check=models.Q(mileage_final__gt=models.F('mileage_initial'))
                                ),
                                   
        ] 


