from django.urls import path
from .views import MappingListCreateView, PatientMappingsView, MappingDeleteView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mappings'),
    path('<int:patient_id>/', PatientMappingsView.as_view(), name='patient-mappings'),
    path('delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
