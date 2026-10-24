pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Lint and Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    flake8 app tests
                    mkdir -p reports
                    pytest --junitxml=reports/junit.xml --cov=app --cov-branch --cov-report=term-missing --cov-report=xml:reports/coverage.xml --cov-report=html:reports/htmlcov --cov-fail-under=90
                '''
            }
            post {
                always {
                    junit testResults: 'reports/junit.xml', allowEmptyResults: true
                    recordCoverage(
                        tools: [[parser: 'COBERTURA', pattern: 'reports/coverage.xml']],
                        id: 'python',
                        name: 'Python coverage',
                        qualityGates: [[threshold: 90.0, metric: 'LINE', baseline: 'PROJECT', criticality: 'FAILURE']]
                    )
                    archiveArtifacts artifacts: 'reports/htmlcov/**', allowEmptyArchive: true
                }
            }
        }

        stage('Package') {
            steps {
                sh 'tar czf app-${BUILD_NUMBER}.tar.gz app requirements.txt'
                archiveArtifacts artifacts: 'app-*.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
