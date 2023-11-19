import os
import subprocess

def banner():
    RED = "\33[91m"

    banner = f"""
    {RED} 
                                                                
     _____ ___ ___             _            _____         _     
    |     |  _|  _|___ ___ ___|_|_ _ ___   |_   _|___ ___| |___ 
    |  |  |  _|  _| -_|   |_ -| | | | -_|    | | | . | . | |_ -|
    |_____|_| |_| |___|_|_|___|_|\_/|___|    |_| |___|___|_|___|
                                                            
    *******************************************************
    *     This tool was created with the aim of           *  
    *     installing some tools for pentesting.           *
    *     By yoonsantos                                   *
    *                                                     *
    *     Currently only works for ubuntu                 *
    *******************************************************
    """
    print(banner)
    
def menu():
    RED = "\33[91m"

    menu = f"""
    {RED}           
    *******************************************************
    *     Menu:                                           *  
    *     1 - Install                                     *
    *     2 - List tools                                  *
    *******************************************************
    """
    print(menu)
    
def clearOutput():
    os.system("clear")

def operationSystem():
    RED = "\33[91m"

    os = f"""
    {RED}           
    *******************************************************
    *     Based:                                          *  
    *     1 - Ubuntu                                      *
    *     2 - Debian                                      *
    *******************************************************
    """
    print(os)

def install():
    banner()
    menu()
    option = input("Please choose an option and press enter: ")

    if option == "1":
        clearOutput()
        operationSystem()
        os = input("What is your OS: ")
        if os == "1":
            print("Instaling Metasploit Framework")
            metasploit = "sudo snap install metasploit-framework"
            metasploitExecute = subprocess.check_output(metasploit, shell=True)
            print(metasploitExecute.decode('utf-8'))
            
            print("Instaling John The Ripper")
            john = "sudo apt install john"
            johnExecute = subprocess.check_output(john, shell=True)
            print(johnExecute.decode('utf-8'))
            
            print("Instaling Feroxbuster")
            feroxbuster = "sudo snap install feroxbuster"
            feroxbusterExecute = subprocess.check_output(feroxbuster, shell=True)
            print(feroxbusterExecute.decode('utf-8'))
            
            print("Instaling Hydra")
            hydra = "sudo apt install hydra"
            hydraExecute = subprocess.check_output(hydra, shell=True)
            print(hydraExecute.decode('utf-8'))
            
            print("Instaling Dirb")
            dirb = "sudo apt install dirb"
            dirbExecute = subprocess.check_output(dirb, shell=True)
            print(dirbExecute.decode('utf-8'))
            
            print("Instaling Nmap")
            nmap = "sudo apt install nmap"
            nmapExecute = subprocess.check_output(nmap, shell=True)
            print(nmapExecute.decode('utf-8'))
            
            print("Install Sucess")
            return False
        
        if os == "2":
            
            print("Currently only works for ubuntu")
            return False
        
        else :
            os = input("Please select a valid option: ")
            return True 
            
    if option == "2":
        clearOutput()
        banner()
        tools()
        
    else :
        os = input("Please select a valid option: ")
        return True    
    
def tools():
    tools = """
    *******************************************************
    *     These tools will be installed:                  * 
    *                                                     * 
    *     1 - Metasploit Framework                        *  
    *     2 - John The Ripper                             *
    *     3 - Feroxbuster                                 *
    *     4 - Hydra                                       *
    *     5 - Dirb                                        *
    *     6 - Nmap                                        *
    *******************************************************
        """
    print(tools)
    
    back = input("Return to menu (y/n)? ")
    if back == "y":
        clearOutput()
        install()
    else:
        return False

if __name__ == "__main__":
   
    execution = True
    while execution:
        execution =  install()