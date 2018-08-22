
lalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = 7
print('Enter your message')
message = input()
newmessage = ''
newdemessage = ''
print('')

for letter in message:
  count = 0
  for item in lalphabet:
    if item == letter or item.upper() == letter:
      if count > 18:
        newcount = count + key - 26
        newletter = lalphabet[newcount]
      else:
        newletter = lalphabet[count + key]
      break
    count = count + 1
  else:
    newletter = letter
  newmessage = newmessage + newletter

for letter in message:
  count = 0
  for item in lalphabet:
    if item == letter or item.upper() == letter:
      if count < 6:
        newcount = count - key + 26
        newletter = lalphabet[newcount]
      else:
        #print(count)
        newletter = lalphabet[count - key]
      break
    count = count + 1
  else:
    newletter = letter
  newdemessage = newdemessage + newletter

print('your encrypted message is:')
print(newmessage) 

print('')

print('your decrypted message is:')
print(newdemessage) 
