import os
file = open( "Cmaxima_v1.1.chr（西葫芦版本）.txt", "r",encoding='utf-8')
#file_add = open("try.txt","r",encoding='utf-8')
content = file.read()
#content_add = file_add.read()
pos = content.find( ">Cmo_Chr07")#将不同编号基因进行分割
t=content.find( ">Cmo_Chr08")
if pos != -1:
    content = content[pos:t+1]
file = open( "Cmo_9.txt", "w" )
file.write( content )
file.close()
#file_add.close()