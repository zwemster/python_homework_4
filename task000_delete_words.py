text_to_edit = 'Напишите абв программу, легабвко удаляющую из ' \
               'абвсего этого страбвнного текста все абв- слова, содержащие букабвы "абв"'

filtered_list = filter(lambda x: 'абв' not in x, text_to_edit.split(' '))
print(' '.join(list(filtered_list)))