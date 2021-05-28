import subprocess
import socket
import threading

def OpenVulnServer():
    try:
        print("[*] Creating process....")
        #F:\RaviTeja\Fuzzer\Vulnserver\vulnserver.exe    
        p=subprocess.Popen(["F:\\RaviTeja\\Fuzzer\\Vulnserver\\vulnserver.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errormsg = p.communicate()
        print ("[*] Process spawned and the output is %s \n",errormsg)
    except Exception as e:
        print("[*] Exception from opening vuln server thread")
        print("[*] Found an exception "+str(e))
        exit()

def GeneratePayloadAndSendToVulnServer(cmd,multiple):
    try:
        # Creating payload in increments and sending to vulnserver        
        payload=cmd+' '+'A'*multiple+" \r\n"        
        #print("[*] payload sent is "+payload)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost",9999))
        s.send(payload.encode())
        s.close()
    except Exception as e:
        print("[*] Exception from generating and sending Payload")
        print("[*] Exception raised while communication to vulnserver "+str(e))

try:
    #Creating vuln server thread
    t1=threading.Thread(target=OpenVulnServer,args=())
    i=1; 
    t1.start()
    while 1:
        t2=threading.Thread( target=GeneratePayloadAndSendToVulnServer,args=("TRUN ", i*100))       
        t2.start()
        i=i+1;
        print("[*] New thread started and payload of "+str(i)+" hundreds"+" A's sent")
except Exception as e:
   print ("Error: unable to start thread"+str(e))


