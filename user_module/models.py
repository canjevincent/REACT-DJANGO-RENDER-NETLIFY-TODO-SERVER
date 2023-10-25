from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

alphanumericspacedashdotcomma = RegexValidator(r'^[a-zA-Z0-9 ,.-]*$', 'Only Alpha, numeric, dash, comma, dot and spaces are allowed.') 

# Create your models here.
class Item(models.Model):
  id = models.AutoField(primary_key=True)
  description = models.CharField(max_length=200, blank=False, null=False, unique=True, validators=[alphanumericspacedashdotcomma], default=None)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  updated_at = models.DateTimeField(auto_now=True)