from django.shortcuts import render

# Create your views here.

from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from accounts.serializers import AppUserSerializer
from rest_framework.views import APIView

class CustomAuthLogin(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            valid_data = VerifyJSONWebTokenSerializer().validate(response.data)
            user = valid_data['user']
            response.data['first_name'] = user.first_name
            response.data['user_id'] = user.id
            if user.is_admin:
                response.data['user_type'] = "seller"
            else:
                response.data['user_type'] = "buyer"

            return Response(
                            {'error': '', 'error_code': '', 'data': response.data}, status=200)
        except :
            return Response(
                            {'error': 'Incorrect email or password', 'error_code': '', 'data': ''}, status=400)



class AppUser(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_serializer = AppUserSerializer(context={'request': request}, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': user_serializer.initial_data}, status=200)
            else:
                return Response({'error': user_serializer.errors, 'error_code': 'HS002', 'data':''}, status=200)
        
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

