import sys
#add sub folders to class path
sys.path.append('C:/Users/N13811A/PycharmProjects/PWS_Apigee_Sample/apigee_objects')
from send_to_apigee import Send_Request

auth = Send_Request().send_auth()

capture = Send_Request().send_capture(auth)

sale = Send_Request().send_purchase()








