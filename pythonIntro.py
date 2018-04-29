print('hello');

#if 3<2:
	#print('condition true');
#else:
	# print('condition false');

# name = 'seetha'

#if name=='kiruba':
	# print('hey Kiruba')
#elif name =='seetha':
	# print('hey seetha')
#else:
	# print('hey yaaruadaaaaaa') 

# volume = 7
# if volume < 20:
   # print("It's kinda quiet.")
#elif 20 <= volume < 40:
   # print("It's nice for background music")
#elif 40 <= volume < 60:
   # print("Perfect, I can hear all the details")
#elif 60 <= volume < 80:
     #print("Nice for parties")
# elif 80 <= volume < 100:
    # print("A bit loud!")
# else:
    # print("My ears are hurting! :(")

#def hi(name):
#	 if name == 'kiruba':
#			print('Hai kiruba')
 #	 else:
 #			print('Hi anonymous!')

#hi('kiruba')


# def hi(name):
 #   if name == 'seetha':
  #      print('Hi seetha!')
  #  elif name == 'kiruba':
  #     print('Hi kiruba!')
  #  else:
   #     print('Hi anonymous!')

# hi('h')


#def hai(sport):
#	if sport == 'cricket':
#		print('like cricket')
#	else:
#		print('dont like others')
#hai('crickett') 


#def sayhai(name):
#	print('hai ' +name)
#sayhai('kiruba')
#
#for nickname in friends:
#	sayhai(nickname)
#	print('next')

#for i in range(1,7):
#	print(i)






#str1 = "this is string example....wow!!!"
#str2 = "exam"
#str3 = "e"

#print(str1.find(str2))
#print(str1.find(str3))


string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:" ,count)

#result = string.index(substring)
#print("Substring index is:", result)


#value = "cat picture is cat picture"

# Start with this value.
location = -1
#location = 0

# Loop while true.
while True:
    # Advance location by 1.
    location = string.find(substring, location + 1)

    # Break if not found.
    if location == -1: break

    # Display result.
    print(location)





#value = "cat picture is cat picture cat picture puli picture"

# Start with this value.
#location = -1

# Loop while true.
#while True:
    # Advance location by 1.
   # location = value.find("picture", location + 1)

    # Break if not found.
   # if location == -1: break

    # Display result.
   # print("location is:",location)





#def get_all_indices(string, substring):
 #    return [index for index in xrange(len(string)) if string[index] == substring]

#print (get_all_indices(string, 5))

#var =  ['1','2','3','4','5','5','4','3','4','2','5']
#unique_entries = set(string)
#indices = { substring : [ i for i, v in enumerate(string) if v == substring ] for substring in unique_entries }
#print(indices)


#var =  ['1','2','3','4','5','5','4','3','4','2','5']
#unique_entries = set(var)
#indices = { value : [ i for i, v in enumerate(var) if v == value ] for value in unique_entries }
#print(indices)


#def getAllindex(list, num):
#     return filter(lambda a: list[a]==num, range(0,len(list)))
 
#a = ['1','2','3','4','5','5','4','3','4','2','5']
#print(getAllindex(a,'5'))
	













