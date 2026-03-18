pipeline {
    agent any
    stages{
        stage('Checkout Code'){
            steps{
                git branch: 'main', url: 'https://github.com/VigneshYR/ci-cd-aws-pipeline'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t fintech-app -f fintech-devops-microservice/docker/Dockerfile .'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose -f docker/docker-compose.yml up -d'
            }
        }
    }
}
