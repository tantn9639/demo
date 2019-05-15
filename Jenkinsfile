pipeline {
    environment {
        registry = "tantn9639/test"
        registryCredential = 'dockerhub'
        dockerImage = ''
        app_name = 'demo-app'
        branch = 'master'
        project = 'marine-potion-240602'
        CREDENTIALS_PATH = credentials('gcloud_auth')
        }
    agent  any
    stages {
        stage ('Git pull') {
            steps {
                git branch: "$branch",
                credentialsId: 'git_id',
                url: 'https://github.com/tantn9639/demo.git'
                }
            }
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    }
                }
            }
        stage('Push Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                        sh 'echo Push Imaged to Registry'
                        }
                    }
                }
            }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
                }   
            } 
        stage('Deploy Image to k8s') {
            steps{
                sh """
                gcloud auth activate-service-account --key-file $CREDENTIALS_PATH
                gcloud config set project $project
                gcloud container clusters get-credentials production-cluster --zone southamerica-east1-a
                sed -i "s/__APP_NAME__/${app_name}/g" deployment.yaml
                sed -i "s+__IMAGE__+${registry}+g" deployment.yaml
                sed -i "s/__VERSION__/${BUILD_NUMBER}/g" deployment.yaml
                kubectl apply -f ./deployment.yaml
                """
                }   
            }
        }    
    }   
