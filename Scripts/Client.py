import _thread
import time
import socket

from ConnectingClientPage import ConnectingClientPage

class Client:
    
    socket_connection = None
    cs = None

    @classmethod
    def connecting(cls):

        try:
            cls.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cls.socket_connection.bind((socket.gethostname(), 45000))
            cls.socket_connection.listen(1)
        except Exception as err:
            print(err)
            cls.socket_connection.close()

        try:
            _thread.start_new_thread(cls.try_connect, ("Thread-1", 4,))
            _thread.start_new_thread(cls.receiv, ("Thread-2", 4,))
        except:
            print("Error: unable to start thread")
    
    @classmethod
    def try_connect(cls, threadName, delay):
        is_connected = "connected"
        
        while True:
            try:
                cls.cs, address = cls.socket_connection.accept()
                cls.cs.send(bytes(is_connected.encode("utf-8")))
            except:
                pass
    
    @classmethod
    def receiv(cls, threadName, delay):
        is_connected = False
        
        while is_connected is False:
            try:
                receiv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                receiv_socket.connect((socket.gethostname(), 50000))
                
                msg = receiv_socket.recv(10)
                msg_decoded = msg.decode("utf-8")

                if msg_decoded == "connected":
                    ConnectingClientPage._connected()
                    is_connected = True

            except Exception as err:
                print(err)

        while True:
            try:
                pass
                    
            except Exception as err:
                print(err)

    @classmethod
    def send(cls, msg):    
        try:
            cls.cs, address = cls.socket_connection.accept()
            cls.cs.send(bytes(msg.encode("utf-8")))
        except:
            pass

    @classmethod
    def send_rock(cls):
        cls.send("ROCK")

    @classmethod
    def send_paper(cls):
        cls.send("PAPER")
    
    @classmethod
    def send_scissors(cls):
        cls.send("SCISSORS")