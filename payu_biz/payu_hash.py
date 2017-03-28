from hashlib import sha512
from payu_config import merchant_salt

KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10')


def generate_hash(data):
    keys = ('key','txnid', 'amount', 'productinfo', 'firstname', 'email',
            'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
            'udf9',  'udf10')
    hash = sha512('')
    for key in KEYS:
        hash.update("%s%s" % (str(data.get(key, '')), '|'))
    hash.update(merchant_salt)
    return hash.hexdigest().lower()



def verify_hash(data, SALT):
    keys.reverse()
    hash = sha512(  merchant_salt)
    hash.update("%s%s" % ('|', str(data.get('status', ''))))
    for key in KEYS:
        hash.update("%s%s" % ('|', str(data.get(key, ''))))
    return (hash.hexdigest().lower() == data.get('hash'))