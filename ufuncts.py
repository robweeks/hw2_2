import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$") # 3-20 chars upper, lower, numbers, -, and _
PASSWORD_RE = re.compile(r"^.{3,20}$") # anything from 3-20 characters
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

months = [ 'January',
                        'February',
                        'March',
                        'April',
                        'May',
                        'June',
                        'July',
                        'August',
                        'September',
                        'October',
                        'November',
                        'December'
                        ]

escape_codes = {'>': '&gt;',
                '<': '&lt;',
                '"': '&quot;',
                '&': '&amp;'
                }

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
        if month:
                short_month = month[:3].lower()
                return month_abbvs.get(short_month)

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year


def escape_html_rob(s):
    if s:                   
            output_str = ''
            for c in s:
                if c in escape_codes:
                    output_str = output_str + escape_codes[c]
                else:
                    output_str = output_str + c
            return output_str

def escape_html(s):
        return cgi.escape(s, quote = True)



#initialize letters list
LOWER_LETTERS = [chr(x) for x in range(97, 123)];
UPPER_LETTERS = [chr(x) for x in range(65, 91)];

def rot13(sourceString):
    resultString = "";
    for char in sourceString:
        if char.isupper():
            resultString += encrypt(char, UPPER_LETTERS);
        elif char.islower():
            resultString += encrypt(char, LOWER_LETTERS);
        else:
            resultString += char;
    return resultString
            
def encrypt(char, letterList):
    resultchar = '';
    originalIndex = letterList.index(char)
    newIndex = originalIndex + 13
    resultchar += letterList[newIndex % len(letterList)]
    return resultchar
    
       


