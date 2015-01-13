require_relative('driver')

class Test

  driver = Driver.new

  #send authorize
  resp = driver.send_authorize

  #get referenceNumber and authorizationCode from response
  refNum, authCode = driver.parseResponse(resp)

  #if they exist(no error), then call the capture
  if refNum && authCode
    resp = driver.send_capture(refNum, authCode)
    driver.parseResponse(resp)
  end


  #send a purchase
  resp = driver.send_purchase

  refNum, authCode, tstamp = driver.parseResponse(resp)

  if refNum && authCode
  #cancel the purchase
  driver.send_cancel(refNum, authCode, tstamp, 'purchase')
  end

end