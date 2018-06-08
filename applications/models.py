from django.db import models

# Create your models here.

class Applications(models.Model):
    applicationid = models.CharField(db_column='ApplicationID', max_length=16, primary_key=True)
    first_name = models.CharField(db_column='FirstName', max_length=45, null=False)
    last_name = models.CharField(db_column='LastName', max_length=45, null=False)
    email = models.CharField(db_column='Email', max_length=254, null=False)
    status = models.CharField(db_column='Status', max_length=30, null=False)
    created_dtm = models.DateTimeField(db_column='CreatedDateTime', auto_now_add=True)
    updated_dtm = models.DateTimeField(db_column='UpdatedDateTime', null=True, default=None)

    class Meta:
        db_table = 'applications'
        get_latest_by = ['-created_dtm', '-updated_dtm']
