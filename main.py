import base64

encoded_value = "TXBhdGNoQHBhc3N3b3JkMTIzNA=="
decoded_value = base64.b64decode(encoded_value).decode("utf-8")
print(decoded_value)
