""" emojize task """
# importing libraries
import requests
from emoji import emojize

uprompt = input()
words = uprompt.split()
reply = []
for word in words:
    if word[-1] == '?' and word[-2] == ':':
       reply.append(emojize(word[:-1]+'?', language='alias'))
    elif word[0] == ':' and word[-1] == ':':
       reply.append(emojize(word, language='alias'))
    else:
       reply.append(word)

replyfinal = ' '.join(reply)

print(replyfinal)

