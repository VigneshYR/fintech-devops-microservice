pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/VigneshYR/fintech-devops-microservice.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t fintech-app -f docker/Dockerfile .'
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
