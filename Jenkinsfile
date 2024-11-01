pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'lunariiin'
        DOCKER_PASSWORD = credentials('dockerhub-credentials') 
        IMAGE_NAME = 'lunariin/orderstackapp'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/EvaCherkun/OrderStackApp'
            }
        }

        stage('Docker Login') { // Переносимо авторизацію перед збіркою образу
            steps {
                script {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}

