def buildVersion

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control
                git url: 'https://github.com/gayathri-ja/weatherapprepo.git', 
                    credentialsId: '1b5ef133-eaa9-4d11-97c5-82329c8aa60c',
                    branch: 'main'
            }
        }

        stage('Build') {
            steps {
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
                // Run your unit tests inside the Docker container
                sh "docker run --rm gayathrija/weatherappdev:${buildVersion} pytest test_app.py"
            }
        }

        stage('push') {
        steps {
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

    environment {
        IMAGE_NAME = 'weatherapp_prodsrv'
        IMAGE_TAG = 'weatherapp_prodsrv'
        AWS_INSTANCE_IP = '52.14.216.119'
        AWS_INSTANCE_USER = 'root' // Replace with your instance's SSH user
        SSH_PRIVATE_KEY = credentials('key-00adf693162fa12dd')
    }
            
    stages('deploy') {
        stage('Pull Image and Deploy to AWS EC2') {
            steps {
                script {
                    // Log in to the AWS EC2 instance using SSH
                    sshagent(credentials: ['key-00adf693162fa12dd']) {
                        sh "ssh -o StrictHostKeyChecking=no -i $SSH_PRIVATE_KEY ${AWS_INSTANCE_USER}@${AWS_INSTANCE_IP} 'docker pull ${IMAGE_NAME}:${IMAGE_TAG}'"
                        sh "ssh -o StrictHostKeyChecking=no -i $SSH_PRIVATE_KEY ${AWS_INSTANCE_USER}@${AWS_INSTANCE_IP} 'docker stop ${IMAGE_NAME} || true && docker rm ${IMAGE_NAME} || true'"
                        sh "ssh -o StrictHostKeyChecking=no -i $SSH_PRIVATE_KEY ${AWS_INSTANCE_USER}@${AWS_INSTANCE_IP} 'docker run -d --name ${IMAGE_NAME} -p 80:80 ${IMAGE_NAME}:${IMAGE_TAG}'"        
        }
    }         
}
