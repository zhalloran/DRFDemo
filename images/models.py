# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from mongoengine import signals
import datetime

# Create your models here.

class Image(DynamicDocument):
    image_name = StringField(required=True)
    image_key = StringField(required=True, unique=True)
    status = StringField(default='active')
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {'collection': 'images'}

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        current_date = datetime.datetime.utcnow()
        if document.created_at == None:
            document.created_at = current_date
        document.updated_at = current_date


signals.pre_save.connect(Image.pre_save,
                         sender=Image)
