# Lab 08 
## 7/15/22

### Checkpoint 1

![image](https://user-images.githubusercontent.com/57297201/179283830-d3e29f70-e0bf-4025-ae98-e3db744e2cc3.png)

### Checkpoint 2

**Q1:** Find the Nightly and Experimental sections and look at some of the submissions. How can you see what tests were run for a particular submission?

**Ans**: You can click on the numbers for each section under "Test", to see which tests are passed, failed or had not run. 

**Q2:** Find a submission with errors. Can you see what the error condition was? How does this help you debug the failure?

**Ans:**  
![image](https://user-images.githubusercontent.com/57297201/179292364-72d77121-3f32-47c0-8b35-ef62aba6bf88.png)
This is the build I selected. There are four errors. These are the errors: 

![image](https://user-images.githubusercontent.com/57297201/179293371-6a2fb84b-f76a-4424-95c0-2346e971bc04.png)

They help me debug because they tell me what the line number is and they tell me what exactly went wrong, so therefore I can debug the failure with these hints. 

**Q3:** Find a system that is close to your specific configuration in the Nightly, Nightly Expected or one of the Masters sections. How clean is the dashboard? Are there any errors that you need to be concerned with?

**Ans:**  
[https://open.cdash.org/build/8040502](https://open.cdash.org/build/8041105)
They are also running Ubuntu 20 on Windows

![image](https://user-images.githubusercontent.com/57297201/179313177-e9efadbb-a677-4b46-bcfb-2926a22a9ad0.png)
I had an error that is Curl (test 25) , which they also had above, I also had test 26 not run. There is two errors on mine and three above. 

![image](https://user-images.githubusercontent.com/57297201/179313372-9cf46cfb-f85a-4590-8935-b0438c328545.png)
These are my passed tests. 

### Checkpoint 3

For Test 25, the information of the failure provided is that 

For test 26, the information of the failure provided is that the file is missing. 

-vv is very verbose, which displays all error information including the input and outputs. 

![image](https://user-images.githubusercontent.com/57297201/179314393-0884eb1f-02eb-4b75-a519-eb9548cef898.png)
![image](https://user-images.githubusercontent.com/57297201/179314716-337656cd-e009-48b9-8dab-fc2f0af679a5.png)
These are my errors 

### Checkpoint 4

