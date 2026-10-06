pipeline {

    agent any

    environment {
        REPORTS_DIR = "reports"
        POSTMAN_COLLECTION = "api-tests/postman/QAOps_Collection.postman_collection.json"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                sh '''
                    mkdir -p ${REPORTS_DIR}

                    python3 --version
                    node --version
                    npm --version
                    chromium --version || true
                    chromedriver --version || true
                    newman --version
                '''
            }
        }

        stage('Install UI Dependencies') {
            steps {
                sh '''
                    python3 -m venv .jenkins-venv

                    . .jenkins-venv/bin/activate

                    pip install --upgrade pip
                    pip install -r ui-tests/requirements.txt
                '''
            }
        }

        stage('UI Tests - Selenium') {
            steps {
                sh '''
                    . .jenkins-venv/bin/activate

                    PYTHONPATH=ui-tests \
                    pytest ui-tests/tests \
                    -v \
                    --junitxml=${REPORTS_DIR}/ui-tests.xml
                '''
            }
        }

        stage('API Tests - Newman') {
            steps {
                sh '''
                    newman run ${POSTMAN_COLLECTION} \
                    --reporters cli,junit \
                    --reporter-junit-export ${REPORTS_DIR}/api-tests.xml
                '''
            }
        }
    }

    post {

        always {
            echo "Publishing test reports..."

            junit(
                allowEmptyResults: true,
                testResults: 'reports/*.xml'
            )

            archiveArtifacts(
                artifacts: 'reports/*.xml',
                allowEmptyArchive: true
            )

            archiveArtifacts(
                artifacts: 'security/**/*',
                allowEmptyArchive: true
            )
        }

        success {
            echo "========================================"
            echo " QA OPS PIPELINE PASSED"
            echo " UI tests: PASSED"
            echo " API tests: PASSED"
            echo "========================================"
        }

        failure {
            echo "========================================"
            echo " QA OPS PIPELINE FAILED"
            echo " Check the Jenkins console and reports."
            echo "========================================"
        }
    }
}