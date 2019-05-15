HOME TEST
This is my hometest, thanks for reading !!!
1. Ansible for install base server, all of taks in playbook.yml
2. The python Script Demo.py with two option
 - demo.py --find <keyword>   --- find all jenkins jobs has job-name contains keyword
 - demo.py --build <job-name>    --- build jenkins job with job-name
   The script needs 3 environment variables JENKINS_URL. API_USER, API_TOKEN
   Dockerfile is used for dockerize demo.py script with minimal python image.
3. Jenkinfile contains pipeline CI/CD code to Pull, Build images, Push and Deploy Images to Google Kubernetes Engine with deployment.yaml configfile.
