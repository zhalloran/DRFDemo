# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from django.http import HttpResponse

from models import Analysis

# Create your views here.
class AnalysisViewSet(viewsets.ViewSet):
    lookup_field = 'name'

    def list(self, request):
        query_set = Analysis.objects.filter({})
        return HttpResponse(query_set.to_json())

    def retrieve(self, request, name=None):
        query_set = Analysis.objects.filter(name=name)
        return HttpResponse(query_set.to_json())

    def create(self, request):
        analysis = Analysis(**request.data)
        analysis.save()

        return HttpResponse(analysis.to_json())
        