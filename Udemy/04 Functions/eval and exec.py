# eval and exec do the same thing but differ slightly

#eval is used on simple single line code

#exec is used on more complex multi line code


print(eval("print('Hello')"))


me = ''' print ('Hello friend')

print ('My name is david')

print ('I am 23 years old') '''

print (exec('me'))
