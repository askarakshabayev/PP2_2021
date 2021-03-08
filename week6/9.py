# compile(command, 'test', 'exec')

text = 'print(100)\nprint(200)'
x = compile(text, 'test', 'exec')
exec(x)