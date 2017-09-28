# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import views, permissions
from bson.objectid import ObjectId
from django.http import HttpResponse, Http404
import datetime

from models import Image

# Create your views here.
class ImageListView(views.APIView):

    def get(self, request):
        filters = {}
        query_set = Image.objects.filter(**filters)

        return HttpResponse(query_set.to_json())

    def post(self, request):
        kwargs = request.data
        new_image = Image(**kwargs)
        new_image.save()

        return HttpResponse(new_image.to_json())


class ImageDetailView(views.APIView):

    def get(self, request, image_id):
        filters = { '_id': ObjectId(image_id) }

        query_set = Image.objects.get(**filters)

        return HttpResponse(query_set.to_json())

    def put(self, request, image_id):
        kwargs = request.data
        filters = { '_id': ObjectId(image_id) }
        image_to_update = Image.objects.get(**filters)

        try:
            kwargs.pop('image_name')
        except:
            pass
        try:
            kwargs.pop('image_key')
        except:
            pass
        try:
            kwargs.pop('created_at')
        except:
            pass
        try:
            kwargs.pop('updated_at')
        except:
            pass

        image_to_update.modify(**kwargs)
        image_to_update.save()

        return HttpResponse(image_to_update.to_json())

    def delete(self, request, image_id):
        filters = { '_id': ObjectId(image_id) }

        old_image = Image.objects.get(**filters)

        image_archive = Image(**old_image.to_mongo().to_dict())
        image_archive.status = 'archived'
        image_archive.archived_at = datetime.datetime.utcnow()
        image_archive.switch_collection('images_archive')
        image_archive.save()

        old_image.delete()

        return HttpResponse(image_archive.to_json())
