def fn(name,age,**kw):
    print(name,age,kw)


#fn('老郭',18,sex='man',address='beijing')
d = {'address': 'beijing', 'sex': 'man'}
fn('老郭',18,**d)
