pipeline {
    agent any
    environment {
        DOCKER_IMAGE_FRONT = 'flaskapp'
        DOCKER_IMAGE_BACK = 'reactapp'
        DOCKER_TAG = "latest"// Dynamic tag "${env.BUILD_NUMBER}" 
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
<<<<<<< HEAD
                    docker tag flask_app nizar27/${DOCKER_IMAGE_BACK}:${DOCKER_TAG}
                    docker push nizar27/${DOCKER_IMAGE_BACK}:${DOCKER_TAG}
                    docker tag react_app nizar27/${DOCKER_IMAGE_FRONT}:${DOCKER_TAG}
                    docker push nizar27/${DOCKER_IMAGE_FRONT}:${DOCKER_TAG}
                    docker logout
=======

                    docker tag flask_app:latest nizar27/${DOCKER_IMAGE_BACK}:latest 
                    docker push nizar27/${DOCKER_IMAGE_BACK}:latest 

                    docker tag react_app:latest nizar27/${DOCKER_IMAGE_FRONT}:latest 
                    docker push nizar27/${DOCKER_IMAGE_FRONT}:latest 
        
>>>>>>> 60f4305e073e94de2080f6191f4b4bfa7bf63763
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
