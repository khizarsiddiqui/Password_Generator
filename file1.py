import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
digit1=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
digit2=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
sign1=chr(random.randint(128,191)) #Generate a random special character (based on ASCII code)
sign2=chr(random.randint(128,191)) #Generate a random special character (based on ASCII code)

password = uppercaseLetter1 + uppercaseLetter2  + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + sign1 + sign2 
password = shuffle(password)

print(password)












        
