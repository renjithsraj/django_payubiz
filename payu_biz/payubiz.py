from payu_hash import generate_hash
from payu_config import (required_params, mode, urls)

class PayuBizTransactions(object):

    def __init__(self):
        self.test = "test"

    @staticmethod
    def validate_request_params(action,data):
        print action
        print required_params[action]
        action_required_params = required_params[action]
        for each_param in action_required_params:
            if not data.has_key(each_param) or data.get(each_param,None) in ['',None]:
                raise Exception('%s is mandatory' % (each_param))

    @classmethod
    def generate_payment_hash(cls,data):
        action = "makepayment_data_hash"
        validate_hash_make_data = cls.validate_request_params(action, data)
        hash_value = generate_hash(data)
        print hash_value
        return hash_value
    @staticmethod
    def generate_payment_url():
        return urls[mode]


