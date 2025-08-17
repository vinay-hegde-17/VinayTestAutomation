pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/vinay-hegde-17/VinayTestAutomation.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                sh 'pytest tests/ --html=reports/test_report.html'
            }
        }
        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            }
        }
    }
}
