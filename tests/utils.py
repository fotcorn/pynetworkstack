from binascii import hexlify

def print_object(obj):
    for t in obj.__dict__.items():
        try:
            print t[0] + ': ' + hex(t[1])
        except:
            try:
                print t[0] + ': ' + hexlify(t[1])
            except:
                print t[0] + ': ' + t[1]