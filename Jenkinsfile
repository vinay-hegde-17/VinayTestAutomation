pipeline {
    agent any
    stages {
        stage('Checkout Backend') {
            steps {
                dir('TestFastAPI') {
                    git branch: 'dev', url: 'https://github.com/vinay-hegde-17/TestFastAPI.git'
                }
            }
        }
        stage('Checkout Tests') {
            steps {
                dir('VinayTestAutomation') {
                    git branch: 'main', url: 'https://github.com/vinay-hegde-17/VinayTestAutomation.git'
                }
            }
        }
        stage('Setup venv') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r VinayTestAutomation/requirements.txt'
                bat 'venv\\Scripts\\pip install -r TestFastAPI/requirements.txt'
            }
        }
        stage('Run Backend') {
            steps {
                dir('TestFastAPI') {
                    bat 'start /B run_server.bat'
                }
                // give backend time to start
                bat 'timeout /t 5'
            }
        }
        stage('Run Tests') {
            steps {
                dir('VinayTestAutomation') {
                    bat 'venv\\Scripts\\pytest tests/test_cases -v --html=reports/test_report.html --self-contained-html'
                }
            }
        }
        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'VinayTestAutomation/reports/*.html', fingerprint: true
            }
        }
    }
}
