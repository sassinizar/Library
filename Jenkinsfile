pipeline {
    agent any

    environment {
        DOCKER_IMAGE_FRONT = 'flaskapp'
        DOCKER_IMAGE_Back = 'reactapp'
        DOCKER_TAG = 'latest' // You can use a dynamic tag like "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS = credentials('nizarsassi-dockerhub') // Jenkins credentials ID for Docker Hub
    }

    stages {
        stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sassinizar/Library.git'
            }
        }
        stage('Build Docker frontend Image') {
            steps {
                script {
                    echo "Building backend Docker image..."
                    sh """
                    docker build -t ${DOCKER_IMAGE_FRONT}:${env.BUILD_NUMBER} ./frontend
                    """
                }
            }
        }
        stage('Build Docker Backend  Image') {
            steps {
                script {
                    echo "Building Docker frontend image..."
                    sh """
                    docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ./Backend
                    """
                }
            }
        }
        stage('Push frontend Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image frontend to Docker Hub..."
                    sh """
                    echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                    docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    """
                }
            }
        }
        stage('Push backend Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image backend to Docker Hub..."
                    sh """
                    echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                    docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    """
                }
            }
        }
        stage('Deploy with Docker-Compose') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker resources..."
            sh 'docker rmi ${DOCKER_IMAGE}:${env.BUILD_NUMBER} || true'
        }
    }
}