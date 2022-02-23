from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Users
from .serializers import UserSerializer

# Create your views here.
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    # @api_view(['POST'])
    def get(self, request):
        queryset = Users.objects.all()
        serializer  = UserSerializer()
        return  Response(serializer.data)