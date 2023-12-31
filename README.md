# flask-application-jenkins
A repository to demonstrate Flask application deployment using Jenkins in EC2


# 1) Jenkins CI CD pipeline for flask application

a. Update apt-get
  `sudo apt-get update`

b. Install nginx
   `sudo apt-get install nginx`

c.  Curl the Jenkins package
   `curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null`

d. Check if it is signed correctly
   `echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null`

e.  Update apt-get again
   `sudo apt-get update`

f. Install Jenkins on EC2
    `sudo apt-get install Jenkins`

g. Open your port 8080 on Your ec2 instance

h. Check the URL <public-ec2-instance>:8080

i. Create an admin user in our case it's group_one and with pwd zaq1ZAQ!

j. Configure Jenkins. Goto New item in Jenkins Dashboard
    <img width="791" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/06ba967a-2804-47d2-ab56-899879a22f48">

k. Select freestyle project and hit OK. Add your public GitHub repository
    <img width="870" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/7167e3bf-6530-41f5-8e9b-071c3ad04236">

l. Add in SCM
   <img width="867" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/ce1fa5f0-1dea-4b43-b954-528431ec0c9b">

m. Specify a branch from that repo to target
  <img width="840" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/d8bfebfd-0f08-42c8-a5fa-981548c14126">

n. Specify a poll interval, which is a cron job that runs at a particular interval
    <img width="891" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/42453c14-d372-44ea-a5b7-e3bc2cacde06">

o. Add build steps that you wanted to execute
    <img width="848" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/4f735012-91e2-4bb8-a754-d5f6352b9148">

p. Add nginx configuration as below to reverse proxy to the port flask app is running
    
  `location / {
    proxy_pass http://localhost:5000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }`

q. Reload nginx
    `sudo systemctl reload nginx`

r. Setup Alert System using default email

    `Add Post-Build Action:
    Scroll down to the 'Post-build Actions' section.
    Click on Add post-build action.
    Select Editable Email Notification.
    Set Email Recipients:
    Configure recipients for the email notifications`

s. Define Email Content:
    `Define the subject and email body.
    Save the job and hit apply.`
