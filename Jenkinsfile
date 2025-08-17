pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vinay-hegde-17/VinayTestAutomation.git'
            }
        }
        stage('Setup venv') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest tests/test_cases -v --html=reports/test_report.html --self-contained-html'
            }
        }
        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            }
        }
    }
    post {
        always {
            junit 'reports/*.xml'
        }
    }
}
