from unittest import TestCase

from main import zasifrovani, rozsifrovani

class Test(TestCase):
#Text do morseovky
    def test_Text_do_morseovky_SOS(self):
        self.assertEqual(zasifrovani("SOS"),"... --- ... ","OK")

    def test_Text_do_morseovky_123(self):
        self.assertEqual(zasifrovani("123"),".---- ..--- ...-- ","OK")

    def test_Text_do_morseovky_znaky(self):
        self.assertEqual(zasifrovani("?.()"),"..--.. .-.-.- -.--. -.--.- ","OK")

    def test_Text_do_morseovky_veta(self):
        self.assertEqual(zasifrovani("Ahoj, jak se mas?"),".- .... --- .--- --..--  .--- .- -.-  ... .  -- .- ... ..--.. ","OK")

#Morseovka do textu
    def test_Morseovka_do_textu_SOS(self):
        self.assertEqual(rozsifrovani("... --- ... "),"SOS ","OK")

    def test_Morseovka_do_textu_456(self):
        self.assertEqual(rozsifrovani("....- ..... -.... "),"456 ","OK")

    def test_Morseovka_do_textu_znaky(self):
        self.assertEqual(rozsifrovani("..--.. -....- -..-. .-.-.- -.--. "),"?-/.( ","OK")

    def test_Morseovka_do_textu_veta(self):
        self.assertEqual(rozsifrovani("-.. --- -... .-. -.--  -.. . -. --..--  .--- .- -.-  ... .  -- .- - . ..--.. "),"DOBRY DEN, JAK SE MATE? ","OK")



