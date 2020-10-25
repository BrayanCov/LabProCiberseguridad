#!/bin/bash
function pp(){

hostname -I > cosa.txt
curl ifconfig.me >> cosa.txt
echo "" >> cosa.txt
nmap 192.168.1.* >> cosa.txt
nmap -Pn --script vuln $(curl ifconfig.me) >> cosa.txt

}
pp
