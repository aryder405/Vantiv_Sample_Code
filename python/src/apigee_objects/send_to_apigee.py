import authorize_json
import capture_json
import purchase_json
import json
import requests
import logging

class Send_Request(object):

    credit_url = 'https://apis.cert.vantiv.com/v1/credit/'
    api_key = 'C2sBuOvzCmp69wDAg7PnV4cKqCFQ3hNR'
    licenseid = '572d606c967f412cb8d840e38fb48010$$#$$MphfoMed030iGRXOd6pBhDzGQnzEMmz7$$#$$2015-11-26$$#$$dev_key$$#$$SHA512withRSA$$#$$RSA$$#$$1$$#$$52BC72E18D55CC77AE2DE3C27C0AFE6C0FCE3E3E6C1638EE824E5DB7775ADBBB616D82127D46DF9272D6A39ABC6BA8AD6797000A52F769C982B5360C06CED1FFA8FABA0DEA70E1CD77DC4DAF912E81319538857CAABE16DB6C412AF478BC059B29232337AE09020069B96E741982FB5E6BC053E98FE7C33789288CAA6A9883C0D2380DD1812FCF2681A8B31545B97DD0736EB3ECBD9329F144CDB93C35780559DB6219604ADB3F5A8DC57E06CFD715FFCECD3CB65DE7BFDA065D4DB3BDC84B7E0FD66116C71AC41E0B875BA18C742A8ECE9E690AC37457DD43845F5C64EA00BF7B585A6FCF75A0F398026CD79C74C3C946C11BAFD1404997917C5592B91E8415'
    headers = {'Content-type': 'application/json', 'licenseid': licenseid,'Apikey': api_key}

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('suds.client').setLevel(logging.DEBUG)


    def send_auth(self):
        url = self.credit_url + 'authorization?sp=1'

        auth = authorize_json.Authorize_Json().get_auth()

        data = json.dumps(auth)

        response = requests.post(url, data=data, headers=self.headers)

        logging.info("Request: %s %s %s", response.request.method, response.request.url, response.request.body)
        logging.info("Response: %s", response.text)

        d = json.loads(response.text)
        return d["AuthorizeResponse"]["AuthorizationCode"]

    def send_capture(self, auth_code):
        url = self.credit_url + 'authorizationcompletion?sp=1'

        capture = capture_json.Capture_Json().get_capture(auth_code)

        data = json.dumps(capture)

        response = requests.post(url, data=data, headers=self.headers)

        logging.info("Request: %s %s %s", response.request.method, response.request.url, response.request.body)
        logging.info("Response: %s", response.text)

    def send_purchase(self):
        url = self.credit_url + 'sale?sp=1'

        purchase = purchase_json.Purchase_Json().get_purchase()

        data = json.dumps(purchase)

        response = requests.post(url, data=data, headers=self.headers)

        logging.info("Request: %s %s %s", response.request.method, response.request.url, response.request.body)
        logging.info("Response: %s", response.text)


