from bs4 import BeautifulSoup
import requests

url = "https://ioepas.edu.np/"

#Get HTML Content
response = requests.get(url)
soap = BeautifulSoup(response.text, "html.parser")

#Parse HTML Content


#Find IMG Tags
image_tags = soap.find_all("img")

'''
URl ma bhako k k image tag cha sab lai list ma rakhcha image_tags ma
soap.find_all() le kunai pani tag given url ma bhako sab dincha

'''

#Image Source
i=1
for img_tag in image_tags:
    image_source_link = img_tag['src']
    
    if image_source_link.startswith("http"):
    
        print(f" IMAGE SOURCE LINK : {image_source_link} ")


        image_data = requests.get(image_source_link).content
        
        with open(f"images/image_{i}.jpg","wb") as file:
            file.write(image_data)
        i+=1


#Image Content Fetch


#File System write