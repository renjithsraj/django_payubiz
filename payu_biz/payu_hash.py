from hashlib import sha512
from payu_config import merchant_salt
from payu_config import (required_params)

KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10')


def generate_hash(data):
    hash_value = sha512('')
    for key in KEYS:
        hash_value.update("%s%s" % (str(data.get(key, '')), '|'))
    hash_value.update(merchant_salt)
    return hash_value.hexdigest().lower()

def get_webservice_hash(data):
    # Generate hash sequence using the string sha512(key|command|var1|salt)
    hash_value = sha512(''.encode("utf-8"))
    for key in required_params['webservice_key']:
        hash_value.update(("%s%s" % (str(data.get(key, '')), '|')).encode("utf-8"))
    hash_value.update((merchant_salt.encode("utf-8")))
    return hash_value.hexdigest().lower()
