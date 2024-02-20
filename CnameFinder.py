#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys,subprocess
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
while True:
    try:
        if len(sys.argv) > 1:
            domain=sys.argv[1]
            fileName=sys.argv[2]
        else:
            print("welcome to Cname Finder :) ")
            domain=input("Please Enter Domain: ")
            fileName=input("Please Enter Your WordList: ")
        data=open(fileName,"r")
        lines=data.readlines()
        for line in lines:
            sub=line.strip()
            result=subprocess.run(['dig', sub + "." + domain ,'cname','+short'],stdout=subprocess.PIPE)
            result=result.stdout.decode("utf-8").strip()
            if len(result) !=0 :
                print( "{0}[{1} + {2}][{3} {4}.{5} {6}][{7} {8} {9}]{10}".format(colors.OKBLUE,colors.FAIL,colors.OKBLUE,colors.WARNING,sub,domain,colors.OKBLUE,colors.WARNING,result,colors.OKBLUE,colors.ENDC) )


        break
    except Exception as e:
            print(e)
            sys.argv[1]=input("Please Enter Domain: ")
            sys.argv[2]=input("Please Enter Your WordList: ")
            
