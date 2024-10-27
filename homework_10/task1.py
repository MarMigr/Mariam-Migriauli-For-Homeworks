def vowel_count(text):
    vowel = 'a,A,e,E,i,I,o,O,u,U,y,Y'
    return sum(text.count(i) for i in vowel)


text='Mariam Migriauli'

print(vowel_count(text))


text='abrakadabra'

print(vowel_count(text))


text='mwvrtneli'

print(vowel_count(text))