# %%
s1 = 'Lorem "ipsum" dolor sit amet'
s2 = "Lorem 'ipsum' \ndolor sit amet"

print(s1,s2)

# %%

s3 = '''Lorem ipsum dolor sit amet, 
consectetur adipisicing elit, 
sed do eiusmod'''

print(s3)
# %%
def foo():
    '''
    Function foo print Hello Python.

    Created: 2022-10-29
    Author: Me
    '''
    print('Hello Python')

# %%
foo()
# %%
print( foo.__doc__)
# %%

x = 45.368976

print(f'value of x is {x:.2f}')
# %%
print( s1[4] )
# %%

print( s1[0:5] )
# %%
print( s1[0:20:2])
# %%
print( s1[::-1])


# %%
print('hello'.upper() )
# %%
name = 'Anna'
msg  = 'Hello'

print( msg + ' ' + name + str(10) )

# %%
print('-' * 20)
# %%
