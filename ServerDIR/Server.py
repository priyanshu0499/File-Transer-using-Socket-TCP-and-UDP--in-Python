import time
import socket
import os
local_ip= "127.0.0.1"
port=9999
format='utf-8'
size=1024
# path="C:/Users/priya/Networks/Assignement/SocketDIR/Directory"

  
def filetransfer(file_name):
    server1=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(file_name,'rb') as f:
        data=f.read(1024)
        server1.sendto(data,(local_ip,9998))
        time.sleep(0.05)
    server1.close()



def filetransferall(server,i):

    conn1,adr1=server.accept()
    name=i
    conn1.send(bytes(name, 'utf-8'))
    time.sleep(0.05)
    with open(name,'rb') as f:
        data=f.read(1024)
        conn1.sendall(data)
    conn1.close()

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((local_ip,port))
    server.listen(5)
   
    print("Server is up and listening")
    while True:
        try:
            conn,adr=server.accept()
            print(f"New Connection with {adr} connected")
            msg="Requests Available : \n 1. listallfiles \n 2. download <filename> \n 3. download all \n 4. exit "
            conn.send(msg.encode('utf-8'))
            while conn:
                

                    
                    
                
                    msg=conn.recv(1024).decode(format)
                    m=msg.split()
                    if m[0]=='listallfiles':
                    
                        files = os.listdir(os.curdir)
                        file_names=""
                        for f in files:
                            file_names= file_names+f+"\n"
                        conn.send(bytes(file_names,format))
                    elif(m[0]=='download' and m[1]=='all'):
                        files=(os.listdir(os.curdir))
                        conn.send(str(len(files)).encode(format))

                        for i in files:
                            filetransferall(server,i)
                    elif(m[0]=='download'):
                        file_name=m[1]
                        filetransfer(file_name)
                    elif(m[0]=='exit'):
                        
                        server.close()
                        break
        except:
                print('Connection has ended')
                break



            

if __name__=='__main__':
    main()