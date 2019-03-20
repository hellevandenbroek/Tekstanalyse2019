'''Exercise 3 (Nltk-Predicates) Translate the following sentences into predicate-argument formula of
first order logic.
(a) Angus likes Cyril and Irene hates Cyril.
(b) Tofu is taller than Bertie.
(c) Bruce loves himself and Pat does too.
(d) Cyril saw Bertie, but Angus didnt.
(e) Cyril is a fourlegged friend.
(f) Tofu and Olive are near eachother
'''

from nltk import sem

read_expr = sem.Expression.fromstring

a = read_expr('like(angus,cyril) & hate(irene,cyril)')

b = read_expr('taller(tofu,bertie)')

c = read_expr('loves(bruce,bruce) & loves(pat,pat)')

d = read_expr('saw(cyril,bertie) & -saw(angus,bertie)')

e = read_expr('fourleggedfriend(cyril)')

f = read_expr('near(tofu,olive) & near(olive,tofu)')

tasks = [a, b, c, d, e, f]

for task in tasks:
    print(task)

