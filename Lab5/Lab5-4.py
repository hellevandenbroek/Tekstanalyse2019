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
    smile => {n, p}
    cough & sneeze => {s}
    coughed & sneezed => {n}
    sleep => {1}
"""

val = nltk.Valuation.fromstring(v)
print(val)

print(('a', 's') in val['like'])
print(('j', 'd') not in val['like'])

g = nltk.Assignment(dom, [('a', 's'), ('j', 'd')])

print(g)

m = nltk.Model(dom, val)

print(m.evaluate('love(angus, dog)', g))

