import datetime
class Purchase_Json(object):

    def get_purchase(self):
        purchase = dict(credentials={}, transaction={}, merchant={}, terminal={}, card={}, address={})

        purchase['credentials'] = {
            'AccountID' : 's.MID5.PAY.WS.NP',
            'Password' : 'Tu2u2AHU'
        }

        purchase['merchant'] = {
            'MerchantID' : '4445012916098',
            #'MerchantName' : 'ABCDEF',
            'NetworkRouting' : '2J',
            'CashierNumber' : '12345678',
            'LaneNumber' : '123',
            'DivisionNumber' : '000',
            'ChainCode' : '70110',
            'StoreNumber' : '00000001',
        }

        purchase['transaction'] = {
            'TransactionID' : '123456',
            'PaymentType' : 'single',
            'ReferenceNumber' : '111111111',
            'DraftLocatorId' : '12345678901',
            'ClerkNumber' : '1234',
            'MarketCode' : 'present',
            'TransactionTimestamp' : datetime.datetime.now().isoformat(),
            'TokenRequested' : 'true',
            'SystemTraceID' : '654321',
            'TransactionAmount' : '10.00'
        }

        purchase['terminal'] = {
            'TerminalID' : '1',
            'IPv4Address' : '192.0.2.235',
            'TerminalEnvironmentalCode' : 'manual',
            'PinEntry' : 'unknown',
            'BalanceInquiry' : 'true',
            'HostAdjustment' : 'true',
            'DeviceType' : 'Software',
            'CardInputCode' : 'ManualKeyed',
            'EntryMode': 'manual'
        }

        purchase['card'] = {
            'CardType' : 'visa',
            'CardNumber' : '4388110000000001',
            'ExpirationMonth' : '12',
            'ExpirationYear' : '2014',
            "CVV": "382"
        }

        purchase['address'] = {
            'BillingAddressLine1': '100',
            'BillingCity': 'Cincinnati',
            'BillingState': 'OH',
            'BillingZipcode': '33606',
            'CountryCode': 'US'
        }
        return purchase