from django.db import models

# Create your models here.
from django.db.models import Model, CharField, DateTimeField, URLField, TextField, \
    IntegerField


class ExternalLink(Model):
    url = URLField()
    comment = TextField(blank=True, null=True)
class Reference(Model):
    number=IntegerField()
    source=TextField()
class WikiPage(Model):
    name = CharField(max_length=50)
    last_modified = DateTimeField(auto_now=True)
