Django Payubiz
===================

Python Package for PayuBiz Payment Gateway for Django Based Applications.

Developer ![#f03c15]
=====================

These packages in the developement stage, its cool package for the payu payment gateway.

payu_biz is wrapper for payubiz payment gateway for django based web application. I can see the internet many of the developers are asking about following doubts. 

  1. Getting error while creatig hash value
  2. Redirection is not happening
  3. transaction failure


Installation
===================

Install django_payubiz from PYPI repository or clone the package from the 
[django_payubiz repo](https://github.com/renjithsraj/django_payubiz.git)

====================
pip install payu_biz
====================

Settings
==========
  Step 1 :
  
    Include the `payu_biz` package in to the INSTALLED_APPS
    
    INSTALLED_APPS = (
                      'django.contrib.auth',
                      'django.contrib.contenttypes',
                      'django.contrib.sessions',
                      'django.contrib.sites',
                      'django.contrib.messages',
                      'django.contrib.staticfiles',
                      'home',
                      'payu_biz' ## Package
                      )

    Include payu_biz urls in your project(project/urls.py)
           
      urlpatterns = patterns('',
              # Examples:
              url(r'^$', 'home.views.home', name='home'),
              url(r'^', include('payu_biz.urls')),
                      )
          
    Step 2:

      Add following parameters in the project settings.py(project/settings.py)
      Note : For the Testing purpose you don't need to include these parameters in the projects.

      PAYMENT_MODE
      ============
      The value should be one of the items from the list ['production', 'test']
      PAYMENT_MODE = "production" ` `default will be "test"`
      ==========================================================================

      MERCHANT_KEY
      ============
      merchant_key from payu. default value will be included builtin in the package.
      MERCHANT_KEY = "xxxxxxxx"
      ===========================================================================

      MERCHANT_SALT
      =============
      merchant_salt from payu. default value will be included builtin in the package.
      MERCHANT_SALT = "xxxxxxxx"
      ============================================================================

      SUCCESS_URL
      ============
      Where to redirect while transaction is succeeded.
      SUCCESS_URL = "www.example.com/success/" ` `default will be "http://127.0.0.1:8000/payubiz-success/"
      =============================================================================

      FAILURE_URL
      =============
      Where to redirect while transaction got failure.
      FAILURE_URL = "www.example.com/failure/" ` `default will be "http://127.0.0.1:8000/payubiz-failure/"
      ==============================================================================

      CANCEL_URL
      =============
      Where to redirect while transaction got canceld
      CANCEL_URL = "www.example.com/cancel/" ` `default will be "http://127.0.0.1:8000/payubiz-cancel/"
      ===============================================================================
      
Integration.
============
 
  payu_biz integration in your project.Add following snippts in your views.py(project/home/views.py)
 
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
             
Note
=====

  The following keys must be there in your `cleaned_data` dict
  
    * txnid - Unique
    * amount
    * productinfo - small description
    * firstname - user firstname
    * email - user email id (Payu will send the transaction details with this mail)
    * phone - 
    * udf1 - udf10 - Chumma(Just simply if you want to add any details you can add)
