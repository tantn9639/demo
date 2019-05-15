pipeline {
    environment {
    def app_name = "python_demo_app"
    def app
    }  
  agent 
    stages {
      stage ('Build') {
        steps {
          app = docker.build(app_name) 
          }
        }
      stage ('Test') {
        steps {
          app.inside{
            sh 'demo.py'
           }
        }
      stage('Push image') {
        steps {
          sh 'echo PUSH'
          }
        }
    }
    }
  }
