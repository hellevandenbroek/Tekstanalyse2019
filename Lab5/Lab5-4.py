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
    irene => i
    one person => 1
    like => {(a, s), (s, j), (c, a), (c, j), (c, d), (c, n), (c, p), (c, s), (c, b), (c, m), (c, c), (c, i), (c, 1) }
    love => {(a, d), (d, a), (m, p), (b, s)}
    smile => {(n, p)}
    cough_sneeze => {s}
    coughed_sneezed => {n}
    sleep => {1}
"""

val = nltk.Valuation.fromstring(v)
print(val)

print("quick check 1: ", ('a', 's') in val['like'])
print("quick check 2: ", ('j', 'd') not in val['like'])

m = nltk.Model(dom, val)


def assign_g(g_variables):
    return nltk.Assignment(dom, g_variables)


# print("angus, dog: ", m.evaluate('love(angus, dog)', g))

# smile = m.evaluate('exists x.(coughed_sneezed(x) & smile(x, y) & -love(x, y) )', g)
# print("smile:", smile)

# a
ga = assign_g([('x', 'a'), ('y', 'j')])  # angus and julia
ex_a = m.evaluate('exists z.(like(x, z)) & exists z.(like(z, y))', ga)
print("(a): ", ex_a)

# b
gb = assign_g([('x', 'a'), ('y', 'd')])  # angus and dog
ex_b = m.evaluate('love(x, y) & love(y, x)', gb)

print("(b): ", ex_b)

# c
gc = assign_g([('x', 'p')])  # pat
ex_c = m.evaluate('exists z.(-smile(z, x))', gc)
print("(c): ", ex_c)

# d
gd = assign_g([])
ex_d = m.evaluate('exists z.(cough_sneeze(z))', gd)
print("(d): ", ex_d)

# e
ge = assign_g([])
ex_e = m.evaluate('exists z.(-coughed_sneezed(z))', ge)
print("(e): ", ex_e)

# f
gf = assign_g([('x', 'b')])  # bruce
ex_f = m.evaluate('exists z.(love(x, z)) & -love(x, x)', gf)
print('(f): ', ex_f)

# g
gg = assign_g([('x', 'm'), ('y', 'p')])  # matthew and pat
# Nobody other than Matthew loves Pat.
ex_g = m.evaluate('all z.(z != x -> -love(z, y))', gg)
print('(g): ', ex_g)

# h
gh = assign_g([('x', 'c'), ('y', 'i')])  # cyril and irene
# Cyril likes everyone except for Irene.
ex_h = m.evaluate('all z.(z != y -> like(x, z))', gh)
print('(h): ', ex_h)

# i
gi = assign_g([('x', '1')])  # one person
# Exactly one person is asleep.
ex_i = m.evaluate('exists x.(sleep(x) -> -all y.( y != x -> sleep(y)))', gi)
print('(i): ', ex_i)
