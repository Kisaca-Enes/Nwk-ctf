import os
import time
import curses

def execute_command(command, stdscr):
    stdscr.clear()
    stdscr.border()
    command = command.lower()
    output = ""

    if "nmap" in command:
        output = """
# Nmap scan report
PORT     STATE SERVICE      VERSION
21/tcp   open  ftp          vsftpd 3.0.3
22/tcp   open  ssh          OpenSSH 8.2p1
445/tcp  open  smb          Windows 10 Pro
80/tcp   open  http         Apache httpd 2.4.41 (Ubuntu)
Filtered ports detected. Firewall olabilir!
"""
    elif "nmap -f" in command:
        output = "Firewall bypass edildi! Yeni açık portlar:\n - 3306/tcp (MySQL)\n - 6379/tcp (Redis)"
    elif "ftp" in command:
        output = "FTP sunucusuna bağlanıldı. Anonim giriş mümkün! Dosyalar listeleniyor:\n - backup.tar.gz\n - config.txt"
    elif "cat config.txt" in command:
        output = "MySQL Kullanıcı: admin\nMySQL Şifre: 123456"
    elif "mysql" in command:
        output = "MySQL sunucusuna giriş yapıldı. Kullanıcı tabloları:\n - users\n - transactions"
    elif "select * from users" in command:
        output = "| ID | Kullanıcı | Şifre   |\n|----|----------|--------|\n| 1  | root     | root123 |\n| 2  | ali      | Ali123  |"
    elif "nikto" in command:
        output = "Web sunucusunda LFI açığı tespit edildi!\nExploit: http://1.0.1.0.1/index.php?page=../../../../etc/passwd"
    elif "http://1.0.1.0.1/index.php?page=../../../../etc/passwd" in command:
        output = "root:x:0:0:root:/root:/bin/bash\nali:x:1000:1000:Ali:/home/ali:/bin/bash"
    elif "ssh ali@1.0.1.0.1" in command:
        output = "Ali kullanıcısı ile SSH bağlantısı sağlandı. Parola: Ali123"
    elif "uname -a" in command:
        output = "Linux target 4.15.0-20-generic #21-Ubuntu x86_64 GNU/Linux"
    elif "cat /proc/kallsyms | grep prepare_kernel_cred" in command:
        output = "ffffffff810a1420 T prepare_kernel_cred"
    elif "cat /proc/kallsyms | grep commit_creds" in command:
        output = "ffffffff810a10e0 T commit_creds"
    elif "gcc exploit.c -o exploit" in command:
        output = "Exploit derlendi. ./exploit komutunu çalıştırarak root olun."
    elif "./exploit" in command:
        output = "[+] Stack overflow başarıyla tetiklendi!\n[+] Kernel exploit çalıştırılıyor...\n[+] Root erişimi sağlandı!\nFlag: FLAG{kernel_exploit_success}"
    elif "exit" in command:
        exit()
    else:
        output = "Bilinmeyen komut."

    height, width = stdscr.getmaxyx()
    stdscr.addstr(2, 2, f"[ {command} Çıktısı ]", curses.A_BOLD)
    stdscr.addstr(4, 2, output)
    stdscr.addstr(height - 2, 2, "Komut bekleniyor...")
    stdscr.refresh()
    time.sleep(2)

def hacker_terminal(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    stdscr.border()
    ascii_banner = """
██╗  ██╗ █████╗ ██╗     ██╗     
██║ ██╔╝██╔══██╗██║     ██║     
█████╔╝ ███████║██║     ██║     
██╔═██╗ ██╔══██║██║     ██║     
██║  ██╗██║  ██║███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
CTF Terminal Emulator
"""
    stdscr.addstr(1, 2, ascii_banner, curses.A_BOLD)
    stdscr.refresh()

    while True:
        stdscr.addstr(10, 2, "┌──(root@ctf)-[~]")
        stdscr.addstr(11, 2, "└─# ")
        stdscr.refresh()
        curses.echo()
        command = stdscr.getstr(11, 5, 1000).decode("utf-8").strip()
        curses.noecho()
        execute_command(command, stdscr)

if __name__ == "__main__":
    curses.wrapper(hacker_terminal)
