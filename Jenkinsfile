pipeline {
    agent any

    tools {
        git 'Default' 
    }

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-credentials')  
        IMAGE_NAME = 'eva_cherkun/orderstackapp'  
    }

    stages {
        stage('Checkout') {
            steps {
                
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    bat """
                    echo ${DOCKER_CREDENTIALS_PSW} | docker login -u ${DOCKER_CREDENTIALS_USR} --password-stdin
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    bat "docker push ${IMAGE_NAME}:latest"
                }
            }
        }
    }

    post {
        always {
            node {
                bat 'docker logout'
            }
        }
    }
}
