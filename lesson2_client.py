import socket
import json
class TCPclient():


    def __init__(self,sms):
        self.target_ip='localhost'
        self.target_port=9998
        self.input_checking(sms)

    def run_client(self):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((self.target_ip,self.target_port))

        return client

    def input_checking(self,sms):
        if sms=="Get":
            self.get_all_data(sms)
        elif sms=="login":
            self.login(sms)
        else:
            print("hello")

    def get_all_data(self,sms):
        client=self.run_client()
        sms=bytes(sms,"utf-8")
        client.send(sms)
        received_from_server=client.recv(4096)
      #  print(received_from_server.decode("utf-8"))
        dict_data:dict =json.loads(received_from_server.decode("utf-8"))

        client.close()

    def login(self,info):
        try:
            print("This is login form")
            l_email=input("Enter your email to login")
            l_pass=input("Enter your password to login")
            client=self.run_client()
            sms=info+' '+l_email+' '+l_pass
            sms=bytes(sms,"utf-8")
            client.send(sms)
            received_from_server = client.recv(4096)
           # print(received_from_server.decode("utf-8"))
            user_info:dict= json.loads(received_from_server.decode("utf-8"))
            self.option_choice(user_info,client)
            client.close()

        except Exception as err:
            print("you have error")

    def registeration(self,info):
        print("This is Registration option")

    def option_choice(self,user_info,client):
        print("Email :", user_info["email"])
        print("Info :", user_info["info"])
        print("Point :", user_info["point"])
        try:
            option = input("Press one to Get User Option:\nPress 2 to Main option\nPress 3 to exit")
            if option=='1':
                self.User_Option(user_info,client)
            elif option=='2':
                pass
            elif option=='3':
                exit(2)
            else:
                print("Invalid option\\")
                self.option_choice(user_info,client)

        except Exception as error:
            print("You have error1")
    def User_Option(self,user_info,client):
        pass



if __name__=="__main__":
    while True:
        sms=input("Enter some data to send")
        tcp_client=TCPclient(sms)

