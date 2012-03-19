

class EthernetFrame():
    source = destination = protocol = data = None
    
    def __str__(self):
        return hex(self.protocol) + ': ' + hex(self.source) + ' -> ' + hex(self.destination)