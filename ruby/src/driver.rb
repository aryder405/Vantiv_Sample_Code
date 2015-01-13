require 'json'
require 'net/https'
require 'uri'

require_relative 'Apigee_Objects/auth'
require_relative 'Apigee_Objects/capture'
require_relative 'Apigee_Objects/purchase'
require_relative 'Apigee_Objects/cancel'

class Driver
  def initialize
    #LicenseID for the REST header
    @licenseid = '572d606c967f412cb8d840e38fb48010$$#$$MphfoMed030iGRXOd6pBhDzGQnzEMmz7$$#$$2015-11-26$$#$$dev_key$$#$$SHA512withRSA$$#$$RSA$$#$$1$$#$$52BC72E18D55CC77AE2DE3C27C0AFE6C0FCE3E3E6C1638EE824E5DB7775ADBBB616D82127D46DF9272D6A39ABC6BA8AD6797000A52F769C982B5360C06CED1FFA8FABA0DEA70E1CD77DC4DAF912E81319538857CAABE16DB6C412AF478BC059B29232337AE09020069B96E741982FB5E6BC053E98FE7C33789288CAA6A9883C0D2380DD1812FCF2681A8B31545B97DD0736EB3ECBD9329F144CDB93C35780559DB6219604ADB3F5A8DC57E06CFD715FFCECD3CB65DE7BFDA065D4DB3BDC84B7E0FD66116C71AC41E0B875BA18C742A8ECE9E690AC37457DD43845F5C64EA00BF7B585A6FCF75A0F398026CD79C74C3C946C11BAFD1404997917C5592B91E8415'
    #Headers for the REST request
    @headers = {'Content-Type' =>'application/json', 'licenseid'=> @licenseid}

    #Base URL to apigee Credit proxies
    @url = 'https://apis.cert.vantiv.com/v1/credit/'
    uri = URI(@url)
    #create http connection
    @http = Net::HTTP.new(uri.host, uri.port)
    @http.use_ssl = true
    @http.verify_mode = OpenSSL::SSL::VERIFY_NONE
    #logging to stdout
    #http.set_debug_output($stdout)
  end

  def send_authorize
    url = @url + 'authorization?sp=1'
    puts url
    uri = URI(url)
    #get the authorization object
    auth = Auth.new
    #get the authorization payload
    payload = auth.getPayload
    puts 'TIME: ' + payload['transaction'][:TransactionTimestamp]
    puts 'Authorize Payload :  ' + payload.to_json
    #send http post request
    puts 'Sending Authorize...'
    response = @http.post(uri.request_uri, payload.to_json, @headers)
    #show response
    puts 'Response : ' + response.body
    return response
  end

  def send_capture(refNum, authCode)
    #get capture object
    capt = Capture.new
    #get capture payload
    payload = capt.getPayload

    payload['transaction'][:OriginalReferenceNumber] = refNum
    payload['transaction'][:AuthorizationCode] = authCode
    puts 'Capture Payload :  ' + payload.to_json
    uri = URI(@url + 'authorizationcompletion?sp=1')

    puts 'Sending Capture...'
    response = @http.post(uri.request_uri, payload.to_json, @headers)

    #show response
    puts 'Response : ' + response.body
    return response
  end

  def send_purchase
    url = @url + 'sale?sp=1'
    puts url
    uri = URI(url)
    #get the authorization object
    purch = Purchase.new
    #get the authorization payload
    payload = purch.getPayload
    puts 'Purchase Payload :  ' + payload.to_json
    #send http post request
    puts 'Sending Purchase...'
    response = @http.post(uri.request_uri, payload.to_json, @headers)
    #show response
    puts 'Response : ' + response.body
    return response
  end


  def send_cancel(refNum, authCode, timestamp, cancelType)
    #get capture object
    cancel = Cancel.new
    #get capture payload
    payload = cancel.getPayload

    payload['transaction'][:OriginalReferenceNumber] = refNum
    payload['transaction'][:OriginalAuthCode] = authCode
    payload['transaction'][:OriginalTransactionTimestamp] = timestamp
    payload['transaction'][:CancelType] = cancelType

    puts 'Cancel Payload :  ' + payload.to_json
    uri = URI(@url + 'reversal?sp=1')

    puts 'Sending Cancel...'
    response = @http.post(uri.request_uri, payload.to_json, @headers)

    #show response
    puts 'Response : ' + response.body
    return response
  end


  #helper function to parse the response and return any values that may be needed for future transactions
  def parseResponse(response)
    #get required data from the response to use in future transactions(authorization code, reference number...)
    jsonResp = JSON.parse(response.body)

    #If it isn't a auth/capture/purchase/cancel response, then it must be a fault/error
    if jsonResp.has_key?("AuthorizeResponse") || jsonResp.has_key?("AuthorizationCompletionResponse") || jsonResp.has_key?("SaleResponse") || jsonResp.has_key?("ReverseResponse")
      key = jsonResp.keys[0]
      refNum = jsonResp[key]['ReferenceNumber']
      authCode = jsonResp[key]['AuthorizationCode']
      timestamp = jsonResp[key]['TransmissionTimestamp']
      return refNum, authCode, timestamp
    elsif jsonResp.has_key?("Fault")
      puts 'FAULT: ' + jsonResp['Fault'].to_s

    else
      puts 'ERROR: ' + jsonResp.to_s
    end


  end


end