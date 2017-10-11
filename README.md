# Payubiz :credit_card:

[![PyPI version](https://badge.fury.io/py/payu_biz.svg)](https://badge.fury.io/py/payu_biz) [![Build Status](https://travis-ci.org/renjithsraj/django_payubiz.svg?branch=master)](https://travis-ci.org/renjithsraj/django_payubiz) [![Code Health](https://landscape.io/github/renjithsraj/django_payubiz/master/landscape.svg?style=plastic)](https://landscape.io/github/renjithsraj/django_payubiz/master)

Python Package for PayuBiz Payment Gateway for Django Based Applications.

### Developer ![#f03c15]

These packages in the developement stage, its cool package for the payu payment gateway.

demo application deployed in [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://djangopayubizdemo.herokuapp.com/)
[home page only redirect to payment gateway, the result you can see in JSON format]
sample credentials for payment

website : [Payment Gateway Payubiz](https://djangopackages.blogspot.in/2017/03/payu-payment-gateway-integration-in.html)
    
    Name on Card: Any name
    Card Number: 5100018609086541
    CVV: 123
    Expiry Date: 01/2020

## Lets Begins :seedling:

django_payubiz is wrapper for payubiz payment gateway for django based web application. I can see the internet many of the developers are asking about following doubts.
+ Getting error while creatig hash value
+ Redirection is not happening
+ transaction failure

be cool now you don't worry about the these things i have the solution for this.

## Installation

* Install django_payubiz from PYPI repository or clone the package from the [django_payubiz repo](https://github.com/renjithsraj/django_payubiz.git)

    `pip install payu_biz`

### Settings

    Step 1 :
        * Include the `payu_biz` package in to the INSTALLED_APPS
        
            `INSTALLED_APPS = (
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.sites',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'home',
                    'payu_biz' ## Package
                )``
        
    Step 2:
    
        Add following parameters in the project settings.py(project/settings.py)

        Note : For the Testing purpose you don't need to include ['PAYMENT_MODE',
        'MERCHANT_KEY','MERCHANT_SALT'] in the projects.

        * PAYMENT_MODE
          * The value should be one of the items from the list ['production', 'test']
              `PAYMENT_MODE = "production" ` `default will be "test"`

        * MERCHANT_KEY
           * merchant_key from payu. default value will be included builtin in the package.
               `MERCHANT_KEY = "xxxxxxxx" `

        * MERCHANT_SALT
           * merchant_salt from payu. default value will be included builtin in the package.
              `MERCHANT_SALT = "xxxxxxxx" `

        * SUCCESS_URL
          * Where to redirect while transaction is succeeded.
              `SUCCESS_URL = "www.example.com/success/" `

        * FAILURE_URL
          * Where to redirect while transaction got failure.
              `FAILURE_URL = "www.example.com/failure/" `

        * CANCEL_URL
          * Where to redirect while transaction got canceld
              `CANCEL_URL = "www.example.com/cancel/" `
      
 ### Integration.
 
 django_payubiz integration in your project. Add following codes in your views.py(project/home/views.py)
 
        `from payu_biz.views import make_transaction
        `def home(request):
            """ DO your stuffs here and create a dictionary (key,value pair) """
             cleaned_data = {
                    'txnid': "aaaaassss", 'amount': 450000, 'productinfo': "sample_produ",
                    'firstname':"renjith", 'email': "renjithsraj@live.com", 'udf1': '', 
                    'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '', 'udf7': '', 
                    'udf8': '', 'udf9': '', 'udf10': '','phone':"9746272610"
                    }
             """ Payment gate calling with provided data dict """       
             return make_transaction(cleaned_data)
             
  #### Note
  1. Please store the response data into database.[the package will update soon]
  2.The following keys must be there in your `cleaned_data` dict
  
        * txnid - Unique
        * amount
        * productinfo - small description
        * firstname - user firstname
        * email - user email id (Payu will send the transaction details with this mail)
        * phone - 
        * udf1 - udf10 - Chumma(Just simply if you want to add any details you can add)
        
## Methods :pizza:

* Verify Payment
* Check Payment
* Capture Transaction
* Refund Transaction
* Cancel Transaction
* Cancel Refund Transaction
* Check Action Status
    
#### Verify Payment

    `from payu_biz.views import (make_transaction, verify_payment)
     def home(request):
        """ Do Stuffs """
        txnid = "payu_biz82532"
        vp = verify_payment(txnid)
        print vp`
    
#### CheckPayment

    `from payu_biz.views import (make_transaction, check_payment)
     def home(request):
        """ Do Stuffs """
        mihpayid = "403993715515865279" ## captured from make_transaction response 
        cp = check_payment(mihpayid)
        print cp `
    
#### Capture Transaction

    `from payu_biz.views.import (make_transaction, capture_transaction)
     def home(request):
        """ DO stuffs """
        mihpayid = "403993715515865279" ## captured from make_transaction response 
        ct = capture_transaction(mihpayid)
        print ct`
    
#### Cancel Transaction

    `from payu_biz.views.import (make_transaction, cancel_transaction)
     def home(request):
        """ DO stuffs """
        mihpayid = "403993715515865279" ## captured from make_transaction response 
        amount = "450000.00"
        ct = cancel_transaction(mihpayid,amount)
        print ct`
    
#### Refund Transaction

    `from payu_biz.views.import (make_transaction, refund_transaction)
     def home(request):
        """ DO stuffs """
        mihpayid = "403993715515865279" ## captured from make_transaction response 
        amount = "450000.00"
        ref_t = refund_transaction(mihpayid, amount)
        print ref_t `

#### Cancel Refund Transaction

    `from payu_biz.views.import (make_transaction, cancel_refund_transaction)
     def home(request):
        """ DO Stuffs """
        mihpayid = "403993715515865279"
        amount = "450000.00"
        ct = cancel_refund_transaction(mihpayid, amount)
        print ct `
    
#### Check Action Status

    `from payu_biz.views.import (maketransaction, cancel_refund_transaction, check_action_status)
     This API is used to check the status of refund/cancel requests
     def home(request):
        request_id = "127403301"  # Pass the Cancel Refund Request ID
        c_status = check_action_status(request_id)
        print c_status`  
        
#####  Future Enhacements

    * Models Integration
    * Common python package
    * Integrate All the payu webservices.

