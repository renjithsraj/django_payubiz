""" The django version is 1.5.1 the imported function mauy varing depands on the versions"""
import json, datetime, hashlib
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from payu_config import (merchant_key, mode,su_url, fu_url, cu_url)
from payubiz import PayuBizTransactions as PayBz


def make_transaction(data):
    payu_biz = PayBz()
    action = "makepayment"
    validate_data = payu_biz.validate_request_params(action, data)
    transaction_dict = data.copy()
    phone_no = data.pop('phone')
    data['key'] = merchant_key
    hash_code = payu_biz.generate_payment_hash(data)
    payment_url = payu_biz.generate_payment_url()
    firstname = transaction_dict['firstname']
    surl,furl,curl = su_url, fu_url, cu_url


    print "FSDfsdfsdfsdfsdfsdfsdf"
    return HttpResponse(
         """
            <html>
                    <head><title>Redirecting...</title></head>
                    <body>


                    <form action='%s' method='post' name="payu">

                            <input type="hidden" name="firstname" value="%s" />
                            <input type="hidden" name="surl" value="%s" />
                            <input type="hidden" name="phone" value="%s" />
                            <input type="hidden" name="key" value="%s" />
                            <input type="hidden" name="hash" value =
                            "%s" />
                            <input type="hidden" name="curl" value="%s" />
                            <input type="hidden" name="furl" value="%s" />
                            <input type="hidden" name="txnid" value="%s" />
                            <input type="hidden" name="productinfo" value="%s" />
                            <input type="hidden" name="amount" value="%s" />
                            <input type="hidden" name="email" value="%s" />
                            <input type="hidden" value="submit">
                    </form>
                    </body>
                    <script language='javascript'>


                    window.onload = function(){
                     document.forms['payu'].submit()

                    }

                    </script>
            </html>

                    """ % (
                            payment_url,
                            firstname,
                            surl,
                            transaction_dict['phone'],
                            merchant_key,
                            hash_code,
                            curl,
                            furl,
                            transaction_dict['txnid'],
                            transaction_dict['productinfo'],
                            transaction_dict['amount'],
                            transaction_dict['email'],
                                 )
        )


@csrf_exempt
def payu_success(request):
    """ we are in the payu success mode"""
    return HttpResponse(json.dumps(request.POST),mimetype='application/json')
@csrf_exempt
def payu_failure(request):
    """ We are in payu failure mode"""
    return HttpResponse(json.dumps(request.POST),mimetype='application/json')
@csrf_exempt
def payu_cancel(request):
    """ We are in the Payu cancel mode"""
    return HttpResponse(json.dumps(request.POST),mimetype='application/json')
