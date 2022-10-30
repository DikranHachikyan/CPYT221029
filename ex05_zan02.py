# %%

tpl = (4, 5, 10, 2, 11)

print(f'tpl={tpl}, type is {type(tpl)}')

# %%

print(f'first element:{tpl[0]}')

# %%

tpl[2] = 15

# %%

a, b, c, d, e = tpl

print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

# %%

a, b, *_ = tpl

print(f'a={a}, b={b}')

# %%

*_, a, b = tpl

print(f'a={a}, b={b}')

# %%

tpl = 55,77,22,11,44

print(f'tpl={tpl} type is {type(tpl)}')


# %%

t1 = (100,)

print(f't1={t1} type is {type(t1)}')
# %%

print(22 in tpl)

# %%

print( 5 not in tpl)

# %%

print(type(tpl) is tuple)
print(type(tpl) is not int)

# %%
