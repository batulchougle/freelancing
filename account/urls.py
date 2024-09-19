from django.urls import path
from .views import RegisterInstituteView, VerifyUserEmail

urlpatterns = [
    
    path('institue-signup/', RegisterInstituteView.as_view(), name='institute-signup'),
    path('verify-email/',VerifyUserEmail.as_view(),name='verify'),

]