
from django.conf import settings

required_params = { 'makepayment':('txnid', 'amount', 'productinfo', 'firstname', 'email', 'phone'),
                    'makepayment_data_hash':('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email'),
                    'webservice_key':('key', 'command', 'var1'),

}

urls = {    "production":"https://secure.payu.in/_payment",
            "test":"https://test.payu.in/_payment",
            "success_url":"http://127.0.0.1:8000/payubiz-success/",
            "cancel_url":"http://127.0.0.1:8000/payubiz-cancel/",
            "failure_url":"http://127.0.0.1:8000/payubiz-failure/"
       }

payment_mode = ['test','production']

mode = getattr(settings,'PAYMENT_MODE',payment_mode[0])
site_url = ""
su_url = getattr(settings,'SUCCESS_URL',urls['success_url'])
fu_url = getattr(settings,'FAILURE_URL',urls['failure_url'])
cu_url = getattr(settings,'CANCEL_URL',urls['cancel_url'])

merchant_key = getattr(settings,'MERCHANT_KEY','gtKFFx')
merchant_salt = getattr(settings,'MERCHANT_SALT','eCwWELxi')

