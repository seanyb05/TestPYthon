import json,os,subprocess
#import firstClass

if __name__== "__main__":
    print("Testing this script")
    getVersion =  subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE).stdout
    version =  str(getVersion.read()).split('\n')
    
    for line in version:
        print(line)