file = input("What's the name of the file? ")
file = file.strip().lower()
if file[-4:] == '.gif':
    print('image/gif')
elif file[-4:] == '.jpg' or file[-5:] == '.jpeg':
    print('image/jpeg')
elif file[-4:] == '.png':
    print('image/png')
elif file[-4:] == '.pdf':
    print('application/pdf')
elif file[-4:] == '.txt':
    print('text/plain')
elif file[-4:] == '.zip':
    print('application/zip')
else:
    print('application/octet-stream')


