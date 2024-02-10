from render import render
from socketserver import BaseServer, BaseRequestHandler, TCPServer




class Handler(BaseRequestHandler):
    
    def handle(self) -> None:
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        
        # Отправляем обратно клиенту данные
        self.request.sendall(render('base.html'))

if __name__ == "__main__":
    # Устанавливаем адрес и порт сервера
    HOST, PORT = "localhost", 9999

    # Создаем сервер, используя наш класс обработчика запросов
    with TCPServer((HOST, PORT), Handler) as server:
        # Запускаем сервер и ожидаем соединений
        print("Server running on {}:{}".format(HOST, PORT))
        server.serve_forever()
    








