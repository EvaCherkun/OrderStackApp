pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-credentials')  
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
                    bat """
                    echo %DOCKER_CREDENTIALS_PSW% | docker login -u %DOCKER_CREDENTIALS_USR% --password-stdin
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
            script {
                bat 'docker logout'
            }
        }
    }
}
