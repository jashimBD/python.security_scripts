#!/usr/bin/env python
# python script using the atbash cipher
import sys

# make dict with ciphertext values

reversed_xyz = {'A': 'Z','B':'Y','C':'X','D':'W', 'E':'V', 'F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'}


def encrypt_msg(msg):
    msg_l = []
    for letter in msg:
        msg_l.append(letter)
    
    for i in range(len(msg_l)):
        
def decrypt_msg(msg):
    pass

encrypt_msg('test')
