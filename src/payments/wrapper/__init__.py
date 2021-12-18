import json, requests, hashlib, hmac
from collections import OrderedDict
from urllib.parse import urlencode

class PaymentAPI:
    def __init__(self, transid, privkey, pubkey):
        self.api = 'https://www.coinpayments.net/api.php'
        self.private_key = privkey
        self.public_key = pubkey
        self.transaction = transid

    def getkey(self, params):
        privateKey = bytearray(self.private_key, 'utf-8')
        
        return hmac.new(
            privateKey, 
            bytearray(str(params), 'utf-8'), 
            hashlib.sha512
        ).hexdigest()

    def getParams(self, command):
        base_params = [
            ('version', 1),
            ('key', self.public_key),
            ('cmd', command),
            ('format', 'json'),
            ('txid', self.transaction)
        ]

        return urlencode(
            OrderedDict(base_params)
        )

    def createRequest(self):
        data = self.getParams('get_tx_info')

        headers = {'HMAC': self.getkey(data), 'Content-Type': 'application/x-www-form-urlencoded'}

        resp =  requests.post(
            url = self.api,
            data = data,
            headers = headers
        ).json()

        try:
            status = resp['result']
            if status['status'] == 100: return status
            else: return False
        except:
            return False
