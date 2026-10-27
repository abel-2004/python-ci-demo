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
                    pytest --junitxml=reports/junit.xml
                '''
            }
            post {
                always {
                    junit testResults: 'reports/junit.xml', allowEmptyResults: true
                }
            }
        }

        stage('Build artifacts') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pip install --upgrade build
                    rm -rf dist
                    python -m build
                    cd npm
                    npm pack --pack-destination ../dist
                    cd ../dist
                    sha256sum * > SHA256SUMS.txt
                    ls -l
                '''
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
