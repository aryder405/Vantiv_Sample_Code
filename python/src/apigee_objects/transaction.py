class Transaction(object):
        TransactionID = None
        TransactionAmount = None
        MarketCode = None
        TransactionTimestamp = None
        ClerkNumber = None
        CancelType = None
        PaymentType = None
        ReferenceNumber = None
        DraftLocatorId = None
        AuthorizationCode = None
        OriginalAuthorizedAmount = None
        CaptureAmount = None
        CashBackAmount = None
        OriginalTransactionTimestamp = None
        OriginalSystemTraceId = None
        OriginalSequenceNumber = None
        OriginalAuthCode = None
        NetworkResponseCode = None
        ReversalReason = None
        ReplacementAmount = None
        OriginalReferenceNumber = None
        TipAmount = None
        ConvenienceFee = None
        TaxExempt = None
        Taxable = None
        TaxAmount = None
        PurchaseOrder = None
        TokenRequested = None
        SystemTraceID = None


        def get_transaction(self):

            return_values = {}
            if not self.TransactionID:
                return_values['TransactionID': self.TransactionID]
                print 'true'
            if not self.TransactionAmount:
                return_values['TransactionAmount' : self.TransactionAmount]
            if not self.MarketCode:
                return_values['MarketCode' : self.MarketCode]
            if not self.TransactionTimestamp:
                return_values['TransactionTimestamp' : self.TransactionTimestamp]
            if not self.ClerkNumber:
                return_values['ClerkNumber' : self.ClerkNumber]
            if not self.CancelType:
                return_values['CancelType' : self.CancelType]
                print 'true'
            if not self.PaymentType: return_values['PaymentType' : self.PaymentType]
            if not self.ReferenceNumber: return_values['ReferenceNumber' : self.ReferenceNumber]
            if not self.DraftLocatorId: return_values['DraftLocatorId' : self.DraftLocatorId]
            if not self.AuthorizationCode: return_values['AuthorizationCode' : self.AuthorizationCode]
            if not self.OriginalAuthorizedAmount: return_values['OriginalAuthorizedAmount' : self.OriginalAuthorizedAmount]
            if not self.CaptureAmount: return_values['CaptureAmount' : self.CaptureAmount]
            if not self.CashBackAmount: return_values['CashBackAmount' : self.CashBackAmount]
            if not self.OriginalTransactionTimestamp: return_values['OriginalTransactionTimestamp' : self.OriginalTransactionTimestamp]
            if not self.OriginalSystemTraceId: return_values['OriginalSystemTraceId' : self.OriginalSystemTraceId]
            if not self.OriginalSequenceNumber: return_values['OriginalSequenceNumber' : self.OriginalSequenceNumber]
            if not self.OriginalAuthCode: return_values['OriginalAuthCode' : self.OriginalAuthCode]
            if not self.NetworkResponseCode: return_values['NetworkResponseCode' : self.NetworkResponseCode]
            if not self.ReversalReason: return_values['ReversalReason' : self.ReversalReason]
            if not self.ReplacementAmount: return_values['ReplacementAmount' : self.ReplacementAmount]
            if not self.OriginalReferenceNumber: return_values['OriginalReferenceNumber' : self.OriginalReferenceNumber]
            if not self.TipAmount: return_values['TipAmount' : self.TipAmount]
            if not self.ConvenienceFee: return_values['ConvenienceFee' : self.ConvenienceFee]
            if not self.TaxExempt: return_values['TaxExempt' : self.TaxExempt]
            if not self.PurchaseOrder: return_values['PurchaseOrder' : self.PurchaseOrder]
            if not self.TokenRequested: return_values['TokenRequested' : self.TokenRequested]
            if not self.SystemTraceID: return_values['SystemTraceID' : self.SystemTraceID]

            return return_values