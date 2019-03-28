from nltk import sem


read_expr = sem.Expression.fromstring
a = read_expr('P -> not Q')

b = read_expr('P and Q')

c = read_expr('-P -> Q')

d = read_expr('((P or Q) -> R)')

e = read_expr('-(P | R)')

f = read_expr('(P -> -R) <-> (Q -> -S)')

tasks = [a, b, c, d, e, f]




for task in tasks:
    print(task)


