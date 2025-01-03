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
               echo 'build stage'     
            }
        }
        stage('Push Docker Image') {
            steps {
                echo "the scond stage push"
            }
        }
        stage('Deploy') {
            steps {
                echo "the third stage deploy"
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
