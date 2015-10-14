# 2015.09.18 21:37:43 EDT
#Embedded file name: /Volumes/Untitled/Excel Parser/unit_tester.py
__author__ = 'pridemai'
import unittest
from parse_functions import BetterCSV

class ParseTestCases(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        self.better_csv=BetterCSV()
        super(ParseTestCases, self).__init__(*args, **kwargs)


    def test_1(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls'])[0]), 11)

    def test_2(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,'])[0]), 12)

    def test_3(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,'])[0]), 13)

    def test_4(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"\",'])[0]), 14)

    def test_5(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,'])[0]), 15)

    def test_6(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"2027M49G01, 2027M69G01\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,data'])[0]), 15)

    def test_7(self):
        self.assertEqual(len(self.better_csv.get_lists(['$(3562.86),\"$174,565.86\",\"as\",,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,data'])[0]), 15)

    def test_8(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\"'])[0]), 19)

    def test_9(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\",,,'])[0]), 22)

    def test_10(self):
        self.assertEqual(len(self.better_csv.get_lists([',,\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\",,,'])[0]), 24)

    def test_11(self):
        self.assertEqual(len(self.better_csv.get_lists(['hello,,\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\",,,'])[0]), 24)

    def test_12(self):
        self.assertEqual(len(self.better_csv.get_lists(['\" $(3,562.86)\",\"$174,565.86\",\"Liming new source\",\"sympathetic, never let it show the way i feel i do \",\"data\",\"fuck\",\"balls\"'])[0]), 7)
    def test_13(self):
        self.assertEqual(len(self.better_csv.get_lists(["\" $(3,562.86)\",\"$174,565.86\",\"Liming new source\",\"sympathetic, never let it show the way i feel i do \",\"data\",\"fuck\",\"balls\""])[0]), 7)
    def test_14(self):
        self.assertEqual(len(self.better_csv.get_lists([",,,,,,,"])[0]), 8)
    def test_15(self):
        self.assertEqual(len(self.better_csv.get_lists(["\n,\n,\n,\n,\n,\n,\n,\n"])[0]), 8)
    def test_16(self):
        self.assertEqual(len(self.better_csv.get_lists(["\r,\r,\r,\r,\r,\r,\r,\r"])[0]), 8)
    def test_17(self):
        self.assertEqual(self.better_csv.search(["2463M43P05","2463M43P05"], ["2463M43P05","2463M43P05"]),True)
    def test_18(self):
        self.assertEqual(self.better_csv.search(["2463M43P05",""], ["2463M43P05-AS02","2463M43P05JEKQ"]),True)
    def test_19(self):
        self.assertEqual(self.better_csv.search(["",""], ["2463M43P05-AS02","2463M43P05JEKQ"]),False)
    def test_20(self):
        self.assertEqual(self.better_csv.search(["2463M43P05",""], ["",""]),False)
    def test_21(self):
        self.assertEqual(self.better_csv.search([" ","2463M43P05"], [" "," "]),False)
    def test_22(self):
        self.assertEqual(self.better_csv.make_parseable("4060T96 P02 (5023T67 / 5023T59 / 1934T24)", {"/": " ", "(":" ",")":" "}), "4060T96 P02  5023T67   5023T59   1934T24 ")
    def test_23(self):
        self.assertEqual(self.better_csv.make_parseable("D191102 (4126T26/4145T05)", {"/": " ", "(":" ",")":" "}), "D191102  4126T26 4145T05 ")
    def test_24(self):

        self.assertAlmostEqual(self.better_csv.find_row("Grand Cherokee",self.better_csv.get_lists(self.better_csv.get_lines( self.better_csv.file_contents_as_string("test_data.csv")))),4)
if __name__ == '__main__':

    unittest.main()

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.09.18 21:37:43 EDT
