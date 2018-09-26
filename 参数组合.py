# def fn(a,b,c=0,*args,**kwargs):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kwargs=',kwargs)

# # fn(1,2,3,4,e=5) 
# args = (1,2,3,4)
# kwargs = {'e':5}
# fn(*args,**kwargs)

def fn(*args):
    s = max(args)
    return s

print(fn(3,1,6,9))