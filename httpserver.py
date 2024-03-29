# # coding:utf-8

# import socket
# import re
# import codecs
# from multiprocessing import Process

# # 设置静态文件根目录
# HTML_ROOT_DIR = "../"


# class HTTPServer(object):
#     def __init__(self):
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     def start(self):
#         self.server_socket.listen(128)
#         while True:
#             client_socket, client_address = self.server_socket.accept()
#             print("[%s, %s]用户连接上了" % client_address)
#             handle_client_process = Process(target=self.handle_client, args=(client_socket,))
#             handle_client_process.start()
#             client_socket.close()

#     def handle_client(self, client_socket):
#         """
#         处理客户端请求
#         """
#         # 获取客户端请求数据
#         request_data = client_socket.recv(1024)
#         print("request data:", request_data)
#         request_lines = request_data.splitlines()
#         # 解析请求报文
#         request_start_line = request_lines[0]
#         # 提取用户请求的文件名
#         file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

#         if "/" == file_name:
#             file_name = "/index.html"

#         # 打开文件，读取内容
#         try:
#             file = codecs.open(HTML_ROOT_DIR + file_name, "r",encoding='utf-8')
#         except IOError:
#             response_start_line = "HTTP/1.1 404 Not Found\r\n"
#             response_headers = "Server: My server\r\n"
#             response_body = "The file is not found!"
#         else:
#             file_data = file.read()
#             file.close()

#             # 构造响应数据
#             response_start_line = "HTTP/1.1 200 OK\r\n"
#             response_headers = "Server: My server\r\n"
#             response_body = file_data

#         response = response_start_line + response_headers + "\r\n" + response_body
#         print("response data:", response)

#         # 向客户端返回响应数据
#         client_socket.send(response.encode('utf-8'))

#         # 关闭客户端连接
#         client_socket.close()

#     def bind(self, port):
#         self.server_socket.bind(("", port))


# def main():
#     http_server = HTTPServer()
#     http_server.bind(5510)
#     http_server.start()


# if __name__ == "__main__":
#     main()

import http.server, ssl
server_ip = '0.0.0.0'
server_port = 5510
server_addr = (server_ip,server_port)
server_cert = '/CRF/cert.pem'
server_key = '/CRF/privkey.pem'

httpd = http.server.HTTPServer(server_addr, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                                server_side=True,
                                certfile=server_cert,
                                keyfile=server_key,
                                ssl_version=ssl.PROTOCOL_TLS)

httpd.serve_forever()