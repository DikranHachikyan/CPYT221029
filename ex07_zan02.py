# %%

conn = dict(
    host='localhost',
    db='northwind',
    port=1521,
    keep_alive=True
)

print(f'conn:{conn} type is:{type(conn)}')

# %%

print(f'host:{conn["host"]}')

# %%

#JSON - JavaScript Object Notation
# 

user = {
    'firstname':'Anna',
    'lastname':'Smith',
    'age': 30,
    'friends':['Jorg', 'Markus']    
}

print(f'name:{user["firstname"]} {user["lastname"]}')

# %%

user1 = [
    'Anna',
    'Smith',
    30,
    ['Jorg', 'Markus']    
]

print(f'user1:{user1}')

# %%

users = [
    {   'firstname':'Anna',
        'lastname':'Smith',
        'age': 30,
        'friends':['Jorg', 'Markus']    
    },
    {   'firstname':'Maria',
        'lastname':'Anderson',
        'age': 25,
        'friends':['Jorg', 'Markus']    
    }
]

print(f'users:{users}')

# %%

print(user.keys())

# %%

print(user.values())

# %%

print(user.items())

# %%

print('age' in user)

# %%

print(user['phone'])

# %%

print(user.get('phone'))
print(user.get('phone','000-00-00'))

# %%
