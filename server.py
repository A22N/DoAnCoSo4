
import base64
  
  
# with open("1.png", "rb") as image2string:
#     converted_string = base64.b64encode(image2string.read())
# print(converted_string)
  
# with open('encode.txt', "wb") as file:
#     file.write(converted_string)
    

  
file = open('encode.txt', 'rb')
byte = file.read()
file.close()
  
decodeit = open('hello_level.png', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()