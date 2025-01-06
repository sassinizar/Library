pipeline {
    agent any
    environment {
        DOCKER_IMAGE_FRONT = 'flaskapp'
        DOCKER_IMAGE_BACK = 'reactapp'
        DOCKER_TAG = "${env.BUILD_NUMBER}" // Dynamic tag
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sassinizar/Library.git'
            }
        }
        stage('Build Docker Frontend Image') {
            steps {
                script {
                    echo "Building frontend Docker image..."
                    sh """
                    docker build -t ${DOCKER_IMAGE_FRONT}:${DOCKER_TAG} ./frontend
                    """
                }
            }
        }
        stage('Build Docker Backend Image') {
            steps {
                script {
                    echo "Building backend Docker image..."
                    sh """
                    docker build -t ${DOCKER_IMAGE_BACK}:${DOCKER_TAG} ./Backend
                    """
                }
            }
        }
        stage('Push Frontend Docker Image') {
            steps {
                script {
                    echo "Pushing frontend Docker image to Docker Hub..."
                    sh """
                    docker login -u $DOCKER_USERNAME --password-stdin
                    docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    """
                }
            }
        }
        stage('Push Backend Docker Image') {
            steps {
                script {
                    echo "Pushing backend Docker image to Docker Hub..."
                    sh """
                    docker login -u $DOCKER_USERNAME --password-stdin
                    docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    """
                }
            }
        }
        stage('Deploy with Docker-Compose') {
            steps {
                script {
                    echo "Deploying with Docker Compose..."
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
