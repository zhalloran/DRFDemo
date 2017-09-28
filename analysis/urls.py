from rest_framework import routers
from views import AnalysisViewSet

analysis_router = routers.DefaultRouter()
analysis_router.register(r'analysis', AnalysisViewSet, base_name='analysis')