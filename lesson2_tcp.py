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
        self.server_port=9998
        self.toSave={}

    def main(self):
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        server.bind((self.server_ip,self.server_port))

        server.listen(1)
        print("Server listen on port:{} and ip {}".format(self.server_port,self.server_ip))


        while True:
            client, address=server.accept()# client လာချိတ်တာကိုလက်ခံလိုက်တာ။

            print(f'[*] Accepted connection from {address[0]}:{address[1]}')#လာချိတ်ရင်လဲ ဘယ်ip,ဘယ်port နဲ့ လာချိတ်ပါတယ်ဆ်ုတာပြတာ
            self.handle_client(client)
    def handle_client(self, client_socket):
        data_list=[]
        with client_socket as sock:
            from_client = sock.recv(1024)
            data_list = from_client.decode("utf-8").split(' ')

            if data_list[0] == "Get":
                self.get_all_data(sock)
            elif data_list[0]=="login":
                self.login_checking(sock,data_list)
            else:
                sms=bytes("Invalid option","utf-8")
                sock.send(sms)

    def get_all_data(self,sock):
        data:dict={}
        id=0
        for i in store.find({},{'_id':0}):
            id=len(data)
            data_form={"email":i["email"],"password":i["password"],"phone":i["phone"],"info":i["info"],"point":i["point"]}
            data.update({id:data_form})
        str_data = json.dumps(data)
        print(str_data)
        print(type(str_data))
        str_data=bytes(str_data,'utf-8')
        sock.send(str_data)

    def login_checking(self,sock,datalist):
        l_email=datalist[1]
        l_pass=datalist[2]
        flag = -1
        sms = {}
        for i in store.find({}, {"_id":0, "email":1, "password":1,"info":1,"point":1}):
            if i["email"]==l_email and i["password"]==l_pass:
                flag=1
                sms={"email":i["email"],"info":i["info"],"point":i["point"]}
                sms=json.dumps(sms)
                break

        if flag==1:
            str_data = bytes(sms, 'utf-8')
            sock.send(str_data)
        else:
            str_data = bytes("user not found,please register", 'utf-8')
            sock.send(str_data)



if __name__== '__main__' :
    Myserver=TCPserver()
    Myserver.main()

