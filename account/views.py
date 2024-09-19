from django.shortcuts import render

# Create your views here.
from .serializers import InstituteRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .utility import send_code_to_user
from .models import OneTimePassword, Institute
# Create your views here.



class RegisterInstituteView(GenericAPIView):
    serializer_class=InstituteRegisterSerializer

    def post(self,request):
        institute_data=request.data
        serializer=self.serializer_class(data=institute_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            institute=serializer.data
            send_code_to_user(institute['email'])
            return Response({'data':institute, 'message':f"hi {institute['name']} thanks for sigining up a passcode has been sent to verify your email"},status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyUserEmail(GenericAPIView):
    def post(self,request):
        otpcode=request.data.get('otp')
        try:
            institute_code_obj=OneTimePassword.objects.get(code=otpcode)
            institute = institute_code_obj.user
            if not institute.is_verified:
                institute.is_verified=True
                institute.save()
                return Response({'message':'account email verified successfully'},status=status.HTTP_200_OK)
            return Response({'message':'code is invalid, user already verified'}, status=status.HTTP_204_NO_CONTENT)
          
        except OneTimePassword.DoesNotExist:
            return Response({'message':'invalid otp'},status=status.HTTP_404_NOT_FOUND)
            
    