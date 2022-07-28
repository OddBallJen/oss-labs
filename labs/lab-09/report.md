# OSS Lab 9
## 7/25/22

## Example 0


![image](https://user-images.githubusercontent.com/57297201/181395149-03a74e29-0673-4fe0-a297-e3c2be9e6841.png)


## Example 1

I installed vim and created a file in root
![image](https://user-images.githubusercontent.com/57297201/181397139-ccd66c70-036a-4a9e-89de-6b8ed0b80de6.png)

![image](https://user-images.githubusercontent.com/57297201/181397161-91ce5519-edaa-4c13-ba4c-6df7a6fbe9e5.png)


I also installed cowsay 

![image](https://user-images.githubusercontent.com/57297201/181397663-bcae74b3-aee9-4900-b31e-0b87bd544912.png)


## Example 2

I ran the commands 

`docker run --name db -d mongo:3.2 mongod --smallfiles`

and 

`docker run --name rocketchat -p 3000:3000 --env ROOT_URL=http://localhost --link db:db -d rocket.chat:0.62`

and this is on my `localhost:3000`  
![image](https://user-images.githubusercontent.com/57297201/181398195-425c6e75-a626-4de4-a718-f25f937a6c40.png)

## Example03

I created and edited the dockerfile, then ran   
`  docker build -t python_hello .`   
then 
`docker run -p 5000:5000 python_hello`

![image](https://user-images.githubusercontent.com/57297201/181400432-933dfe69-10f4-4d7e-b842-58679cad85e1.png)


on my `localhost:5000`   
![image](https://user-images.githubusercontent.com/57297201/181400372-14a889b1-59fe-450e-b969-54adbd944887.png)


## Example 04

I created a Dockerfile and typed in the things. 

When I tried to run the first command it broke my computer. I am sure I am on the right branch. I shall try again. 

I tried running it and this error popped up

![image](https://user-images.githubusercontent.com/57297201/181406854-79abac16-c2d0-4088-972f-acb78133b1ce.png)


so I added a .dockerignore file in the directory of messageApp and added the following

`
./log
./tmp
.git
*Dockerfile*
*docker-compose*
node_modules
`
And it ran successfully! 

This is docker images  
![image](https://user-images.githubusercontent.com/57297201/181407101-89a3b607-d901-4c5a-b9b2-8a2eaa0fcb9c.png)

` docker run message-app ` failed as indicated in the example. 

So I created the .yml file
And ran the compose build and ran it. 

![image](https://user-images.githubusercontent.com/57297201/181407828-4e9ec806-fd06-412e-80a0-84db67d1d8d9.png)
there's a boat!

` curl http://localhost:1337/message `

![image](https://user-images.githubusercontent.com/57297201/181408065-1dea6f59-4967-4a15-9ad0-a563d07bca3d.png)

after adding the messages:  
![image](https://user-images.githubusercontent.com/57297201/181408257-8c443f18-be85-441c-bad5-c26871a32a0e.png)

When I tried to edit the messages I got this error:
![image](https://user-images.githubusercontent.com/57297201/181408407-10463261-71a5-44fb-88ad-def896198fad.png)
so I ran the following instead
![image](https://user-images.githubusercontent.com/57297201/181408779-64b9da43-dc29-45a2-8720-d2fe36648b8f.png)

![image](https://user-images.githubusercontent.com/57297201/181409148-a42cfeab-2cdd-445f-ac20-84d9335f2f53.png)

After running delete:  

![image](https://user-images.githubusercontent.com/57297201/181409230-72217f46-85e7-4937-87d7-cb4797243ada.png)



