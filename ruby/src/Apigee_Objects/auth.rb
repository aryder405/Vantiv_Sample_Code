require 'date'
require 'json'
require 'time'


class Auth
  @@request

  def initialize
    credentials = {
        :AccountID => 's.MID5.PAY.WS.NP',
        :Password => 'Tu2u2AHU'
    }

    merchant = {
        :NetworkRouting => '2J',
        :CashierNumber => '12345678',
        :LaneNumber => '123',
        :DivisionNumber => '000',
        :ChainCode => '70110',
        :StoreNumber => '00000001',
        :MerchantID => '4445012916098'
    }

    terminal = {
        :TerminalID => '1',
        :Ipv4Address => '192.0.2.235',
        :TerminalEnvironmentalCode => 'electronic_cash_register',
        :PinEntry => 'none',
        :BalanceInquiry => 'false',
        :HostAdjustment => 'false',
        :DeviceType => 'Terminal',
        :CardInputCode => 'ManualKeyed',

    }

    transaction = {
        :TransactionID => '123456',
        :PaymentType => 'single',
        :ReferenceNumber => '100001',
        :DraftLocatorID => '100000001',
        :ClerkNumber => '1234',
        :MarketCode => 'present',
        :TransactionTimestamp =>  Time.now.utc.iso8601,
        :SystemTraceID => '100002',
        :TokenRequested => 'false',
        :TransactionAmount => '10.00'
    }

    address = {
        :BillingAddress1 => '1234 main street',
        :BillingCity => 'Cincinnati',
        :BillingState => 'OH',
        :BillingZipcode => '45209',
        :CountryCode => 'US'
    }

    card = {
        :CardType => 'visa',
        :PartialApprovalCode => 'not_supported',
        :CardNumber => '4445222299990007',
        :ExpirationMonth => '12',
        :ExpirationYear =>'2017',
        :CVV => '382',

    }

    @@request = {
        'credentials' => credentials,
        'merchant' => merchant,
        'terminal' => terminal,
        'transaction' => transaction,
        'address' => address,
        'card' => card
    }
  end

  def getPayload
    return @@request

  end


end