a = 5
print(a, id(a))

a += 1
print(a, id(a))  # Здесь изменяется не сам объект, а сама ссылка не него

txt = "Hello world!"
# txt[5] = '_'
print(txt, id(txt))

txt = txt.replace(' ', '_')
print(txt, id(txt))
