# Django Payubiz

Python Package for PayuBiz Payment Gateway for Django Based Applications.

## Lets Begins :seedling:

django_payubiz is wrapper for payubiz payment gateway for django based web application. I can see the internet many of the developers are asking about following doubts.
+ Getting error while creatig hash value
+ Redirection is not happening
+ transaction failure

be cool now you don't worry about the these things i have the solution for this.

## Installation

* Install django_payubiz from PYPI repository or clone the package from the [django_payubiz repo](https://github.com/renjithsraj/django_payubiz.git)

    `pip install django_payubiz`

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
                )`
                
        * Include payu_biz urls in your project(project/urls.py)
         
              `urlpatterns = patterns('',
                     # Examples:
                    url(r'^$', 'home.views.home', name='home'),
                    url(r'^', include('payu_biz.urls')),
                    ) `
        
    Step 2:
    
        Add following parameters in the project settings.py(project/settings.py)

        Note : For the Testing purpose you don't need to include these parameters in the projects.

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
              `SUCCESS_URL = "www.example.com/success/" ` `default will be "http://127.0.0.1:8000/payubiz-success/"`

        * FAILURE_URL
          * Where to redirect while transaction got failure.
              `FAILURE_URL = "www.example.com/failure/" ` `default will be "http://127.0.0.1:8000/payubiz-failure/"`

        * CANCEL_URL
          * Where to redirect while transaction got canceld
              `CANCEL_URL = "www.example.com/cancel/" ` `default will be "http://127.0.0.1:8000/payubiz-cancel/"`
      
 
