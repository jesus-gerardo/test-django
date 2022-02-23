from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CategoriesSerializer
from rest_framework.response import Response
from .models import Categories

# Create your views here.
class CategoriesView(APIView):
    permission_classes = [IsAuthenticated]

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

    def put(request):
        pass

    def delete(self, request):
        pass