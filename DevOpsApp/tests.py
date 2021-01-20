from django.test import TestCase
from DevOpsApp.challs.scripts import *
# Create your tests here.
class CryptoTest(TestCase):
    def test(self):
        key='ICCN'
        plaintext='Groupe 1'
        shift=3
        self.assertEqual(encryptcesar(shift, plaintext), 'Jurxsh 1') #cesar
        self.assertEqual(encryptSub(key, plaintext), 'roGue#p1') #homophonic
        self.assertEqual(vignere(txt=plaintext, key=key, typ='e'), 'p63D:)C_') #vigenere
