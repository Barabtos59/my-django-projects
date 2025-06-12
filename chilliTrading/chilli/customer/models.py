from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=40, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    utype = models.CharField(max_length=30, null=True, blank=True)

class warehose_details(models.Model):
    warehouse_id = models.CharField(max_length=30, null=True, blank=True)
    warehouse_name = models.CharField(max_length=40, null=True, blank=True)
    capacity = models.CharField(max_length=40, null=True, blank=True)
    warehouse_type = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=40, null=True, blank=True)
    owner_id = models.CharField(max_length=40, null=True, blank=True)
    contact_number = models.CharField(max_length=40, null=True, blank=True)


class farmer_details(models.Model):
    farmer_id = models.CharField(max_length=30, null=True, blank=True)
    farmer_name = models.CharField(max_length=40, null=True, blank=True)
    village = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    contact_number = models.CharField(max_length=40, null=True, blank=True)


class owner_detils(models.Model):
    owner_id = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    email_id = models.CharField(max_length=40, null=True, blank=True)
    contact_number = models.CharField(max_length=40, null=True, blank=True)


class request_for_storage(models.Model):
    request_id = models.CharField(max_length=30, null=True, blank=True)
    farmer_id = models.CharField(max_length=40, null=True, blank=True)
    warehouse_id = models.CharField(max_length=40, null=True, blank=True)
    quantity = models.CharField(max_length=40, null=True, blank=True)
    from_date = models.CharField(max_length=40, null=True, blank=True)
    to_date = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=40, null=True, blank=True)


class rate_chart(models.Model):
    warehouse_id = models.CharField(max_length=30, null=True, blank=True)
    rate_per_month = models.CharField(max_length=40, null=True, blank=True)
    per_square_meter = models.CharField(max_length=40, null=True, blank=True)
    min_space = models.CharField(max_length=40, null=True, blank=True)
    max_space = models.CharField(max_length=40, null=True, blank=True)

class forgotpassword(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)


class changepassword(models.Model):
    old_password = models.CharField(max_length=30, null=True, blank=True)
    new_password = models.CharField(max_length=40, null=True, blank=True)
    cunfirm_password = models.CharField(max_length=40, null=True, blank=True)

