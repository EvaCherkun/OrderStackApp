pipeline {
    agent any

    environment {
        IMAGE_NAME = 'docker-image' 
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
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Створюємо тимчасовий файл для пароля
                        bat "echo ${DOCKER_PASSWORD} > temp_password.txt"
                        bat "docker login -u ${DOCKER_USERNAME} --password-stdin < temp_password.txt"
                        // Видаляємо файл після використання
                        bat "del temp_password.txt"
                    }
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
