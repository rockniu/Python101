#import os
#print os.name

#------Test Number List-------------
num_list=[1, 2, 3, 4]
print ('Len of number list=', len(num_list))
num_list.extend((5,6))
print ('Len of number list after extend with tuple=', len(num_list))
i=7
while(i<=100):
    num_list.append(i)
    i=i+1

print ('Len of number list after loop=', len(num_list))

num_list =range(10)
print ('Len of number list after range=', len(num_list))


#-----Test String List------------
str_list=['rock' ,'niu', 'jack', 'wu', 'niu']
len(str_list)
str_list.append('jack')
str_list.remove('niu')
rock_idx = str_list.index('rock')
print ('index of rock in list=' + str(rock_idx))
str_list.insert(0, 'HGG')
rock_idx = str_list.index('rock')
print ('index of rock in list=' + str(rock_idx))

print ('count of jack=' + str(str_list.count('jack')))

