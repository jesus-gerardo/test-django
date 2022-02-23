from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductsSerializer
from rest_framework.response import Response
from .models import Products

# Create your views here.
class ProductsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products=Products.objects.all()
        serialize=ProductsSerializer(products, many=True)
        return Response(serialize.data)

    def post(self, request):
        try:
            product=ProductsSerializer(data=request.data)
            if not product.is_valid():
                return Response({
                    'response': False,
                    'msg': product.errors
                })
            product.save()
            return Response({'response':True})
        except Exception as error:
            return Response({
                'response': False,
                'msg': error
            })