import nltk


dom = {'a', 'j', 'd', 'n', 'p', 's', 'b', 'm', 'c', 'i', '1'}


v = """
    angus => a
    julia => j
    dog => d
    nobody => n
    pat => p
    somebody => s
    bruce => b
    matthew => m
    cyril => c
    one person => 1
    like => {(a, s), (s, j), -(c, i)}
    love => {(a, d), (d, a), (m, p)}
    smile => {(n, p)}
    cough_sneeze => {s}
    coughed_sneezed => {n}
    sleep => {1}
"""

val = nltk.Valuation.fromstring(v)
print(val)

print(('a', 's') in val['like'])
print(('j', 'd') not in val['like'])

g_variables = [('x', 'n'), ('y', 'p')]  # nobody and pat

g = nltk.Assignment(dom, g_variables)

print("g: ", g)

m = nltk.Model(dom, val)

print("angus, dog: ", m.evaluate('love(angus, dog)', g))

smile = m.evaluate('exists x.(coughed_sneezed(x) & smile(x, y))', g)
print("smile:", smile)