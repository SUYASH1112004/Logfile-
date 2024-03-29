import psutil
import os
from sys import *
import time

def processdisplay(log_dir="Logfile"):
    listprocess=[]
    if not os.path.exists(log_dir):
        try:
          os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"Logfile.log")
    f=open(log_path,'w')
    f.write(separator+"\n")
    f.write("Automation For Creating log file "+ time.ctime()+"\n")
    f.write(separator+"\n")
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.ZombieProcess,psutil.AccessDenied,psutil.NoSuchProcess):
            pass

    for elem in listprocess:
        f.write("%s\n"%elem)

    
def main():
    print("----Automation By SJP---")
    if(len(argv)!=2):
        print("Error:Invalid Number Of Arguments ")

    elif(argv[1]=="-h" or argv[1]=="-H"):
        print("The Script Is Making Log Record Of Running Process..")
        exit()

    elif(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Application_name Absolute_path_directory ")
        exit()

    try:
        processdisplay(argv[1])
    except ValueError:
        print ("Error :Invalid datatype of input")
    except:
        print("Error: Invalid input")

if __name__=="__main__":
    main()
