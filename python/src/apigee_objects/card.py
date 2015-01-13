class Card(object):
        CardType = ''
        CardNumber = ''
        ExpirationMonth = ''
        ExpirationYear = ''
        Track1Data = ''
        Track2Data = ''
        EncryptedTrack1Data = ''
        EncryptedTrack2Data = ''
        EncryptedFormat = ''
        CardDataKeySerialNumber = ''
        TokenID = ''
        TokenValue = ''
        CVV = ''
        CardholderName = ''



        def get_card(self):
            return {
                'CardType': self.CardType,
                'CardNumber':self.CardNumber,
                'ExpirationMonth': self.ExpirationMonth,
                'ExpirationYear':self.ExpirationYear,
                'Track1Data':self.Track1Data,
                'Track2Data': self.Track2Data,
                'EncryptedTrack1Data': self.EncryptedTrack1Data,
                'EncryptedTrack2Data': self.EncryptedTrack2Data,
                'EncryptedFormat': self.EncryptedFormat,
                'CardDataKeySerialNumber': self.CardDataKeySerialNumber,
                'TokenID': self.TokenID,
                'TokenValue': self.TokenValue,
                'CVV': self.CVV,
                'CardholderName': self.CardholderName,



            }