from django.http import HttpResponse
from payu_config import (merchant_key, su_url, fu_url, cu_url)
from payubiz import PayuBizTransactions as PayBz
from payubiz import PayuPaymentTrasactionService as PayWTS

def make_transaction(data):
    payu_biz = PayBz()
    action = "makepayment"
    payu_biz.validate_request_params(action, data)
    transaction_dict = data.copy()
    data.pop('phone')
    data['key'] = merchant_key
    hash_code = payu_biz.generate_payment_hash(data)
    payment_url = payu_biz.generate_payment_url()
    firstname = transaction_dict['firstname']
    surl,furl,curl = su_url, fu_url, cu_url
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


def verify_payment(txnid):
    v_p = PayWTS()
    vp_p = v_p.verify_payment(txnid)
    return vp_p

def check_payment(mihpayid):
    c_p = PayWTS()
    cp_p = c_p.check_payment(mihpayid)
    return cp_p

def capture_transaction(mihpayid):
    c_t = PayWTS()
    ct_t = c_t.capture_transaction(mihpayid)
    return ct_t

def cancel_transaction(mihpayid, amount):
    c_t = PayWTS()
    ct_t = c_t.cancel_transaction(mihpayid, amount)
    return ct_t


def refund_transaction(mihpayid, amount):
    r_t = PayWTS()
    rt_t = r_t.refund_transaction(mihpayid, amount)
    return rt_t

def cancel_refund_transaction(mihpayid, amount):
    cr_t = PayWTS()
    cr_rt = cr_t.cancel_refund_transaction(mihpayid, amount)
    return cr_rt

def check_action_status(request_id):
    ca_s = PayWTS()
    ca_sd = ca_s.check_action_status(request_id)
    return ca_sd




