class Whatsapp:
    def message(self):
        print("sent")
class Whatsapp1(Whatsapp):
    def message(self):
        print("sent-delivered")
class Whatsappnew(Whatsapp1):
    def message(self):
        print("sent-delivered-seen")

yugesh=Whatsappnew()
yugesh.message()