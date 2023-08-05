def buildVersion

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control
                git url: 'https://github.com/gayathri-ja/weatherapprepo.git', credentialsId: 'gayathri-ja'
            }
        }

        stage('Build') {
            steps {
                // Generate a timestamp-based version number for the Docker image
                script {
                    buildVersion = new Date().format('yyyyMMdd-HHmmss')
                }

                // Build your Docker image with the version number
                sh "docker build -t weatherappnew:${buildVersion} ."
            }
        }

        stage('Unit Test') {
            steps {
                // Run your unit tests inside the Docker container
                sh "docker run --rm weatherappnew:${buildVersion} pytest test_app.py"
            }
        }

        stage('Deploy') {
            steps {
                // Push the Docker image to a container registry (Optional)
                sh "docker push weatherappnew:${buildVersion}"

                // Deploy the application using the Docker image
                // You might use Docker Compose, Kubernetes, or other deployment methods based on your setup.
                // Here's an example using Docker Compose:
                
            }
        }
    }
}
