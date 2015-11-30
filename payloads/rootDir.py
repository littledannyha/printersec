#!/usr/bin/python
# host = raw_input("enter printer IP: ")
urlFile = open('printerURL')
host = urlFile.read().strip()
port = 9100
# text = chr(27) + "%-12345X@PJL RDYMSG DISPLAY=\"" + text + "\"\n"
text = chr(27) + "%-12345X@PJL FSDIRLIST ENTRY=1 COUNT=999999 NAME=\"" +  "0:\\" + "\"\n"
text += "%-12345X" + chr(29)
print text
