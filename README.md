# flask-application-jenkins
A repository to demonstrate Flask application deployment using Jenkins in EC2


# Steps for installation

1. Update apt-get
  `sudo apt-get update`

2. Install nginx
   `sudo apt-get install nginx`

3.  Curl the Jenkins package
   `curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null`

4. Check if it is signed correctly
   `echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null`

8.  Update apt-get again
   `sudo apt-get update`

10. Install Jenkins on EC2
    `sudo apt-get install Jenkins`

12. Open your port 8080 on Your ec2 instance

13. Check the URL <public-ec2-instance>:8080

14. Create an admin user in our case it's group_one and with pwd zaq1ZAQ!

15. Configure Jenkins. Goto New item in Jenkins Dashboard
    <img width="791" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/06ba967a-2804-47d2-ab56-899879a22f48">

16. Select freestyle project and hit OK. Add your public GitHub repository
    <img width="870" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/7167e3bf-6530-41f5-8e9b-071c3ad04236">

17. Add in SCM
   <img width="867" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/ce1fa5f0-1dea-4b43-b954-528431ec0c9b">

18. Specify a branch from that repo to target
  <img width="840" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/d8bfebfd-0f08-42c8-a5fa-981548c14126">

19. Specify a poll interval, which is a cron job that runs at a particular interval
    <img width="891" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/42453c14-d372-44ea-a5b7-e3bc2cacde06">

20. Add build steps that you wanted to execute
    <img width="848" alt="image" src="https://github.com/Mahi2k/flask-application-jenkins/assets/10346368/4f735012-91e2-4bb8-a754-d5f6352b9148">

21. Add nginx configuration as below to reverse proxy to the port flask app is running
    location / {
              proxy_pass http://localhost:5000;
              proxy_http_version 1.1;
              proxy_set_header Upgrade $http_upgrade;
              proxy_set_header Connection 'upgrade';
              proxy_set_header Host $host;
              proxy_cache_bypass $http_upgrade;

              # First attempt to serve request as a file, then
              # as directory, then fall back to displaying a 404.
        }

22. Reload nginx
    `sudo systemctl reload nginx`
