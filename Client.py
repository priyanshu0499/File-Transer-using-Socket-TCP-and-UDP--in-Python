import socket
local_ip= "127.0.0.1"
port=9999
format='utf-8'
size=1024
def filereceive(x):
    client1=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client1.bind((local_ip,9998))

    # path="C:/Users/priya/Networks/Assignement/ClientDIR"
    with open(x,'wb') as f:
        data=client1.recv(1024)
        f.write(data)
    client1.close()



    
def filereceiveall():
     client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client1.connect((local_ip, 9999))
    #  path="C:/Users/priya/Networks/Assignement/ClientDIR"
     name=client1.recv(1024).decode(format)
     with open(name,'wb') as f:
         data=client1.recv(1024)
         f.write(data)
     client1.close()
def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((local_ip,port)) 
    msg=client.recv(1024).decode('utf-8') #state request message
    print(msg)
    while True:
        
  
        n=input("State Request :")#input for request
        m=n.split() 
   
        if m[0]=='listallfiles':
            client.send(n.encode(format))
            file_names=client.recv(1024).decode('utf-8')
            print("\nFiles available:")
            print(file_names)
        elif(m[0]=='download' and m[1]=='all'):
            client.send(n.encode(format))
            length=int(client.recv(1024).decode(format))
            for i in range(length):
                filereceiveall()
            print('All files has been successfully downloaded')
        elif(m[0]=='download'):
            x=m[1]
            client.send(n.encode(format))
            # file_name=client.recv(1024).decode('utf-8')
            filereceive(x)
            print('File :'+x+' has been downloaded')
        elif(m[0]=='exit'):
           client.send(n.encode(format))
           client.close()
           
           print("Connection Closed") 
           break
        else:
            print('Invalid Input')
        

            



if __name__=='__main__':
    main()