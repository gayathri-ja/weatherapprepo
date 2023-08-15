def buildVersion

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checkout..."
                // Checkout your source code from version control
                git url: 'https://github.com/gayathri-ja/weatherapprepo.git', 
                    credentialsId: '1b5ef133-eaa9-4d11-97c5-82329c8aa60c',
                    branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo "Build..."
                // Generate a timestamp-based version number for the Docker image.
                script {
                    buildVersion = new Date().format('yyyyMMdd-HHmmss')
                }

                // Build your Docker image with the version number
                sh "docker build -t gayathrija/weatherappdev:${buildVersion} ."
            }
        }

        stage('Unit Test') {
            steps {
                echo "Unit Test..."
                // Run your unit tests inside the Docker container
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

                // Log in to Docker Hub using the credentials
                sh "docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW"

                // Push the Docker image to a container registry
                sh "docker push gayathrija/weatherappdev:${buildVersion}"

            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy..."
                script {
                    // Define variables
                    def instancePublicIP = '18.116.65.96'
                    def instancePort = '8081'
                    def dockerImageTag = "${buildVersion}"
            
                // Pull the Docker image from Docker Hub
                sh "docker pull gayathrija/weatherappdev:${dockerImageTag}"
            
                // Deploy using SSH and Docker
                sh "docker run -d -p ${instancePort}:80 gayathrija/weatherappdev:${dockerImageTag}"
                }
            }        
        }
    }
}
