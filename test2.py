"""Chapter 6 onwards assignment

6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.



text = "X-DSPAM-Confidence:    0.8475"
a= text.find('0.8475') # trying to find index value 
b= (text [a:]) # extracting value at the end of the line
c= float (b) # converting to floating point number
print (c)

-----------------------------------------------------------

7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.


fname= input('Please enter file name:')
ofile= open (fname)

for line in ofile:
    aline= line.rstrip()# removes the new line space
    nline= aline.upper()# converts all characters to upper
    print(nline)
    
----------------------------------------------------------

7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

Average spam confidence: 0.7507185185185187


fname= input ('Please enter file name:')
ofile= open (fname)
total=0
count= 0

for line in ofile:# reading the file 
    if not line.startswith('X-DSPAM-Confidence: '):
        continue # go to next iteration
        
    count= count + 1
    fvalue= line.find('0.') #finds the index of floting value
    x= line[fvalue:]# extracts the floating point values
    y= float(x) # convert string value to floating number
    total= total + y
    
avg= total/count
print('Average spam confidence:',avg)
------------------------------------------------------------
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

Output:
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']


ofile= open('romeo.txt')
nlist=[]

for line in ofile: #read line by line
    slist= line.split() #spliting the line

    for word in slist: #scanning each word in a line
        if word in nlist:
            continue       #checks if word is already in list
        nlist.append(word) #if not then appends and then sorts
        nlist.sort()
            
print(nlist)
--------------------------------------------------------------

8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.


ofile= open('mbox-short.txt')
count=0

for line in ofile:
    if not line.startswith('From '): # if line does not start with "From" then skip iteration
        continue
    sline= line.split() # parsing the From line
    print (sline[1])
    count= count + 1

print("There were", count, "lines in the file with From as the first word")
----------------------------------------------------------------------------------------------
 
 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Desired Output
cwen@iupui.edu 5
 
   
ofile= open('mbox-short.txt')#read through the mbox-short.txt 
ndic= dict()

for line in ofile:
    if not line.startswith('From '): # if line does not start with "From" then skip iteration
        continue
    x= line.split() #parsing lines to words
    sender= x[1] #takes the second word of those lines as the person who sent the mail
    
    ndic[sender]=ndic.get(sender,0)+1 #scanning each sender name and the count of occurance into a dictionary. Creating a histogram.

bigsender=None
bigcount= None
for sender, count in ndic.items():#reads through the dictionary using a maximum loop to find the most prolific committer
    if bigcount is None or count> bigcount:
        bigcount= count
        bigsender= sender
        
print (bigsender, bigcount)
---------------------------------------------------------------------------------------------
 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
 
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
 


ofile= open ('mbox-short.txt')
lhour=list() 

for line in ofile:
    if not line.startswith('From '): #skips line not starting with 'From '
        continue
    else:
        x= line.split()# splitting line into words
        y= x[5] #extacting time from the line
        z= y.split(':') #splitting time by colon
        hrs= z[0] #extracting hour from time
         
        lhour.append(hrs) #appending all hrs to lhour list
        
        
# creating histogram of hours and its count
dhour= dict()
for i in lhour:
    dhour[i]= dhour.get(i,0)+1


    
#Printing dictionary in ordered format
for k, v in sorted(dhour.items()): #sorted function sorts the keys in the dictionary
    print(k,v)
    
11: You will extract all the numbers in the file and compute the sum of the numbers.
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.


import re

ofile= open('regex_sum_1869544.txt') 
nlist= list()
count=0

for line in ofile: #reads line in file
    line=line.rstrip()
    num= re.findall('[0-9]+', line) #logic to extract numbers in line
    if len(num) < 1: continue #lines without numbers are ignored
    
    for i in num: #scanning through numb list  
        x= int(i) #converting the extracted list strings to integers
        nlist.append(x) #making list of all integer values
        count= count+1
    

print(nlist)
print('Count:', count)
print('Sum:', sum(nlist))
--------------------------------------------------------------------------------------------------
 
 Chapter 12: python and webpage
    
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close() 
    
-----------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))# checks if url is present, if not then it reurns None
    print('Contents:', tag.contents[0])# gets the content in bw tag
    print('Attrs:', tag.attrs) # gets the attribute of the tag

-------------------------------------------------------------------------

You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
Sample Execution

$ python3 solution.py
Enter - http://py4e-data.dr-chuck.net/comments_42.html
Count 50
Sum 2...
     

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_name = "http://py4e-data.dr-chuck.net/comments_1869546.html" #url to open
html = urlopen (url_name, context=ctx).read()
soup = BeautifulSoup(html, "html.parser") #parsing html data into clean format

span_value= list()
tags = soup('span') #slicing only for span tags and its content

for tag in tags:
    x = tag.contents[0] #gets the value in the span tag
    y= int(x) #converting into int so we can add the valie in list later
    span_value.append(y)

print (sum(span_value))
 -------------------------------------------------------------------------------------
 
 The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
 
  
        
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_name = input ('Enter URL: ') #url to open
#url_name= 'http://py4e-data.dr-chuck.net/known_by_Colette.html'
count= input ('Enter count: ')
position= input ('Enter position: ')

c= int(count)
p= int(position)
x= 0 


while x < c+1: #this while repeats the number of counts that user enters
    print ('Retriving:', url_name) 
    html = urlopen (url_name, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser") #parsing html data into clean format
    tags = soup('a') #slicing only for span tags and its content
    nlist = list(tags)
    olist = list() # creating a list of url only
    
    for i in nlist[p-1:p]: #this loop gets the urlname in position as entered by user
        url = i.get('href', None) #extract the href values from the anchor tags
        olist.append(url)
        url_name= url
        
    x = x+1
    
    ------------------------------------------------------------------------------------------
    
   XML ASSIGNMENT
    
   In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
   You are to look through all the <comment> tags and find the <count> values sum the numbers. 
   
   counts = tree.findall('.//count')
   https://py4e-data.dr-chuck.net/comments_42.xml
   
   Sum=2553
   
   Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
   Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
   Retrieved 4189 characters
   Count: 50
   Sum: 2...
  



from urllib.request import urlopen
import xml.etree.ElementTree as ET #will help us parse the response.
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address= input ('Enter location: ')
#address= 'https://py4e-data.dr-chuck.net/comments_42.xml'
#https://py4e-data.dr-chuck.net/comments_1869548.xml
print ('Retrieving http:', address) 

data = urlopen (address, context=ctx).read() # opens the url
print('Retrieved', len(data), 'characters')
  
    
tree = ET.fromstring(data) #parses into tree format
lst = tree.findall('comments/comment') #get only elements under comment tag
count=0
total=0


for i in lst:
    x= i.find ('count').text
    count += 1
    y= int(x)
    total= total+y
   
    
print ('Count:', count)
print ('Sum:', total)

-------------------------------------------------------------------
JSON ASSIGNMENT

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...



import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

user_url= input('Enter location:')
print ('Retrieving', user_url)
#'https://py4e-data.dr-chuck.net/comments_42.json'
#https://py4e-data.dr-chuck.net/comments_1869549.json


ourl = urllib.request.urlopen (user_url, context=ctx) # opens the url
rurl = ourl.read().decode() #reads JSON data from url and decode from UTF-8 to unicode
print ('Retrieved', len(rurl), 'characters') 
#print (rurl) #prints data and it will be formatted

data= json.loads(rurl)#parses the JSON data and will get back an object
#print (data) # prints data which hold a dictionary of JSON data
#y= json.dumps(rurl)

x=0 #var used to iterate through comments 
nlist= [] #list to hold count values

for i in data['comments']: #extract the comment only from the JSON data
    c= data['comments'][x]['count'] #extract counts from the comment dic
    x= x+1
    nlist.append(c)
    
print ('Count:', x)
print ('Sum:',sum(nlist))
--------------------------------------------------------------------------

JSON using API assignment

The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 3073 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key=42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else: 
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    
while True: 
  
    location = input ('Enter location: ')
    #'South Federal University'
    if len(location) < 1 : break 

    ndic = dict()
    ndic['address']= location # "location" is set as value for "address" key
    if api_key is not False:
        ndic['key']= api_key # additional key value pait to ndic dictionary
    url = serviceurl + urllib.parse.urlencode(ndic) #creating a full url by appending location value to the end. 

    print ('Retrieving', url)
    ourl = urllib.request.urlopen (url, context=ctx) #contact a web service and retrieve JSON for the web service and parse that data
    data = ourl.read().decode() #reading JSON data and decoding it to unicode
    print ('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)#parsing JSON data
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print ('======FAILED========')
        continue
    
    #print (json.dumps(js, indent=4)) #formats output 
    
    
    place_id= js['results'][0]['place_id'] #retriving the first place_id 
    print ('Place id', place_id)
--------------------------------------------------------------------    
"""    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_name = input ('Enter URL: ') #url to open
#url_name= 'http://py4e-data.dr-chuck.net/known_by_Colette.html'
count= input ('Enter count: ')
position= input ('Enter position: ')

c= int(count)
p= int(position)
x= 0 


while x < c+1: #this while repeats the number of counts that user enters
    print ('Retriving:', url_name) 
    html = urlopen (url_name, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser") #parsing html data into clean format
    tags = soup('a') #slicing only for span tags and its content
    nlist = list(tags)
    olist = list() # creating a list of url only
    
    for i in nlist[p-1:p]: #this loop gets the urlname in position as entered by user
        url = i.get('href', None) #extract the href values from the anchor tags
        olist.append(url)
        url_name= url
        
    x = x+1
    