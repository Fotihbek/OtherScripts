from transliterate import to_cyrillic, to_latin

matn = input('Matn kiriting: ')

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))