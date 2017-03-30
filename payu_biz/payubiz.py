from payu_hash import (generate_hash, get_webservice_hash)
from payu_config import (required_params, mode, urls, merchant_key)
import json
from django.utils.http import urlencode
from django.conf import settings
from hashlib import sha512
from uuid import uuid4
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


class PayuBizTransactions(object):
    def __init__(self):
        pass

    @staticmethod
    def validate_request_params(action,data):
        action_required_params = required_params[action]
        for each_param in action_required_params:
            if not data.has_key(each_param) or data.get(each_param,None) in ['',None]:
                raise Exception('%s is mandatory' % (each_param))

    @classmethod
    def generate_payment_hash(cls,data):
        action = "makepayment_data_hash"
        validate_hash_make_data = cls.validate_request_params(action, data)
        hash_value = generate_hash(data)
        return hash_value

    @staticmethod
    def generate_payment_url():
        return urls[mode]

    
def webservice_url():
    if mode.lower() == 'test':
        url = 'https://test.payu.in/merchant/postservice.php?form=2'
    elif mode.lower() == 'production':
        url = 'https://info.payu.in/merchant/postservice.php?form=2'
    else:
        raise Exception("The Service Urls is not found for the Payment mode")
    return url

class PayuPaymentTrasactionService(PayuBizTransactions):
    
    @staticmethod
    def payu_post(params):
        params = params
        params['key'] = merchant_key
        params['hash'] = get_webservice_hash(params)
        url = webservice_url()
        payload = urlencode(params)
        request = urllib2.Request(url)
        request.add_data(payload)
        response = (urllib2.urlopen(request))
        response = json.loads(response.read())
        return response

    def verify_payment(self,txnid):
        params = {}
        params['command'] = "verify_payment"
        params['var1'] = txnid
        verify_payment_data = self.payu_post(params)
        return verify_payment_data

    def check_payment(self,mihpayid):
        params = {}
        params['command'] = "check_payment"
        params['var1'] = mihpayid
        check_payment_data = self.payu_post(params)
        return check_payment_data

    def capture_transaction(self,mihpayid):
        params = {}
        params['command'] = "capture_transaction"
        params['var1'] = mihpayid
        params['var2'] = uuid4().hex
        capture_transaction_data = self.payu_post(params)
        return capture_transaction_data

    def cancel_transaction(self, mihpayid, amount):
        params = {}
        params['command'] = "cancel_transaction"
        params['var1'] = mihpayid      # Pass the Payu id (mihpayid) of the transaction to capture.
        params['var2'] = uuid4().hex   # token ID(unique token from merchant)
        params['var3'] = amount
        cancel_transaction_data = self.payu_post(params)
        return cancel_transaction_data
        
    def refund_transaction(self,mihpayid, amount):
        params = {}
        params['command'] = "refund_transaction"
        params['var1'] = mihpayid
        params['var2'] = uuid4().hex
        params['var3'] = amount
        refund_transaction_data = self.payu_post(params)
        return refund_transaction_data

    def cancel_refund_transaction(self,mihpayid, amount):
        params = {}
        params['command'] = "cancel_refund_transaction"
        params['var1'] = mihpayid
        params['var2'] = uuid4().hex
        params['var3'] = amount
        cancel_refund_transaction_data = self.payu_post(params)
        return cancel_refund_transaction_data

    # This API is used to check the status of refund/cancel requests
    def check_action_status(self,request_id):
        params = {}
        params['command'] = "check_action_status"
        params['var1'] = request_id    # Pass the Cancel Refund Request ID.
        check_action_status_data = self.payu_post(params)
        return check_action_status_data


   


