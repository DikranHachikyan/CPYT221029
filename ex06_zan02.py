# %%

arr = [12, 34, 56, 67, 89]

print(f'arr={arr} type is {type(arr)}')

# %%

arr[2] = 15

print(f'arr={arr}')
# %%

print(f'id of arr:{id(arr)}')

arr[0] = 120

print(f'id of arr:{id(arr)}')

arr.append(10)

print(f'id of arr:{id(arr)}')

print(f'arr={arr}')

# %%

t = 'Hello'
print(f't={t} id of t:{id(t)}')

t = 'Hello Python'
print(f't={t} id of t:{id(t)}')

# %%

tpl = 100,200,300,400,500

arr = list(tpl)

print(f'arr={arr} type is:{type(arr)}')

# %%

print(300 in arr)

# %%
