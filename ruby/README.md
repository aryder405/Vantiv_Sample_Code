Vantiv-Developer-Portal and Vantiv-Payment-Web-Services
=======================================================
*** IMPORTANT You will need to create a project at http://vantiv.devportal.apigee.com/ in order to get access to the sandbox and test your code

Integration Guidelines available here: https://apideveloper.vantiv.com/docs/payment-web-services/implementation-guidelines
Online developers guide: https://apideveloper.vantiv.com/documentation

The Ruby implementation of Vantiv-Developer-Portal sample code demonstrating how to integrate with both Vantiv-Developer-Portal as well as Vantiv-Payment-Web-Services
- Contains a REST sample* for integrating to Vantiv-Developer-Portal 
- Contains a SOAP sample* for integrating to Payment-Web-Services

* Please note that if you are unsure of which solution which will match your solution needs you should contact a vantiv solution consultant first before starting any development efforts. Not doing so may lead to lost coding time. 

This application was built using RubyMine and Ruby 1.9.3
You can start this application by running test.rb.

####Folder Contents
test.rb - this is the main class that uses driver.rb to show the requests/responses.
driver.rb - this class uses the objects within Apigee_Objects to send the requests.
Apigee_Objects 
	auth.rb - this is the authorize object
	cancel.rb  - this is the cancel object
	capture.rb - this it the capture object
	purchase.rb - this is the purchase object