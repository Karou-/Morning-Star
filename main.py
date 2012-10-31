#!/usr/bin/python2
import sys, socket, random, string, settings, _ssl, time, urllib

#Constants
HOST=settings.HOST
PORT=settings.PORT
REALNAME=settings.REALNAME
CHAN=settings.CHAN
VERSION=settings.VERSION
NICK=settings.NICK
BOTOWNER=settings.BOTOWNER
IDENT=NICK
OPS=settings.OPS
VOICE=settings.VOICE
PASS=settings.PASS
Site = urllib.urlopen("http://www.google.com").read()
GREETINGS=settings.GREETINGS

#Variables
readbuffer=""                                     # the readbuffer stores all the data the server send to us
#saidHi=False
saidHi=[]

#os.system("TITLE "+VERSION+'  '+CHAN+'@'+HOST)

# here we connect to the irc server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#s=ssl.wrap_socket(s)
s=socket.ssl(s)
s.write("NICK %s\r\n" % NICK)
s.write("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.write ( 'PRIVMSG '+CHAN+' :Hello all!\r\n' )

#Prints different connection info to window if it connects.
print('[+] Connected to '+HOST)
now = time.localtime(time.time())
print time.asctime(now)
print time.strftime("%y/%m/%d %H:%M", now)
s.write ( 'JOIN '+CHAN+'\r\n' )
print('[+] Joined: '+CHAN+'@'+HOST)
now = time.localtime(time.time())
print time.asctime(now)
print time.strftime("%y/%m/%d %H:%M", now)
s.write ( '/msg nickserv identify '+PASS+'\r\n')

while True:
        # The connection holder, prevents the bot form disconnecting
        data = s.read ( 4096 ) #recv (write == send in newer versions)
        #print data
        if data.find ( 'PING' ) != -1:
                s.write ( 'PONG ' + data.split() [ 1 ] + '\r\n' )

# Gets the name of the sender
        getName = data.split("!")
        name = getName[0].split(":")

                # !commands

        if data.find ('!op') != -1 or data.find('JOIN') != -1:
                for i in OPS:
                        if name[1] in i:
                                s.write ( 'MODE '+CHAN+' +o '+i+'\r\n')
                                break
        if data.find ('!voice') != -1 or data.find('JOIN') != -1:
                for i in VOICE:
                        if name[1] in i:
                                s.write ('MODE '+CHAN+' +v '+i+'\r\n')
                                break
        elif data.find ( '!commands' ) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+" : Wana know my commands ey? Well her you go\r\n" )
                s.write ( 'PRIVMSG '+CHAN+" : [1] !quit  [2] !op  [3]!voice  [4]!stats\r\n" )
        elif name[1] == BOTOWNER and data.find ('!quit') != -1:
                s.write ( 'PRIVMSG '+CHAN+' :q.q\r\n' )
                s.write ( 'QUIT\r\n' )
        elif data.find ( '!stats' ) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :So you want my hawt stats aye?\r\n' )
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :'+VERSION+'  '+CHAN+'@'+HOST+'\r\n' )
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :My owner is '+BOTOWNER+'\r\n' )

#
#       Social events
#
        for i in GREETINGS:
                if data.lower().find (i+' '+NICK.lower()) != -1:
                        if name[1] not in saidHi:
                                s.write ( 'PRIVMSG '+CHAN+' :Hello ' + name[1] +'! :)\r\n' )
                                saidHi += [name[1]]
                        else:
                                s.write ( 'PRIVMSG '+CHAN+' :I already said hi...\r\n' )
        if data.find ( 'KICK' ) != -1:
                s.write ( 'JOIN '+CHAN+'\r\n' )
        if data.lower().find ( 'cheese' ) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :Cheese? Where!?\r\n')
        if data.find ( 'kode' ) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :Did I hear someone say Kode?\r\n' )
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :print( "Hello, World!" )\r\n' )
        if data.find ( 'update' ) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+ +Site+ '\r\n' )
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :print( "Hello, World!" )\r\n' )
        if data.find ( 'i want icecream' ) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :Did I hear someone say they want icecream?\r\n' )
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :        )\r\n' )
                s.write ( 'PRIVMSG '+CHAN+' :        C,\r\n' )
                s.write ( 'PRIVMSG '+CHAN+' :       ( ~)\r\n' )
                s.write ( 'PRIVMSG '+CHAN+' :       ( ~)\r\n' )
                s.write ( 'PRIVMSG '+CHAN+' :       (~ )\r\n' )
                s.write ( 'PRIVMSG '+CHAN+' :       \~~/\r\n' )
                s.write ( 'PRIVMSG '+CHAN+' :        \/ \r\n' )
        if data.find ( ':lol'+NICK) != -1:
                time.sleep(1)
                s.write ( 'PRIVMSG '+CHAN+' :'+name[1]+' What you loling at? Not me I hope..\r\n' )

#?
        if data.find ('?say ') != -1:
                time.sleep(1)
                s.write ('PRIVMSG '+CHAN+' :'+data.split('?say ')[1]+'\r\n')
        elif data.find ('?you') != -1:
                time.sleep(1)
                s.write ('PRIVMSG '+CHAN+' : '+settings.RED+' hi you\r\n')
        elif data.find ('?irc') != -1:
                time.sleep(1)
                s.write ('PRIVMSG '+CHAN+' :Please use IRC names in IRC, this can be done by typing part of their name and hitting tab, this also pings the person so they know you\'re referring to them\r\n')
        if data.find ('?gender') != -1:
                time.sleep(1)
                s.write ('PRIVMSG '+CHAN+' : im a dude and i dont plan on changing\r\n')
