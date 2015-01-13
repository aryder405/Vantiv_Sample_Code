class Terminal(object):
        TerminalID = ''
        IPv4Address = ''
        IPv6Address = ''
        TerminalEnvironmentalCode = ''
        CardInputCode = ''
        PinEntry = ''
        BalanceInquiry = ''
        HostAdjustment = ''
        DeviceType = ''

        def get_terminal(self):
            return {
                'TerminalID': self.TerminalID,
                'IPv4Address':self.IPv4Address,
                'IPv6Address': self.IPv6Address,
                'TerminalEnvironmentalCode':self.TerminalEnvironmentalCode,
                'CardInputCode':self.CardInputCode,
                'PinEntry': self.PinEntry,
                'BalanceInquiry': self.BalanceInquiry,
                'HostAdjustment': self.HostAdjustment,
                'DeviceType': self.DeviceType,
            }