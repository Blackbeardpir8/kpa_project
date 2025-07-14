from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from forms.models import BogieForm, WheelForm
from forms.serializers import BogieFormSerializer, WheelFormSerializer
from django.db.models import Q


class BogieFormView(APIView):
    def post(self, request):
        serializer = BogieFormSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            return Response({
                "success": True,
                "message": "Bogie checksheet submitted successfully.",
                "data": {
                    "formNumber": form.formNumber,
                    "inspectionBy": form.inspection_by, 
                    "inspectionDate": str(form.inspection_date) ,
                    "status": "Saved"
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "message": "Invalid data submitted.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class WheelFormView(APIView):
    def post(self, request):
        serializer = WheelFormSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": form.formNumber,
                    "submittedBy": form.submittedBy,
                    "submittedDate": str(form.submittedDate),
                    "status": "Saved"
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": "Invalid data submitted.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        formNumber = request.GET.get('formNumber')
        submittedBy = request.GET.get('submittedBy')
        submittedDate = request.GET.get('submittedDate')

        filters = Q()
        if formNumber:
            filters &= Q(formNumber=formNumber)
        if submittedBy:
            filters &= Q(submittedBy=submittedBy)
        if submittedDate:
            filters &= Q(submittedDate=submittedDate)

        forms = WheelForm.objects.filter(filters)
        data = []

        for form in forms:
            fields = getattr(form, 'fields', None)
            data.append({
                "formNumber": form.formNumber,
                "submittedBy": form.submittedBy,
                "submittedDate": str(form.submittedDate),
                "fields": {
                    "treadDiameterNew": getattr(fields, 'treadDiameterNew', None),
                    "lastShopIssueSize": getattr(fields, 'lastShopIssueSize', None),
                    "condemningDia": getattr(fields, 'condemningDia', None),
                    "wheelGauge": getattr(fields, 'wheelGauge', None)
                } if fields else {}
            })

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": data
        }, status=status.HTTP_200_OK)
