pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-repository/flaskapp'
        DOCKER_TAG = 'latest' // You can use a dynamic tag like "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS = credentials('nizarsassi-dockerhub') // Jenkins credentials ID for Docker Hub
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building my Docker image......."
                    sh """
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ./Backend
                    """
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image to Docker Hub..."
                    sh """
                    echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying application..."
                // Add deployment logic here (e.g., deploy to Kubernetes)
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker resources..."
            sh 'docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || true'
        }
    }
}
