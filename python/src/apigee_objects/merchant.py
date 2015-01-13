class Merchant(object):
        MerchantID = ''
        MerchantName = ''
        NetworkRouting = ''
        CashierNumber = ''
        LaneNumber = ''
        DivisionNumber = ''
        ChainCode = ''
        StoreNumber = ''

        def get_merchant(self):

            return_values = {}
            if not self.MerchantID: return_values['MerchantID' : self.MerchantID]
            if not self.MerchantID: return_values['MerchantName' : self.MerchantName]
            if not self.MerchantID: return_values['NetworkRouting' : self.NetworkRouting]
            if not self.MerchantID: return_values['CashierNumber' : self.CashierNumber]
            if not self.MerchantID: return_values['DivisionNumber' : self.DivisionNumber]
            if not self.MerchantID: return_values['LaneNumber' : self.LaneNumber]
            if not self.MerchantID: return_values['ChainCode' : self.ChainCode]
            if not self.MerchantID: return_values['StoreNumber' : self.StoreNumber]

            return return_values



