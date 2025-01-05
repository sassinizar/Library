pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1' // Enable Docker BuildKit
        DOCKER_IMAGE = 'my-repository/flaskapp'
        DOCKER_TAG = 'latest' // You can use a dynamic tag like "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building my Docker image......."
                    sh """
                    docker buildx build -t ${env.DOCKER_IMAGE}:${env.DOCKER_TAG} ./Backend
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image to Docker Hub..."
                    withCredentials([usernamePassword(credentialsId: 'nizarsassi-dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh """
                        echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin
                        docker push ${env.DOCKER_IMAGE}:${env.DOCKER_TAG}
                        """
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                // Add deployment logic here (e.g., deploy to Kubernetes, Docker Swarm, etc.)
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker resources..."
            sh 'docker rmi ${env.DOCKER_IMAGE}:${env.DOCKER_TAG} || true'
        }
    }
}
