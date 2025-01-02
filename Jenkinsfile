pipeline {

    agent any;

    stages {

        stage('build') {
            steps {
               sh 'echo build stage'     
            }
        }
        stage('push') {
            steps {
                sh 'echo "the scond stage push"'
            }
        }
        stage('deploy') {
            steps {
                sh 'echo "the third stage deploy"'
            }
        }
    }
}
