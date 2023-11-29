import os
import subprocess

def banner():
    RED = "\33[91m"

    banner = f"""
    {RED} 
                                                                
  _  __     _ _ ___          _        
 | |/ /__ _| (_) _ )_  _ _ _| |_ _  _ 
 | ' </ _` | | | _ \ || | ' \  _| || |
 |_|\_\__,_|_|_|___/\_,_|_||_\__|\_,_|
                                        
******************************************************* 
*     Install some Kali Linux tools in Ubuntu         *
*     By axroot                                       *
*                                                     *
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


def install():
    banner()
    menu()
    option = input("Please choose an option and press enter: ")

    if option == "1":
        print("Instaling Metasploit Framework")
        metasploit = "sudo snap install metasploit-framework"
        subprocess.run(metasploit, shell=True)
        print("Installing metasploit framework ...")
            
        print("Instaling John The Ripper")
        john = "sudo apt install john -y"
        subprocess.run(john, shell=True)
        print("Installing john the ripper ...")
            
        print("Instaling Feroxbuster")
        feroxbuster = "sudo snap install feroxbuster"
        subprocess.run(feroxbuster, shell=True)
        print("Installing feroxbuster ...")
            
        print("Instaling Hydra")
        hydra = "sudo apt install hydra -y"
        subprocess.run(hydra, shell=True)
        print("Installing hydra ...")
            
        print("Instaling Dirb")
        dirb = "sudo apt install dirb -y"
        subprocess.run(dirb, shell=True)
        print("Installing dirb ...")
            
        print("Instaling Nmap")
        nmap = "sudo apt install nmap -y"
        subprocess.run(nmap, shell=True)
        print("Installing nmap ...")
        
        print("Instaling Nmap")
        sqlmap = "sudo apt install sqlmap -y"
        subprocess.run(sqlmap, shell=True)
        print("Installing sqnlmap ...")
        
        print("Instaling Crunch")
        crunch = "sudo apt install crunch -y"
        subprocess.run(crunch, shell=True)
        print("Installing crunch ...")
        
        print("Instaling Wireshark")
        wireshark = "sudo apt install wireshark -y"
        subprocess.run(wireshark, shell=True)
        print("Installing wireshark ...")
        
        print("Instaling HashCat")
        hashcat = "sudo apt install hashcat -y"
        subprocess.run(hashcat, shell=True)
        print("Installing hashcat ...")
        
        print("Instaling Hping3")
        hping3 = "sudo apt install hping3 -y"
        subprocess.run(hping3, shell=True)
        print("Installing hping3 ...")
        
        
        clearOutput()
        banner() 
        print("Install Sucess\n\n")
        
        return False
    
            
    if option == "2":
        clearOutput()
        banner()
        tools()
        
    else :
        print("Please select a valid option (1 or 2): ")
        return False
    
def tools():
    tools = """
*******************************************************
*     These tools will be installed:                   * 
*                                                      * 
*     01 - Metasploit Framework                        *  
*     02 - John The Ripper                             *
*     03 - Feroxbuster                                 *
*     04 - Hydra                                       *
*     05 - Dirb                                        *
*     06 - Nmap                                        *
*     07 - SQLmap                                      *
*     08 - Crunch                                      *
*     09 - Wireshark                                   *
*     10 - HashCat                                     *
*     11 - Hping3                                     *
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
