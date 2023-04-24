import numpy as np
filename='state_names.txt'
data=np.loadtxt(filename, delimiter=',', dtype=str)
print('There are ',len(data),' lines in input file')
for x in data:
  for y in data:
    if (x!=y):
      for z in data:
        if (x!=y):
          if (x!=z):
            if (y!=z):
              word=y.lower()+z.lower()
              #result of the find must be less than length of y to ensure target string is found across both sources
              #sum of the result of the find and the length of y must also exceed the length of y to ensure target string is found across both sources
              if 1 <= word.find(x.lower()) <= len(y) and word.find(x.lower())+len(x) > len(y):
                print('Concatenation of ',y.lower(),' and ',z.lower(), 'finds ',x.lower(),' at position ',word.find(x.lower()))
#,' whilst length of first source string is ',len(y),' and length of target is ',len(x))
#                print('length of x:',len(x))
#                print('length of y:',len(y))
#                print('posn of find:',word.find(x.lower()))
#                print('posn of find + length of target:',word.find(x.lower())+len(x))
#word = 'geeks for geeks'
#print(word.find('for'))
#word = 'geeks for geeks'
#
## returns first occurrence of Substring
#result = word.find('geeks')
#print("Substring 'geeks' found at index:", result)
#
#result = word.find('for')
#print("Substring 'for ' found at index:", result)
#
## How to use find()
#if word.find('pawan') != -1:
#	print("Contains given substring ")
#else:
#	print("Doesn't contains given substring")
#word = 'geeks for geeks'

## Substring is searched in 'eks for geeks'
#print(word.find('ge', 2))

## Substring is searched in 'eks for geeks'
#print(word.find('geeks ', 2))

## Substring is searched in 's for g'
#print(word.find('g', 4, 10))

## Substring is searched in 's for g'
#print(word.find('for ', 4, 11))

#main_string = "Hello, hello, Hello, HELLO! , hello"
#sub_string = "hello"
#count_er=0
#start_index=0
#for i in range(len(main_string)):
#  j = main_string.find(sub_string,start_index)
#  if(j!=-1):
#    start_index = j+1
#    count_er+=1
#print("Total occurrences are: ", count_er)
#
#string = "freeCodeCamp"
#print(string[0:5])
