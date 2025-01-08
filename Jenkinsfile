pipeline {
    agent any
    environment {
        DOCKER_IMAGE_FRONT = 'reactapp'
        DOCKER_IMAGE_BACK = 'flaskapp'
        DOCKER_TAG = "${env.BUILD_NUMBER}" // Dynamic tag
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sassinizar/Library.git'
            }
        }
        stage('Building docker Images') {
            steps {
                script {
                    echo "Building frontend Docker image..."
                    sh """                  
                    docker-compose build
                    """
                }
            }
        }
       
        stage('Pushing the Images docker') {
            steps {
                script {
                    echo "Pushing frontend Docker image to Docker Hub..."
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-token', 
                           usernameVariable: 'DOCKER_USERNAME', 
                           passwordVariable: 'DOCKER_PASSWORD')]) {
                sh """
                    echo '$DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    docker tag flask_app nizar27/${DOCKER_IMAGE_BACK}:${DOCKER_TAG}
                    docker push nizar27/${DOCKER_IMAGE_BACK}:${DOCKER_TAG}
                    docker tag react_app nizar27/${DOCKER_IMAGE_FRONT}:${DOCKER_TAG}
                    docker push nizar27/${DOCKER_IMAGE_FRONT}:${DOCKER_TAG}
                    docker logout
                """
                }
            }
        }
     }
       
        stage('Deploy with Docker-Compose') {
            steps {
                script {
                    echo "Deploying with Docker Compose..."
                    sh 'docker-compose down'
                    sh 'docker-compose pull'
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
