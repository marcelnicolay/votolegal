# coding: utf-8
from decimal import Decimal
import re, logging

def generate_slug(texto):

    replaces = [["a","á|à|ã|â|ä"],["e","é|è|ê|ë"],["i","í|ì|î|ï"],["o","ó|ò|õ|ô\ö"],["u","ú|ù|û\ü"],["c","ç"]]
       
    # remove espaco em branco do comeco e final
    string = texto.strip()

    if isinstance(string, str):
        string = unicode(string, 'utf8')

    string = string.lower()
    
    # substitui espaco por -
    string = re.sub('\s', '-', string)
    
    for replace in replaces:
        string = re.sub(unicode(replace[1], 'utf8'), replace[0], string)
    
    # remove caracteres invalidos
    string = re.sub('[^a-z0-9\-]', '', string)

    return string

def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))