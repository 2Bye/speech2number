# MIT License

# Copyright (c) 2018-2019 Groupe Allo-Media

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Test the ``text_to_num`` library.
"""
from unittest import TestCase
from text_to_num import alpha2digit, text2num


class TestTextToNumFR(TestCase):
    def test_text2num(self):
        test1 = "cinquante trois mille millions deux cent quarante trois mille sept cent vingt quatre"
        self.assertEqual(text2num(test1, "fr"), 53_000_243_724)

        test2 = (
            "cinquante et un million cinq cent soixante dix-huit mille trois cent deux"
        )
        self.assertEqual(text2num(test2, "fr"), 51_578_302)

        test3 = "quatre-vingt cinq"
        self.assertEqual(text2num(test3, "fr"), 85)

        test4 = "quatre-vingt un"
        self.assertEqual(text2num(test4, "fr"), 81)

        self.assertEqual(text2num("quinze", "fr"), 15)
        self.assertEqual(text2num("soixante quinze mille", "fr"), 75000)

    def test_text2num_variants(self):
        self.assertEqual(text2num("quatre-vingt dix-huit", "fr"), 98)
        self.assertEqual(text2num("nonante-huit", "fr"), 98)
        self.assertEqual(text2num("soixante-dix-huit", "fr"), 78)
        self.assertEqual(text2num("septante-huit", "fr"), 78)
        self.assertEqual(text2num("quatre-vingt-huit", "fr"), 88)
        self.assertEqual(text2num("octante-huit", "fr"), 88)
        self.assertEqual(text2num("huitante-huit", "fr"), 88)
        self.assertEqual(text2num("huitante-et-un", "fr"), 81)
        self.assertEqual(text2num("quatre-vingts", "fr"), 80)
        self.assertEqual(text2num("mil neuf cent vingt", "fr"), 1920)

    def test_text2num_centuries(self):
        self.assertEqual(text2num("dix-neuf cent soixante-treize", "fr"), 1973)

    def test_text2num_exc(self):
        self.assertRaises(ValueError, text2num, "mille mille deux cent", "fr")
        self.assertRaises(ValueError, text2num, "soixante quinze cent", "fr")

    def test_text2num_zeroes(self):
        self.assertEqual(text2num("z??ro", "fr"), 0)
        self.assertEqual(text2num("z??ro huit", "fr"), 8)
        self.assertEqual(text2num("z??ro z??ro cent vingt-cinq", "fr"), 125)
        self.assertRaises(ValueError, text2num, "cinq z??ro", "fr")
        self.assertRaises(ValueError, text2num, "cinquante z??ro trois", "fr")
        self.assertRaises(ValueError, text2num, "cinquante trois z??ro", "fr")

    def test_alpha2digit_integers(self):
        source = (
            "Vingt-cinq vaches, douze poulets et cent vingt-cinq kg de pommes de terre."
        )
        expected = "25 vaches, 12 poulets et 125 kg de pommes de terre."
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "Mille deux cent soixante-six clous."
        expected = "1266 clous."
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "Mille deux cents soixante-six clous."
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "Nonante-cinq = quatre-vingt-quinze"
        expected = "95 = 95"
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "Nonante cinq = quatre-vingt quinze"
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "un deux trois quatre vingt quinze"
        expected = "1 2 3 4 20 15"
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "Vingt et un, trente et un."
        expected = "21, 31."
        self.assertEqual(alpha2digit(source, "fr"), expected)

    def test_relaxed(self):
        source = "un deux trois quatre vingt quinze."
        expected = "1 2 3 95."
        self.assertEqual(alpha2digit(source, "fr", relaxed=True), expected)

        source = "Quatre, vingt, quinze, quatre-vingts."
        expected = "4, 20, 15, 80."
        self.assertEqual(alpha2digit(source, "fr", relaxed=True), expected)

        source = "trente-quatre = trente quatre"
        expected = "34 = 34"
        self.assertEqual(alpha2digit(source, "fr"), expected)

    def test_alpha2digit_formal(self):
        source = "plus trente-trois neuf soixante z??ro six douze vingt et un"
        expected = "+33 9 60 06 12 21"
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "z??ro neuf soixante z??ro six douze vingt et un"
        expected = "09 60 06 12 21"
        self.assertEqual(alpha2digit(source, "fr"), expected)

    def test_trente_et_onze(self):
        source = "cinquante soixante trente et onze"
        expected = "50 60 30 11"
        self.assertEqual(alpha2digit(source, "fr"), expected)

    def test_alpha2digit_zero(self):
        source = "treize mille z??ro quatre-vingt-dix"
        expected = "13000 090"
        self.assertEqual(alpha2digit(source, "fr"), expected)
        source = "treize mille z??ro quatre-vingts"
        expected = "13000 080"
        self.assertEqual(alpha2digit(source, "fr"), expected)

        # source = "Votre service est z??ro !"
        # self.assertEqual(alpha2digit(source, "fr"), source)

        self.assertEqual(alpha2digit("z??ro", "fr"), "0")

    def test_alpha2digit_ordinals(self):
        source = (
            "Cinqui??me premier second troisi??me vingt et uni??me centi??me mille deux cent trenti??me."
        )
        expected = "5??me premier second troisi??me 21??me 100??me 1230??me."
        self.assertEqual(alpha2digit(source, "fr"), expected)

    def test_alpha2digit_all_ordinals(self):
        source = (
            "Cinqui??me premier second troisi??me vingt et uni??me centi??me mille deux cent trenti??me."
        )
        expected = "5??me 1er 2nd 3??me 21??me 100??me 1230??me."
        self.assertEqual(alpha2digit(source, "fr", ordinal_threshold=0), expected)

    def test_alpha2digit_decimals(self):
        source = (
            "Douze virgule quatre-vingt dix-neuf, cent vingt virgule z??ro cinq,"
            " un virgule deux cent trente six."
        )
        expected = "12,99, 120,05, 1,236."
        self.assertEqual(alpha2digit(source, "fr"), expected)

        self.assertEqual(
            alpha2digit("la densit?? moyenne est de z??ro virgule cinq.", "fr"),
            "la densit?? moyenne est de 0,5."
        )


    def test_alpha2digit_signed(self):
        source = (
            "Il fait plus vingt degr??s ?? l'int??rieur et moins quinze ?? l'ext??rieur."
        )
        expected = "Il fait +20 degr??s ?? l'int??rieur et -15 ?? l'ext??rieur."
        self.assertEqual(alpha2digit(source, "fr"), expected)

        source = "J'en ai vu au moins trois dans le jardin, et non plus deux."
        expected = "J'en ai vu au moins 3 dans le jardin, et non plus 2."

        self.assertEqual(alpha2digit(source, "fr", signed=False), expected)
        self.assertNotEqual(alpha2digit(source, "fr", signed=True), expected)

    def test_article(self):
        source = (
            "Ne pas confondre un article ou un nom avec un chiffre et inversement : "
            "les uns et les autres ; une suite de chiffres : un, deux, trois !"
        )
        expected = (
            "Ne pas confondre un article ou un nom avec un chiffre et inversement : "
            "les uns et les autres ; une suite de chiffres : 1, 2, 3 !"
        )
        self.assertEqual(alpha2digit(source, "fr"), expected)

    def test_un_pronoun(self):
        source = "Je n'en veux qu'un. J'annonce: le un"
        self.assertEqual(alpha2digit(source, "fr"), source)
