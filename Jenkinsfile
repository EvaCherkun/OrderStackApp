pipeline {
    agent any

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
                    bat "docker build -t docker-image:latest ."
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                       
                        echo "Logging in to Docker Hub as ${DOCKER_USERNAME}"
                        bat "cmd /c echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    bat "docker push docker-image:latest"
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
