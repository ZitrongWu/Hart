import codecs
import base64
class Server_list:

    def __init__(self) -> None:
        self.list = {}
        self.updata = False

    def active(self,server):
        self.list[server] = True
    def check(self):
        offlinelist = []
        for server,isalive in self.list.items():
            if isalive == False:
                offlinelist.append(server)
            else:
                self.list[server] = False
            
        for offline in offlinelist:
            self.list.pop(offline)
        
        print(self.list.keys())
        urlstr = ""
        for url,state in self.list.items():
            urlstr = urlstr + url + "\n"
        listfile = codecs.open("/ssr/ssr_server_list","w",encoding='utf-8')
        
        listfile.write(base64.b64encode(urlstr.encode('utf-8')).decode('utf-8'))

        listfile.close()