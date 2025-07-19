from colorama import Fore, Style
import requests
import os
import sys
from ui.ui import *
from bs4 import BeautifulSoup
import hashlib
from passlib.hash import nthash
import time
import socket
import subprocess
import dns.resolver
import whois
from datetime import datetime
def header(menu=True):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.DiagonalBackwards(Colors.red_to_yellow, ("""
                                                                

    ██╗    ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
    ██║    ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
    ██║ █╗ ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
    ██║███╗██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
    ╚███╔███╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
     ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                  
    """)))
        print(f'{Fore.WHITE} Developped By {Fore.CYAN}zKaiioZ {Fore.WHITE} & {Fore.RED}Cat.Sh'.center(60))
        
        if menu:
            print(Colorate.Vertical(Colors.cyan_to_blue,"""
            1 - Web Page Scraping 
            2 - Website Meta Lookup 
            3 - Reverse DNS Lookup
            4 - Whois DNS 
            5 - Ports Scanner
            6 - Href Finder
            7 - Hash Broker
            ! - Quit
                  """))
            a = input("[ ] Choose an option : ")
            
            if a == "1":
                web_scrap()
            elif a == "2":
                web_lookup()
            elif a == "3":
                reverse_dns()
            elif a == "4":
                whois_domain()
            elif a == "5":
                port_scanner()
            elif a == "6":
                href_finder()
            elif a == "!":
                sys.exit(0)  
            else:
                print("[-] Invalid option. Please enter a valid number.")
                time.sleep(2)
                header(menu=True)
    except KeyboardInterrupt:
        print("\n\n[!] Exiting...")
        time.sleep(1)
        sys.exit(0)

def web_scrap():
    url_raw = input("\n[/] Enter the URL : ")
    url = url_raw.strip()
    if not url.startswith('http'):
        url = 'http://' + url
    elif url.startswith('https'):
        url = url
    else:
        url = url    
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'\n[-] Error during HTTP request: \n\n Error : "{e}"')
        return
    if response.status_code == 400:
        print("\n[-] Error during HTTP request: 400")
    elif response.status_code == 404:
        print("\n[-] Not found")
    else:
        resp = response.text
        counter = 0
        filename = f"output/web-scrap/{url_raw}.html"
        while os.path.isfile(filename):
            counter += 1
            filename = f"output/web-scrap/{url_raw}({counter}).html"
        with open(filename, "a+") as web_scrap:
            web_scrap.write(resp)
        print(f"\n{resp}")
    print(Fore.LIGHTCYAN_EX + f"Saved as {filename}")
    input(Colorate.Horizontal(Colors.rainbow, ("Press Enter to continue...")))
    header(menu=True)
    
def web_lookup():
    url_raw = input("\n[/] Enter the URL : ")
    url = url_raw.strip()
    if not url.startswith('http'):
        url = 'http://' + url
    elif url.startswith('https'):
        url = url
    else:
        url = url
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'\n[-] Error during HTTP request: \n\n Error : "{e}"')
        return
    if response.status_code == 400:
        print("\n[-] Error during HTTP request: 400")
    elif response.status_code == 404:
        print("\n[-] Not found")
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        paragraphs = soup.find_all('p')
        para_text = ""  
        for paragraph in paragraphs:
            para = paragraph.text.strip()
            para_text += para

        blabla = f"""
----------------------------------------------------------------------
Web Scraping for: {url} 
----------------------------------------------------------------------
Title: {title_tag.text.strip()}
----------------------------------------------------------------------
Paragraphs: {para_text}
----------------------------------------------------------------------
        """
        print(Fore.CYAN + Style.BRIGHT + blabla)
        counter = 0
        filename = f"output/web-lookup/{url_raw}.txt"
        while os.path.isfile(filename):
            counter += 1
            filename = f"output/web-lookup/{url_raw}({counter}).txt"
        with open(filename, "a+") as web_look:
            web_look.write(blabla)
        print(Fore.LIGHTCYAN_EX + f"Saved as {filename}")
        input(Colorate.Horizontal(Colors.rainbow, ("Press Enter to continue...")))
        header(menu=True)

def reverse_dns():
    url = input("\n[/] Please enter a URL: ")
    api = f"http://ip-api.com/json/{url}?fields=query,status,message,continent,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy"
    data = requests.get(api).json()
    if data["status"] == "fail":
        print(f"Erreur: {data['message']}")
    else:
        ip_v4 = data.get('query', '')
        
        blabla = f"""
+-----------------------------------------------+
- Reverse DNS Lookup for: {url} - 
/\ IP (IPv4) : {ip_v4:<24}
\/ ISP       : {data['isp']:<24}
/\ Country   : {data['country']:<24}
\/ City      : {data['city']:<24}
+-----------------------------------------------+
        """
        print(Colorate.Vertical(Colors.purple_to_red,(blabla)))
        counter = 0
        filename = f"output/reverse-dns/{url}.txt"
        while os.path.isfile(filename):
            counter += 1
            filename = f"output/reverse-dns/{url}({counter}).txt"
        with open(filename, "a+") as web_look:
            web_look.write(blabla)
        print(Fore.LIGHTCYAN_EX + f"Saved as {filename}")
        input(Colorate.Horizontal(Colors.rainbow, ("Press Enter to continue...")))
        header(menu=True)

def port_scanner():
    remoteServer = input("[/] Enter the host ip : ")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print("\n" +  "-" * 60)
    print("Wait while scanning the host", remoteServerIP)
    print("-" * 60)
    t1 = datetime.now()
    try:
        for port in range(1,1025):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("The port {} is open ".format(port))
                try: 
                    servicename = socket.getservbyport(port)
                    print("Service name : {}".format(servicename))
                except OSError: 
                    print("Service name : Unknow")
                try:
                    processname = subprocess.check_output(["lsof", "-i:"+str(port)], universal_newlines=True).split('\n')[1].split()[0]
                    print("Process name : {}".format(processname))
                except IndexError: 
                    print("Process name : Unknow")
                print("-" * 60)
            sock.close()
    except KeyboardInterrupt:
        input(Colorate.Horizontal(Colors.rainbow, ("\nPress Enter to continue...")))
        header(menu=True)
    except socket.gaierror:
        print('Host unknow, EOF')
        input(Colorate.Horizontal(Colors.rainbow, ("\nPress Enter to continue...")))
        header(menu=True)
    except socket.error:
        print("Can't reach the host, EOF")
        input(Colorate.Horizontal(Colors.rainbow, ("\nPress Enter to continue...")))
        header(menu=True)
    t2 = datetime.now()
    total =  t2 - t1
    print('Scanning Completed in: ', total)
    input(Colorate.Horizontal(Colors.rainbow, ("\nPress Enter to continue...")))
    header(menu=True)
    
def href_finder():
    url_raw = input("\n[/] Enter the URL : ")
    url = url_raw.strip()
    if not url.startswith('http'):
        url = 'http://' + url
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'\n[-] Error during HTTP request: \n\n Error : "{e}"')
        return
    if response.status_code == 400:
        print("\n[-] Error during HTTP request: 400")
        return
    elif response.status_code == 404:
        print("\n[-] Not found")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    hrefs = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            hrefs.append(href)
            print(href)
    counter = 0
    filename = f"output/href-lookup/{url_raw}.txt"
    while os.path.isfile(filename):
        counter += 1
        filename = f"output/href-lookup/{url_raw}({counter}).txt"
    with open(filename, "w") as href_file:
        href_file.write("\n".join(hrefs))
    print(Fore.LIGHTCYAN_EX + f"Saved as {filename}")
    input("\nPress Enter to continue...")
    header(menu=True)

def whois_domain():
    domain = input("Entrez le nom de domaine : ")
    counter = 0
    filename = f"output/whois-dns/{domain}.txt"
    while os.path.isfile(filename):
        counter += 1
        filename = f"output/whois-dns/{domain}({counter}).txt"
    with open(filename, "w") as output_file:
        try:
            domain_info = whois.whois(domain)
            output_file.write("Informations sur le propriétaire du domaine:\n")
            for key, value in domain_info.__dict__.items():
                print(f"{key} : {value}")
                output_file.write(f"{key} : {value} \n")
            ns_records = dns.resolver.resolve(domain, 'NS')
            output_file.write("\nName Server (NS) Records:\n")
            for data in ns_records:
                print(data.to_text())
                output_file.write(f"{data.to_text()}\n")
            mx_records = dns.resolver.resolve(domain, 'MX')
            output_file.write("\nMail Exchange (MX) Records:\n")
            for data in mx_records:
                print(data.to_text())
                output_file.write(f"{data.to_text()}\n")
            txt_records = dns.resolver.resolve(domain, 'TXT')
            output_file.write("\nText (TXT) Records:\n")
            for data in txt_records:
                print(data.to_text())
                output_file.write(f"{data.to_text()}\n")
            a_records = dns.resolver.resolve(domain, 'A')
            output_file.write("\nAddress (A) Records:\n")
            for data in a_records:
                output_file.write(f"{data.to_text()}\n")
            aaaa_records = dns.resolver.resolve(domain, 'AAAA')
            output_file.write("\nIPv6 Address (AAAA) Records:\n")
            for data in aaaa_records:
                print(data.to_text())
                output_file.write(f"{data.to_text()}\n")
        except dns.resolver.NoAnswer:
            output_file.write("\nNo response for the domain.\n")
        except dns.resolver.NXDOMAIN:
            output_file.write("\nThe domain specified does not exist.\n")
        except dns.resolver.Timeout:
            output_file.write("\nThe DNS request has expired.\n")
        except dns.resolver.NoNameservers:
            output_file.write("\nNo name servers are available\n")
        except dns.exception.DNSException as e:
            output_file.write(f"\nDNS error : {e}\n")
        except Exception as e:
            output_file.write(f"Error: {e}\n")

    print(Fore.LIGHTCYAN_EX + f"Saved as {filename}")
    input(Colorate.Horizontal(Colors.rainbow, ("\nPress Enter to continue...")))
    header(menu=True)
    
header(menu=True)