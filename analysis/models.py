# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import DynamicDocument

# Create your models here.

class Analysis(DynamicDocument):
    meta = {'collection': 'analysis'}
