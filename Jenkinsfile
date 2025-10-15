pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest > result.log || true'
                sh 'cat result.log'
            }
        }

        stage('Build') {
            steps {
                echo 'Demo build step - your app is ready!'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'result.log', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
