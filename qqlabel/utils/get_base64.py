import base64

def get_base64(path):
    with open(path, 'rb') as image:
        return str(base64.b64encode(image.read()))[1:].strip('\'')

