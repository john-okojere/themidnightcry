from django.db import models
from qrcode import *
import uuid

GENDER = (
    ('Male','Male'),
    ('Female','Female')
)

DEPARTMENT = (
    ('MEDIA', 'MEDIA'),
    ('WORSHIP', 'WORSHIP'),
    ('USHERING', 'USHERING'),
    ('TRANSPORT_&_LOGISTICS', 'TRANSPORT_&_LOGISTICS'),
    ('TECHNICAL', 'TECHNICAL')

)

class Volunteer(models.Model):
    uid = models.UUIDField( default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255 ,null=True, blank=True)
    gender = models.CharField(max_length=255, choices = GENDER  ,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=255 ,null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    address_street = models.TextField(null=True, blank=True) 
    address_city = models.CharField(max_length=255 ,null=True, blank=True)
    address_state = models.CharField(max_length=255 ,null=True, blank=True)

    local_church_name =  models.CharField(max_length=255 ,null=True, blank=True)
    local_church_branch =  models.CharField(max_length=255 ,null=True, blank=True)

    church_address_street = models.TextField(null=True, blank=True) 
    church_address_city = models.CharField(max_length=255 ,null=True, blank=True)
    church_address_state = models.CharField(max_length=255 ,null=True, blank=True)

    pastors_name = models.CharField(max_length=255 ,null=True, blank=True)
    time_in_church = models.CharField(max_length=255 ,null=True, blank=True)
    active_in_church = models.CharField(max_length=255 ,null=True, blank=True)

    department = models.CharField(max_length=255, choices=DEPARTMENT ,null=True, blank=True)
    consistency = models.BooleanField(null=True, blank=True)
    detailed_consistency = models.TextField(null=True, blank=True) 

    explained_interest = models.TextField(null=True, blank=True) 

    Emergency_contact_name = models.CharField(max_length=255 ,null=True, blank=True)
    Emergency_contact_relationship = models.CharField(max_length=255 ,null=True, blank=True)
    Emergency_contact_phone_number = models.CharField(max_length=255 ,null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True ,null=True, blank=True)


    

    def qr_code(self):
        qr_code = make(self.uid)
        basename = str(self.name) + '_QR_CODE.png'
        qr_code.save('media/QR_CODE/{}'.format(basename))
        return '/media/QR_CODE/{}'.format(basename)
    
    
    def save(self,force_insert=True,using='dataset'):
        super().save(force_insert)

    def save(self, *args, **kwargs):
        self.qr_code()
        return super().save(*args, **kwargs)
