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
                    bat "echo %DOCKER_PASSWORD% | docker l
