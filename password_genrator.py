import random
import string
# bag_of_char = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(i for i in range(10))
bag_of_printable = list(string.printable) 

password_length = 8 
password =''.join(random.sample(bag_of_printable,password_length)
 
print('Generated password : {}'.format(password)))