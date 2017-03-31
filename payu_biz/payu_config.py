
from django.conf import settings

required_params = { 'makepayment':('txnid', 'amount', 'productinfo', 'firstname', 'email', 'phone'),
                    'makepayment_data_hash':('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email'),
                    'webservice_key':('key', 'command', 'var1'),

}

urls = {    "production":"https://secure.payu.in/_payment",
            "test":"https://test.payu.in/_payment",
       }

payment_mode = ['test','production']

mode = getattr(settings,'PAYMENT_MODE',payment_mode[0])
site_url = ""
su_url = getattr(settings,'SUCCESS_URL',None)
fu_url = getattr(settings,'FAILURE_URL',None)
cu_url = getattr(settings,'CANCEL_URL',None)

merchant_key = getattr(settings,'MERCHANT_KEY','gtKFFx')
merchant_salt = getattr(settings,'MERCHANT_SALT','eCwWELxi')

