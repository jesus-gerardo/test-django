from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from .serializers import CategoriesSerializer
# from rest_framework.decorators import action
from rest_framework.response import Response
# from django.http import JsonResponse
from .models import Categories



# Create your views here.
class CategoriesView(APIView):
    # permission_classes = [IsAuthenticated]

    # @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated])
    def get(self, request):
        categories=Categories.objects.all()
        serializer=CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        try:
            category = CategoriesSerializer(data=request.data)
            if not category.is_valid():
                return Response({
                    'response':False, 
                    'msg': category.errors
                })
            category.save()

            return Response({'response':True})
        except Exception as error:
            return Response({
                'response':False,
                'msg': error
            })

    def put(self, request):
        try:
            # category = CategoriesSerializer(data=request.data)
            # if not category.is_valid():
            #     return Response({
            #         'response':False, 
            #         'msg': category.errors
            #     })
            # data = Categories.objects.get(data.get('id'))
            # category.save()
            return Response({'response':True})
        except Exception as error:
            return Response({
                'response':False,
                'msg': error
            })

    def delete(self, request):
        id = request.GET['id']
        categories=Categories.objects.get(id)
        serializer=CategoriesSerializer(categories)
        return Response(serializer.data)