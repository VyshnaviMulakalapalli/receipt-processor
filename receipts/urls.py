from django.urls import path
from .views import ProcessReceiptsView, GetPointsView

urlpatterns = [
    path('receipts/process', ProcessReceiptsView.as_view(), name='process_receipts'),
    path('receipts/<str:id>/points', GetPointsView.as_view(), name='get_points'),
]
