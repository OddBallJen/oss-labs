# Lab 10 Report
## 8/1/22

### Checkpoint 0 
https://github.com/OddBallJen/oss-labs/wiki/Lab-10-Checkpoint-0

### Checkpoint 1

(I used FireFox) 

![image](https://user-images.githubusercontent.com/57297201/182233301-b0615843-ba32-4e88-ad1a-6fa1e19c6713.png)

### Checkpoint 2

---------
### 1.6.1

![image](https://user-images.githubusercontent.com/57297201/182253227-c340a555-fc84-4836-9f8f-34bbd0a8ab82.png)  

`curl -X GET http://admin:password@127.0.0.1:5984/_all_dbs` getting all dbs:  
![image](https://user-images.githubusercontent.com/57297201/182413049-13c09fd5-9de0-40c2-a2c6-fd6b373609bc.png)

`curl -X PUT http://admin:password@127.0.0.1:5984/oss`:  
![image](https://user-images.githubusercontent.com/57297201/182413266-542d24b7-46fb-4ac6-9d3e-2eb1f18fae4d.png)  

`curl -X PUT http://admin:password@127.0.0.1:5984/oss2` twice:    
![image](https://user-images.githubusercontent.com/57297201/182413496-6fc25a1b-446f-4d67-ac41-339a64414907.png)

`curl -X DELETE http://admin:password@127.0.0.1:5984/oss2`:  
![image](https://user-images.githubusercontent.com/57297201/182414081-6f3ca0de-64e4-4785-b4c1-7c71a91cb97b.png)

### 1.6.2   
logging in:  
![image](https://user-images.githubusercontent.com/57297201/182414509-b88f9eee-2fcc-4768-a077-13b64b30eecf.png)


### 1.6.3
First DB and doc:   

![image](https://user-images.githubusercontent.com/57297201/182415663-0a063da9-8fd6-41d9-a38f-d698f00d864a.png)

### 1.6.4
I created three movie files   
![image](https://user-images.githubusercontent.com/57297201/182416477-d34c2ef8-d345-4888-9b21-b9d1c33a20f0.png)

Then ran query:  
![image](https://user-images.githubusercontent.com/57297201/182419415-63f9de34-3a51-4fe3-915c-fd06c8796bbd.png)

### 1.6.5
Replication:  
![image](https://user-images.githubusercontent.com/57297201/182422016-8377575a-a3f8-4557-be6b-cb3538a73e6d.png)

![image](https://user-images.githubusercontent.com/57297201/182422074-1fd1c21d-a225-47a5-909c-dae9f9f13ead.png)


### Checkpoint 
----------------------------
### 1.7.1
`curl http://127.0.0.1:5984/`   
![image](https://user-images.githubusercontent.com/57297201/182425137-b0626569-1ce7-428a-8d0a-0b844c336631.png)

### 1.7.2

Creating a db called 'album', creating it again (error), and creating backup with -v
![image](https://user-images.githubusercontent.com/57297201/182425532-a2e4926d-133a-4ec4-995d-7312996dbb78.png)


Delete:  
![image](https://user-images.githubusercontent.com/57297201/182426190-2d4cd627-3dd9-42ec-8977-0d029d7c095e.png)

### 1.7.3
Put things in my documents   
![image](https://user-images.githubusercontent.com/57297201/182427029-c350cf16-0717-4e0a-98be-eb825f808969.png)

1.7.3.1 
Revised with no \_rev, then with correct rev. 
![image](https://user-images.githubusercontent.com/57297201/182465020-eca51133-5c35-4927-bc24-f14eda2858a8.png)

1.7.3.2   
Put item but with -v to see details.   
![image](https://user-images.githubusercontent.com/57297201/182466922-774aa95f-815c-445b-b71f-a29dc012e42d.png)

1.7.3.3
I ran the line to put the image in
` curl -vX PUT http://admin:password@127.0.0.1:5984/albums/6e1295ed6c29495e54cc05947f18c8af/artwork.jpg?rev=2-a0ecd0b4133f5d5824078835d510c231 --data-binary @artwork.jpg -H "Content-Type:image/jpg"`  

![image](https://user-images.githubusercontent.com/57297201/182510659-5a2af5fc-4732-4ced-83fc-709cdd735071.png)

![image](https://user-images.githubusercontent.com/57297201/182510711-ea5be1bc-ed0e-4db3-b06e-66802767f3f1.png)

I opened it up on the server   
![image](https://user-images.githubusercontent.com/57297201/182510817-7b869e00-40fa-49ed-84df-d609d42f17f6.png)

![image](https://user-images.githubusercontent.com/57297201/182510863-6899cca6-f637-4917-832f-2ad8fe249fc8.png)


### 1.7.4  
`curl -X PUT http://admin:password@127.0.0.1:5984/albums-replica`

`curl -vX POST http://admin:password@127.0.0.1:5984/_replicate \
     -d '{"source":"http://admin:password@127.0.0.1:5984/albums",\
          "target":"http://admin:password@127.0.0.1:5984/albums-replica"}' \
     -H "Content-Type: application/json"`
     
![image](https://user-images.githubusercontent.com/57297201/182513417-7179f3c1-93c7-4be5-95dc-3a415669cd95.png)


Professor said we don't have to worry about the remote stuff.

### Checkpoint 4

1. 
![image](https://user-images.githubusercontent.com/57297201/182515532-b942d0fe-eb26-4f8e-a52d-b605c9b10147.png)


2.  ![image](https://user-images.githubusercontent.com/57297201/182516058-3738ffbc-d3dc-4b01-83bd-698f2273df31.png)

3.  
![image](https://user-images.githubusercontent.com/57297201/182516188-88f61511-8d55-454c-a804-8b1a9e0bad38.png)


![image](https://user-images.githubusercontent.com/57297201/182516547-8d9d6b09-7b54-4722-b832-ac55450390dd.png)

4.  
![image](https://user-images.githubusercontent.com/57297201/182516634-e3593986-fd98-4dc4-805f-bde253587487.png)










