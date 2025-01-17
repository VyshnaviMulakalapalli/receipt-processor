from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Receipt

receipts_data = {}

class ProcessReceiptsView(APIView):
    def post(self, request):
        data = request.data
        try:
            receipt = Receipt(
                retailer=data['retailer'],
                purchase_date=data['purchaseDate'],
                purchase_time=data['purchaseTime'],
                items=data['items'],
                total=data['total']
            )
            receipts_data[receipt.id] = receipt
            return Response({"id": receipt.id}, status=status.HTTP_200_OK)
        except KeyError:
            return Response(
                {"error": "Invalid receipt format. Please verify input."},
                status=status.HTTP_400_BAD_REQUEST,
            )

class GetPointsView(APIView):
    def get(self, request, id):
        receipt = receipts_data.get(id)
        if not receipt:
            return Response({"error": "No receipt found for that ID."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"points": receipt.points}, status=status.HTTP_200_OK)
