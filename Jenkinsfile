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
                    sh "sudo docker build -t gayathrija/weatherappdev:${buildVersion} ."
                }
            }
        }

        stage('Unit Test') {
            steps {
                echo "Unit Test..."
                sh "sudo docker run --rm gayathrija/weatherappdev:${buildVersion} pytest test_app.py"
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

                sh "sudo docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW"
                sh "sudo docker push gayathrija/weatherappdev:${buildVersion}"
            }
        }

        stage('Deploy') {   
            steps {
                 echo "Deploy..."
                      //script {
                        //    def remoteServer = [:]
                          //      remoteServer.name = 'jenkintest'
                            //    remoteServer.host = '4.206.177.39'
                              //  remoteServer.user = 'jenk'
                                //remoteServer.allowAnyHosts = true
                              //  remoteServer.password = 'Jenk@1234567'

                               // sshCommand remote: remoteServer, command: '''
                                  sh "sudo docker stop $(sudo docker ps -aq)"
                                  sh "sudo lsof -i :8085 | awk 'NR>1 {print $2}' | xargs -r sudo kill"
                                  sh "sudo docker pull gayathrija/weatherappdev:${buildVersion}"
                                  sh "sudo docker run -d -p 8085:8080 gayathrija/weatherappdev:${buildVersion}"
                                 // # Add your script commands here
                                // '''
                // // Authenticate with SSH key
                // sshagent(credentials: ['credprod']) {
                //     // SSH commands to pull and run Docker image on the remote server
                //     sh "ssh -o StrictHostKeyChecking=no jenk@18.222.116.155 'sudo docker pull gayathrija/weatherappdev:${buildVersion}'"
                //     sh "ssh -o StrictHostKeyChecking=no jenk@18.222.116.155 'sudo docker run -d -p 8085:8080 gayathrija/weatherappdev:${buildVersion}'"
                //}
            }
        }

       // stage(post) {
         //   steps {
           //     always {
                    // cleanWs()
                    // dir("Weatherapp-pipeline@tmp") {
                    // deleteDir()
                    // }
                    // dir("Weatherapp-pipeline@script") {
                    // deleteDir()
                    // }
                    // dir("Weatherapp-pipeline@script@tmp") {
                    // deleteDir()
                    // }
              //  }
           // }
        //}
    }
}
