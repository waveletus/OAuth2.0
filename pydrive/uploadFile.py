from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authenticationfrom pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance

file1 = drive.CreateFile({'title': 'Hello.txt'}) # Create GoogleDriveFile instance with title 'Hello.txt'
file1.Upload() # Upload it
print 'title: %s, id: %s' % (file1['title'], file1['id']) # title: Hello.txt, id: {{FILE_ID}}

file1['title'] = 'HelloWorld.txt' # Change title of the file
file1.Upload() # Update metadata
print 'title: %s' % file1['title'] # title: HelloWorld.txt

file4 = drive.CreateFile({'title':'appdata.json', 'mimeType':'application/json'})
file4.SetContentString('{"firstname": "John", "lastname": "Smith"}')
file4.Upload() # Upload file
file4.SetContentString('{"firstname": "Claudio", "lastname": "Afshar"}')
file4.Upload() # Update content of the file

file5 = drive.CreateFile()
file5.SetContentFile('girl.jpg') # Read file and set it as a content of this instance.
file5.Upload() # Upload it
print 'title: %s, mimeType: %s' % (file5['title'], file5['mimeType']) # title: cat.png, mimeType: image/png

file6 = drive.CreateFile({'id': file5['id']}) # Initialize GoogleDriveFile instance with file id
file6.GetContentFile('catlove.png') # Download file as 'catlove.png'

file7 = drive.CreateFile({'id': file4['id']}) # Initialize GoogleDriveFile instance with file id
content = file7.GetContentString() # content: '{"firstname": "Claudio", "lastname": "Afshar"}'
file7.SetContentString(content.replace('lastname', 'familyname'))
file7.Upload() # Uploaded content: '{"firstname": "Claudio", "familyname": "Afshar"}'