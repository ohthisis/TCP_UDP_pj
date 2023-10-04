import json
import socket
#import subprocess


# import threading
import pymongo

connection = pymongo.MongoClient("localhost", 27017)
database = connection["test"]
store = database["students"]


class TCPserver():

    def __init__(self):
        self.server_ip='localhost'#(len )private server
        self.server_port=9999
        self.toSave={}

    def main(self):
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# ipv4 နဲ့ tcp protocol //
        #protocol ဆိုတာ ဆက်သွယ်သူနှစ်ဖက်စလုံး နားလည်လို့ဖန်တီးထားတာ
        server.bind((self.server_ip,self.server_port))
        #serve အလုပ်စလုပ်တာ
        server.listen(1)
        print("Server listen on port:{} and ip {}".format(self.server_port,self.server_ip))
        #  print(f'[*] Listening on {self.server_ip}:{self.server_port}')#client ကနေလာပီးချိတ်တာကိုစောင့်နေတာ

        while True:
            client, address=server.accept()# client လာချိတ်တာကိုလက်ခံလိုက်တာ။

            print(f'[*] Accepted connection from {address[0]}:{address[1]}')#လာချိတ်ရင်လဲ ဘယ်ip,ဘယ်port နဲ့ လာချိတ်ပါတယ်ဆ်ုတာပြတာ
            self.handle_client(client)
    #         client_handler=threading.Thread(target=self.handle_client,args=(client,))
    #         client_handler.start()
    #
    # def handle_client(self,client_socket):
    #     with client_socket as sock:
    #         request=sock.recv(1024)#102byte နဲ့လက်ခ့လိုက်တာ
    #         print(f'[*] Received: {request.decode("utf-8")}')# decode လုပ်ပေးရတယ် ပို့လာတဲ့ဒေတာကို
    #
    #         testString=request.decode("utf-8")
    #         print(f'CypherText{testString} ')
    #         sock.send(b'ACK')
    # def handle_client(self,client_socket):
    #     with client_socket as sock:
    #         from_client=sock.recv(2096)
    #         received_data=from_client.decode("utf-8")
    #         print("Received Data from Client",received_data)
    #         self.toSave.update(received_data)
    #         message="server got it:>"+received_data
    #         to_send=bytes(message,"utf-8")
    #         sock.send(to_send)

    def handle_client(self, client_socket):
        with client_socket as sock:
            from_client = sock.recv(1024)

            received_data = from_client.decode("utf-8")
            # print("Received Data from Client", received_data)
            #
            # # Update the toSave dictionary properly
            # key = len(self.toSave)
            # self.toSave[key] = received_data
            # # Execute the received command using subprocess
            # try:
            #     return_value = subprocess.call(received_data, shell=True)
            #     print("Command executed with return value:", return_value)
            # except subprocess.CalledProcessError as e:
            #     print("Error executing command:", e)
            #
            # message = "server got it:>" + received_data
            # to_send = bytes(message, "utf-8")
            # sock.send(to_send)
            if received_data == "Get":
                self.get_all_data(sock)

    def get_all_data(self,sock):
        data:dict={}
        id=0
        for i in store.find({},{'_id':0}):
            id=len(data)
            data_form={"name":i["name"],"email":i["email"]}
            data.update({id:data_form})
        str_data = json.dumps(data)
        print(str_data)
        print(type(str_data))

        str_data=bytes(str_data,'utf-8')
        sock.send(str_data)




            #print(i)


if __name__== '__main__' :
    Myserver=TCPserver()
    Myserver.main()

