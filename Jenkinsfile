pipeline {
    agent any

    environment {
        IMAGE_NAME = 'lunariiin/orderstackapp' 
        DOCKER_USERNAME = 'lunariiin' 
        DOCKER_PASSWORD = '-@.3r}4yNdu;=yY' 
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm 
                }
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
                    bat "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
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
            script {
                bat 'docker logout'
            }
        }
    }
}
