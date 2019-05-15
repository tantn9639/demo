pipeline {
  agent  { dockerfile true }
  stages {
    stage ('Build') {
      steps {
          sh 'python -version'
        }
        }
    stage ('Test') {
      steps {
            sh 'demo.py'
        }
    stage('Push image') {
      steps {
          sh 'echo PUSH'
          }
        }
    }
    }
  }
