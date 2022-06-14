import base64

with open("./pictures/1.jpg", "rb") as imagestring:
    convert_string = base64.b64encode(imagestring.read())
print(convert_string)