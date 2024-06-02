from django.db import models

# Create your models here.


class GovernmentID(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Telecommunications(models.Model):
    full_legal_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    government_identification = models.CharField(max_length=150)
    government_identification_number = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=150)
    email_address = models.EmailField(max_length=254)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    government_id = models.ForeignKey(GovernmentID, on_delete=models.CASCADE)
    # Note 1: Images and Files are large files in size for the database to handle.
    # Therefore, this implmentation of the "image uploads" and "file uploads" stores
    # the actual images and files in the computer's or server's file system and the
    # meta data information about the "images" and "files" are stored in the PostgreSQL database
    # 1. photo field
    government_identification_photo = models.ImageField(
        upload_to='portal/images/government_identification_photo')
    # 2. documents upload filed 1
    document_1 = models.FileField(upload_to='portal/images/document_1')
    document_2 = models.FileField(upload_to='portal/images/document_2')
    document_3 = models.FileField(upload_to='portal/images/document_3')
    # 3. documents upload filed 2
    # 4. user hand signature field
    #
    electronic_signature_full_legal_name = models.CharField(max_length=300)

    def __str__(self):
        return self.full_legal_name
