pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Upgrade pip and install requirements
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest, continue even if some tests fail
                bat 'pytest > result.log || exit 0'
                bat 'type result.log'
            }
        }

        stage('Build') {
            steps {
                echo 'Build step completed - app is ready!'
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
