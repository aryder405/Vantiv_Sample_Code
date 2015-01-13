class Credentials(object):
        AccountId = 's.MID5.PAY.WS.NP'
        Password = 'Tu2u2AHU'

        def get_credentials(self):
            return {
                'AccountId': self.AccountId,
                'Password': self.Password
            }