def buildVersion

pipeline {
    agent any
    options {
        timeout(time: 5, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checkout..."
                git url: 'https://github.com/gayathri-ja/weatherapprepo.git', 
                    credentialsId: '1b5ef133-eaa9-4d11-97c5-82329c8aa60c',
                    branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo "Build..."
                script {
                    buildVersion = new Date().format('yyyyMMdd-HHmmss')
                    sh "docker build -t gayathrija/weatherappdev:${buildVersion} ."
                }
            }
        }

        stage('Unit Test') {
            steps {
                echo "Unit Test..."
                sh "docker run --rm gayathrija/weatherappdev:${buildVersion} pytest test_app.py"
            }
        }

        stage('Push') {
            steps {
                echo "Push..."
                script {
                    DOCKERHUB_CREDENTIALS = credentials('ac643925-fe10-4d90-899c-4282fae6dc00')
                    DOCKERHUB_CREDENTIALS_USR = 'gayathrija'
                    DOCKERHUB_CREDENTIALS_PSW = 'dckr_pat_NlvLmQpfODLrHLb2SALVuKOf4lI'
                }

                sh "docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW"
                sh "docker push gayathrija/weatherappdev:${buildVersion}"
            }
        }

        stage('Deploy') {   
            steps {
                echo "Deploy..."

                // Pull the Docker image from Docker Hub
                sh "docker -H ssh://jenkins@18.222.116.155 'docker run -d -p 8085:8080 gayathrija/weatherappdev:${buildVersion}'"
            }
        }

        stage('Post') {
            steps {
                cleanWs()
            }
        }
    }
}
