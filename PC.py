class PC():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.reboot_counter = 0

    def reboot(self):
        self.reboot_counter += 1
        print(self.name, "is reboot", self.reboot_counter, "times")

    def shutdown(self):
        self.reboot_counter += 1
        print(self.name, "is shutdown", self.reboot_counter, "times")


machenike = PC("machenike", "game")
machenike.reboot()
machenike.reboot()
machenike.shutdown()
