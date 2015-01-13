
package com.vantiv.services.merchant.payments.v6;

import javax.xml.ws.WebFault;


/**
 * This class was generated by Apache CXF 3.0.1
 * 2014-07-31T13:47:48.470-06:00
 * Generated source version: 3.0.1
 */

@WebFault(name = "RequestValidationFault", targetNamespace = "urn:com:vantiv:types:payment:transactions:v6")
public class RequestValidationFault extends Exception {
    
    private com.vantiv.types.payment.transactions.v6.RequestValidationFault requestValidationFault;

    public RequestValidationFault() {
        super();
    }
    
    public RequestValidationFault(String message) {
        super(message);
    }
    
    public RequestValidationFault(String message, Throwable cause) {
        super(message, cause);
    }

    public RequestValidationFault(String message, com.vantiv.types.payment.transactions.v6.RequestValidationFault requestValidationFault) {
        super(message);
        this.requestValidationFault = requestValidationFault;
    }

    public RequestValidationFault(String message, com.vantiv.types.payment.transactions.v6.RequestValidationFault requestValidationFault, Throwable cause) {
        super(message, cause);
        this.requestValidationFault = requestValidationFault;
    }

    public com.vantiv.types.payment.transactions.v6.RequestValidationFault getFaultInfo() {
        return this.requestValidationFault;
    }
}
