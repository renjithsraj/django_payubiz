from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from payu_biz.views import make_transaction
from django.http import JsonResponse # django version 1.10



def home(request):
        
    cleaned_data = {
                'txnid': "payudempo125", 'amount': 450000, 'productinfo': "sample_produ",
                'firstname':"renjith", 'email': "renjithsraj@live.com", 'udf1': '', 
                'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '', 'udf7': '', 
                'udf8': '', 'udf9': '', 'udf10': '','phone':"9746272610"
                }
    """ Payment gate calling with provided data dict """       
    return make_transaction(cleaned_data)


@csrf_exempt
def payu_success(request):
    return JsonResponse(request.POST)
@csrf_exempt
def payu_failure(request):
    return JsonResponse(request.POST)
@csrf_exempt
def payu_cancel(request):
    return JsonResponse(request.POST)
