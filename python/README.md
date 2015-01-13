Vantiv-Developer-Portal and Vantiv-Payment-Web-Services
=======================================================
*** IMPORTANT You will need to create a project at https://apideveloper.vantiv.com/ in order to get access to the sandbox and test your code

Integration Guidelines available here: https://apideveloper.vantiv.com/docs/payment-web-services/implementation-guidelines<br>
Online developers guide: https://apideveloper.vantiv.com/documentation<br>

The python implementation of Vantiv-Developer-Portal sample code demonstrating how to integrate with both Vantiv-Developer-Portal as well as Vantiv-Payment-Web-Services
- Contains a REST sample* for integrating to Vantiv-Developer-Portal 

* Please note that if you are unsure of which solution which will match your solution needs you should contact a vantiv solution consultant first before starting any development efforts. Not doing so may lead to lost coding time. 


This application was built using PyCharm and Python 3.4.1
You will need to download the external module "requests".
To run this application, run test.py.

####Folder Contents
* test.py - entry point for running the script. It runs an authorize, a capture, and a purchase.
* apigee_objects - Folder containing all classes that are used to send requests to Apigee.
	* address.py - container for all address information			
	* card.py - container for all Card information			
	* credentials.py - container for credential information (username and password)
	* merchant.py - container for all merchant information.
	* terminal.py - Container for all terminal information.
	* transaction.py - container for all transaction information.
	* authorize_json.py - creates a JSON object for an authorize and sets the values for all fields being sent.
	* capture_json.py - creates a JSON object for an capture and sets the value for all fields being sent.
	* purchase_json.py - creates a JSON object for an purchase and sets the value for all fields being sent.
	
