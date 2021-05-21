# task : Download the image data from the facecbook
# Facebook Graph Api's

import os 
import requests 

#cwd  = os.getcwd()

url = 'https://graph.facebook.com/{}/picture?type=large'
#data = requests.get(url)

# create the new foldetr to save the images 
os.makedirs('Images_' , exist_ok = True)
storage_path  = os.path.join(os.getcwd() ,'Images_' )
print(storage_path)


for i in range(70,100):
    data =  requests.get(url.format(i))
    with open(storage_path +'/{}_img.jpg'.format(i) , 'wb') as file :
        file.write(data.content)



