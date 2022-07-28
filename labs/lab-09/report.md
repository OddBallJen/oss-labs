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






