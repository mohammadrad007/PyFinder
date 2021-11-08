from requests import get
from os import system
from colorama import Fore, init

system('cls' or 'clear')
init()

print(Fore.LIGHTRED_EX + """
            ****** ═════════    § Sasa SocialMedia Finder §    ═════════ ******
           
                         ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
                         ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
                         █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
                         ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
                         ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
                         ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
    """)
print(Fore.LIGHTYELLOW_EX +
      """                    𝕊𝔸𝕊𝔸                      """)
print(
    Fore.LIGHTBLUE_EX +
    """                                                                                ──╮
            ===========━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━============    
            **            WebSite : programmingwithrad.netlify.com            **
            **                  Channel : @researcher_of_islam                **
            **                       Developers : Writer                      **
            **                     Team Members : Just me                     **
            **                  Thank's : .:: TopLearn.com ::.                **
            ===========━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━============
         ╰──
                                              """)

username = input('                               ▲ Username : ')

sites = [
    "http://www.aparat.com", "http://www.github.com",
    "http://www.instagram.com", "http://www.google.com"
]

for site in sites:
    url = site + '/' + username
    response = get(url)
    if response.status_code == 200:
        print(Fore.GREEN + '                        [ツ] 👨' + username +
              ' Found In: 📡 ' + site)
    elif response.status_code == 404:
        print(Fore.RED + '                        [ϡ ] 👨' + username +
              ' Not Found In: 📡 ' + site)
    else:
        print("Unknow Error ! | ERROR CODE : {}".format(response.status_code))
