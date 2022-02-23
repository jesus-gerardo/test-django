from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework.response import Response

# Create your views here.
class CategoriesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories=Categories.objects.all()
        serializer=CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            valid = CategoriesSerializer(data=request.data)
            if not valid.is_valid():
                return Response({
                    'response':False, 
                    'msg': valid.errors
                })
            valid.save()

            return Response({'response':True})
        except Exception as error:
            return Response({
                'response':True,
                'msg': error
            })

    def put(request):
        pass

    def delete(self, request):
        pass