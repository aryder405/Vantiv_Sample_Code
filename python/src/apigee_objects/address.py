class Address(object):
    BillingAddressLine1 = '100'
    BillingCity = 'Cincinnati'
    BillingState = 'OH'
    BillingZipcode = '33606'
    CountryCode = 'US'

    def get_address(self):
        return {
            'BillingAddressLine1': self.BillingAddressLine1,
            'BillingCity': self.BillingCity,
            'BillingState': self.BillingState,
            'BillingZipCode':self.BillingZipCode,
            'CountryCode':self.CountryCode
        }