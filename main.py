import os
from colorama import init, Fore
import pygame 
from pystyle import Center, Colors, Write

init(autoreset=True)
pygame.mixer.init()

def play_music():
    try:
        pygame.mixer.music.load('Psycho Dreams (speed up).mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Erreur de lecture de la musique : {e}")

def stop_music():
    pygame.mixer.music.stop()

def set_volume(level):
    pygame.mixer.music.set_volume(level)

def display_intro():
    os.system('clear' if os.name == 'posix' else 'cls')
    intro = f"""
{Fore.BLUE}
            $$$$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$\ $$$$$$$$\ $$\   $$\    $$\    
            \____$$  |$$  _____|$$$\  $$ |\_$$  _|\__$$  __|$$ |  $$ | $$$$$$\  
                $$  / $$ |      $$$$\ $$ |  $$ |     $$ |   $$ |  $$ |$$  __$$\ 
               $$  /  $$$$$\    $$ $$\$$ |  $$ |     $$ |   $$$$$$$$ |$$ /  \__|
              $$  /   $$  __|   $$ \$$$$ |  $$ |     $$ |   $$  __$$ |\$$$$$$\  
             $$  /    $$ |      $$ |\$$$ |  $$ |     $$ |   $$ |  $$ | \___ $$\ 
            $$$$$$$$\ $$$$$$$$\ $$ | \$$ |$$$$$$\    $$ |   $$ |  $$ |$$\  \$$ |
            \________|\________|\__|  \__|\______|   \__|   \__|  \__|\$$$$$$  |
                                                                       \_$$  _/ 
                                                                         \ _/   
                                                                      
                            > Appuyez sur Entrer                                  
"""
    print(intro)
    input()

menu = f"""
{Fore.RED}
        Commandes pour le volume :
        v+ : Augmente le volume de 0.1.
        v- : Diminue le volume de 0.1.
        v0 : Réduit le volume à 0.0 (silence).
        v1 : Réactive le volume à 0.1 (volume par défaut).

        ▬▬ι═══════════════════════════════════════════════════════════════════════════════════════════════════════ﺤ
                                                            ╔════════════╗
                                                            ║ Multi-Tools║
                                                            ╚════════════╝

        [Menu n°1]
        [01] -> Tool Info                                    |    [07] -> Ip Info (Lookup)
        [02] -> Dark Web Links                               |    [08] -> ( soon )
        [03] -> DDOS 2024                                    |    [09] -> ( soon )
        [04] -> Dox Create                                   |    [10] -> ( soon )
        [05] -> Databases ZENITH$                            |    [11] -> ( soon )
        [06] -> Osint ( 2024 )                               |    [12] -> ( soon )

        |
        -By  1previsible'

        ▬▬ι═══════════════════════════════════════════════════════════════════════════════════════════════════════ﺤ
"""

def display_menu_with_title():
    os.system('clear' if os.name == 'posix' else 'cls')
    title = f"""
{Fore.BLUE}
            $$$$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$\ $$$$$$$$\ $$\   $$\    $$\    
            \____$$  |$$  _____|$$$\  $$ |\_$$  _|\__$$  __|$$ |  $$ | $$$$$$\  
                $$  / $$ |      $$$$\ $$ |  $$ |     $$ |   $$ |  $$ |$$  __$$\ 
               $$  /  $$$$$\    $$ $$\$$ |  $$ |     $$ |   $$$$$$$$ |$$ /  \__|
              $$  /   $$  __|   $$ \$$$$ |  $$ |     $$ |   $$  __$$ |\$$$$$$\  
             $$  /    $$ |      $$ |\$$$ |  $$ |     $$ |   $$ |  $$ | \___ $$\ 
            $$$$$$$$\ $$$$$$$$\ $$ | \$$ |$$$$$$\    $$ |   $$ |  $$ |$$\  \$$ |
            \________|\________|\__|  \__|\______|   \__|   \__|  \__|\$$$$$$  |
                                                                       \_$$  _/ 
                                                                         \ _/   
"""
    print(title)
    print(menu)

def wait_for_enter():
    Write.Print("\nAppuyez sur Entrer pour revenir au menu...", Colors.red, interval=0.005)
    input()
    display_menu_with_title()

def display_tool_info():
    os.system('clear' if os.name == 'posix' else 'cls')
    Write.Print("""
Hey , Ce tools a ete Cree par 1previsible' Le 01/08/2024

Ce tools est 100% safe Aucun virus ni truc malveillant

Voici mes reseau : 

Mon TikTok - > https://www.tiktok.com/@spectreog?lang=fr

Mon youtube - > https://www.youtube.com/channel/UCiXt6uKazsAg6bZQbJERATQ

Mon canal Telegram - > https://t.me/zenithtools
    """, Colors.green, interval=0.005)
    wait_for_enter()

def dox_create():
    data = {
        "Username": "",
        "Name": "",
        "Age": "",
        "Date of Birth": "",
        "Address": "",
        "Phone Number": "",
        "Email": "",
        "IP Address": "",
        "Social Media Accounts": "",
        "Credit Card Info": "",
        "Bank Account Info": "",
        "Personal Information": {},
        "Loc Information": {}
    }

    for key in data:
        if isinstance(data[key], dict):
            sub_dict = data[key]
            for sub_key in ["Info1", "Info2", "Info3"]:
                sub_dict[sub_key] = input(f"Enter {sub_key} for {key}: ").strip()
        else:
            data[key] = input(f"Enter {key}: ").strip()

    output_text = "[!] | Personal Information:\n"
    for key, value in data.items():
        if isinstance(value, dict):
            output_text += f"[>] {key}:\n"
            for sub_key, sub_value in value.items():
                output_text += f"    - {sub_key} : {sub_value}\n"
        else:
            output_text += f"[>] | {key} : {value}\n"

    output_text += "\n[!] | Loc Information:\n"
    for key, value in data["Loc Information"].items():
        output_text += f"[>] | {key} : {value}\n"

    with open("output.txt", "w") as file:
        file.write(output_text)

    Write.Print("\nLes informations ont été sauvegardées dans le fichier 'output.txt'.", Colors.green, interval=0.005)
    wait_for_enter()

def display_ddos_options():
    os.system('clear' if os.name == 'posix' else 'cls')
    Write.Print("""
Tu veux choisir quel site ?
Le premier est un site Google - > https://stresslab.app/u/attacks

Le 2ème aussi -> https://stresser.su/hub

Le 3ème est un site de DDOS puissant, mais il faut installer Tor :
- Stresser : http://ecwvi3cd6h27r2kjx6ur6gdi4brwdllz2k4xjjsckkbvvnbxzxnrs2y4b5s7wnc.onion/
- Stressit : http://flxjtvcsmfczrlqcznhg5jiuhr4zbwtfl5fdzql4y7evnsrjssfgfpv3eht4n.onion/
- Rapture : http://og3z2hs0py3j8ilypfdk4j2hxh1m2kvjcqtzgvj2h5c4ur6h6eslbnyxoeyicgx.onion/
- InterStresser : http://kzry7u5rg4cv5jshx5bq7l5kscmhuwwf3byzfkupfsggup7vep7d4w32ytimlk.onion/
- Ddos Heaven : http://ztu6knqkphopdyjeuj3kgb32szejbwxtxzpq5aqepc3eh5b4yxuov72wgnkikz7.onion/
- The Hammer : http://dbf6zhmgyjpnt74quv5lxhzeegkm4kg6u6gy7m32t6ixv3zxxw5wos7cyrgdnz.onion/

C'est un DDOS puissant mais sur le Dark Web (Il faut installer Tor)
    """, Colors.green, interval=0.005)
    wait_for_enter()

def display_dark_web_links():
    os.system('clear' if os.name == 'posix' else 'cls')
    Write.Print("""
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃                                          Dark Web                                         ┃
            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            ┃Search Engine:                                                                             ┃
            ┃[Torch]        : http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/    ┃
            ┃[Danex]        : http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/    ┃
            ┃[Sentor]       : http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/    ┃
            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            ┃Bitcoin Anonymity:                                                                         ┃
            ┃[Dark Mixer]   : http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/    ┃
            ┃[Mixabit]      : http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/    ┃
            ┃[EasyCoin]     : http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/    ┃
            ┃[Onionwallet]  : http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/    ┃
            ┃[VirginBitcoin]: http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/    ┃
            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            ┃Stresser / Ddos:                                                                           ┃
            ┃[Stresser]     : http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/    ┃
            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            ┃Market:                                                                                    ┃
            ┃[Deep Market]  : http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/    ┃
            ┃[DrChronic]    : http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/    ┃
            ┃[TomAndJerry]  : http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/    ┃
            ┃[420prime]     : http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/    ┃
            ┃[Can*abisUK]   : http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/    ┃
            ┃[DeDope]       : http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/    ┃
            ┃[AccMarket]    : http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/    ┃
            ┃[Cardshop]     : http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/    ┃
            ┃[Darkmining]   : http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/    ┃
            ┃[MobileStore]  : http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/    ┃
            ┃[EuroGuns]     : http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/    ┃
            ┃[UKpassports]  : http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/    ┃
            ┃[ccPal]        : http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/    ┃
            ┃[Webuybitcoins]: http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/    ┃
            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            ┃DataBase:                                                                                  ┃
            ┃[Database]     : http://breachdbsztfykg2fdaq2gnqnxfsbj5d35byz3yzj73hazydk4vq72qd.onion/    ┃
            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """, Colors.green, interval=0.005)
    wait_for_enter()

def display_databases():
    os.system('clear' if os.name == 'posix' else 'cls')
    Write.Print("""
Voici quelques bases de données accessibles  : 

1. D0xbin : https://gofile.io/d/jQQkKW
2. Orange : https://gofile.io/d/B5T2lu
            https://gofile.io/d/MXVMj1
            https://gofile.io/d/pZq1Ge
                
3.Minecraft : https://gofile.io/d/EggYGD
4. Fivem : https://gofile.io/d/L30IOp 
5. Roblox : https://gofile.io/d/Xop4z0

Ces bases de données peuvent contenir des informations sensibles Donc je ne suis en Aucun Cas Responsable de vos Actes merci .
    """, Colors.green, interval=0.005)
    wait_for_enter()

def display_osint_tools():
    os.system('clear' if os.name == 'posix' else 'cls')
    Write.Print("""
Voici Les Tools D'osint ou les sites 2024  : 

1 - (site) -> https://osintframework.com/
2 - (site) -> https://jfrog.com
3 - (site) -> https://www.maltego.com/

1 - tools (Osint) -> https://github.com/smicallef/spiderfoot
    """, Colors.green, interval=0.005)
    wait_for_enter()

def display_ip_lookup():
    os.system('clear' if os.name == 'posix' else 'cls')
    Write.Print("""
Ip lookup 2024 - > https://www.iplocation.net/

Ip lookup v2 2024 - > https://whois.domaintools.com/
    """, Colors.green, interval=0.005)
    wait_for_enter()

def process_command(command):
    if command == "01":
        display_tool_info()
    elif command == "02":
        display_dark_web_links()
    elif command == "03":
        display_ddos_options()
    elif command == "04":
        dox_create()
    elif command == "05":
        display_databases()
    elif command == "06":
        display_osint_tools()
    elif command == "07":
        display_ip_lookup()
    elif command == "v+":
        current_volume = pygame.mixer.music.get_volume()
        new_volume = min(current_volume + 0.1, 1.0)
        set_volume(new_volume)
        Write.Print(f"Volume augmenté à {int(new_volume * 100)}%.", Colors.green, interval=0.005)
        wait_for_enter()
    elif command == "v-":
        current_volume = pygame.mixer.music.get_volume()
        new_volume = max(current_volume - 0.1, 0.0)
        set_volume(new_volume)
        Write.Print(f"Volume réduit à {int(new_volume * 100)}%.", Colors.green, interval=0.005)
        wait_for_enter()
    elif command == "v0":
        set_volume(0.0)
        Write.Print("Volume désactivé.", Colors.green, interval=0.005)
        wait_for_enter()
    elif command == "v1":
        set_volume(0.1)
        Write.Print(f"Volume rétabli à {int(0.1 * 100)}%.", Colors.green, interval=0.005)
        wait_for_enter()
    else:
        Write.Print("Commande invalide, veuillez réessayer.", Colors.red, interval=0.005)
        wait_for_enter()

if __name__ == "__main__":
    play_music()
    display_intro()
    display_menu_with_title()
    while True:
        command = input("Entrez votre commande : ").strip()
        process_command(command)