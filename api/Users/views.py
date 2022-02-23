from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import Users

# Create your views here.
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    # @api_view(['POST'])
    def get(self, request):
        queryset = Users.objects.all()
        serializer  = UserSerializer(queryset, many=True)
        return  Response(serializer.data)