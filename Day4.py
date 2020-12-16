import re

"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport.
While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't
actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport
scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same
time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required
fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of
key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the
Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials,
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat
this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not,
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file,
how many passports are valid?
"""


class Passport:
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False

    def is_valid(self) -> int:
        return int(self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid)


def count_valid_passports(filename: str) -> int:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    passport = Passport()
    valid_count = 0
    for line in lines:
        line = line.strip()
        if line == "":
            valid_count += passport.is_valid()
            passport = Passport()
        else:
            if "byr" in line:
                passport.byr = True
            if "iyr" in line:
                passport.iyr = True
            if "eyr" in line:
                passport.eyr = True
            if "hgt" in line:
                passport.hgt = True
            if "hcl" in line:
                passport.hcl = True
            if "ecl" in line:
                passport.ecl = True
            if "pid" in line:
                passport.pid = True
            if "cid" in line:
                passport.cid = True
    return valid_count


"""
--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data 
are getting through. Better add some data validation, quick! 

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for 
automatic validation: 

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules. 
Here are some example values: 

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as 
optional. In your batch file, how many passports are valid? 
"""


class Passport_Strict:
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False

    def set_byr(self, string: str):
        """
        sets the boolean value of byr after checking if it is valid or not (between 1920 and 2002)
        """
        self.byr = int(string) in range(1920, 2003)

    def set_iyr(self, string: str):
        """
        sets the boolean value of iyr after checking if it is valid or not (between 2010 and 2020)
        """
        self.iyr = int(string) in range(2010, 2021)

    def set_eyr(self, string: str):
        """
        sets the boolean value of eyr after checking if it is valid or not (between 2020 and 2030)
        """
        self.eyr = int(string) in range(2020, 2031)

    def set_hgt(self, hgt_value: str):
        """
        sets the boolean value of hgt after checking if it is valid or not (
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.)
        """
        if "cm" in hgt_value:
            self.hgt = int(hgt_value.split("cm")[0]) in range(150, 194)
        elif "in" in hgt_value:
            self.hgt = int(hgt_value.split("in")[0]) in range(59, 77)
        else:
            self.hgt = False

    def set_hcl(self, hcl_value: str):
        """
        sets the boolean value of hcl after checking if it is valid or not (a # followed by exactly six characters
                0-9 or a-f.)
        """
        char_set = re.compile('#[a-f0-9]{6}')
        self.hcl = bool(char_set.search(hcl_value))

    def set_ecl(self, string: str):
        """
        sets the boolean value of eyr after checking if it is valid or not (exactly one of: amb blu brn gry grn hzl oth)
        """
        valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        self.ecl = any(ect in string for ect in valid_ecl)

    def set_pid(self, string: str):
        """
        sets the boolean value of eyr after checking if it is valid or not (a nine-digit number, including leading
            zeroes)
        """
        self.pid = len(string) == 9 and string.isdigit()

    def is_valid(self) -> int:
        return int(self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid)


def count_valid_passports_2(filename: str) -> int:
    """
    Parses the file and creates passport objects for each of them, then sets the different values found in the file
    and counts the number of valid passports
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    passport = Passport_Strict()
    valid_count = 0
    for line in lines:
        line = line.strip()
        if line == "":
            valid_count += passport.is_valid()
            passport = Passport_Strict()
        else:
            attributes = line.strip().split(" ")
            for attribute in attributes:
                attribute = attribute.strip()
                att = attribute.split(":")
                if "byr" == att[0]:
                    passport.set_byr(att[1])
                elif "iyr" == att[0]:
                    passport.set_iyr(att[1])
                elif "eyr" == att[0]:
                    passport.set_eyr(att[1])
                elif "hgt" == att[0]:
                    passport.set_hgt(att[1])
                elif "hcl" == att[0]:
                    passport.set_hcl(att[1])
                elif "ecl" == att[0]:
                    passport.set_ecl(att[1])
                elif "pid" == att[0]:
                    passport.set_pid(att[1])

    return valid_count


if __name__ == '__main__':
    print(count_valid_passports_2("Files/input_Day4.txt"))
