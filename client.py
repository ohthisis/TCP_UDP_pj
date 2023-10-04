import socket

class TCPclient():
    def __init__(self,sms):
        self.target_ip='localhost'
        self.target_port=9999
     #   self.send_and_received={}

        self.client_sms= bytes(sms,'utf-8')

     #   self.send_and_received.update({len(self.send_and_received):sms})
    def run_client(self):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((self.target_ip,self.target_port))
        client.send(self.client_sms)
        received_from_server=client.recv(2096)
        recv_sms=received_from_server.decode("utf-8")
    #    self.send_and_received.update({len(self.send_and_received):recv_sms})
        print("Get back data from Server:",recv_sms)

if __name__=="__main__":
    while True:
        sms=input("Enter some data to send")
        tcp_client=TCPclient(sms)
        tcp_client.run_client()
