
class Server_list:

    def __init__(self) -> None:
        self.list = {}
        self.updata = False

    def active(self,server):
        self.list[server] = True
    def check(self):
        for server,isalive in self.list.items():
            if isalive == False:
                self.list.pop(server)
            else:
                self.list[server] = False
            print(server)
