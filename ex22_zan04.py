
if __name__ == '__main__':
    
    users = ['anna', 'maria', 'markus', 'jorg', 'florian']
    mails = ['anna@no.com', 'maria@no.com', 'markus@no.com', 'jorg@no.com']

    for data in zip(users, mails):
        name, email = data

        print(f'data={data} name= {name} => {email}')
        
    print('---')