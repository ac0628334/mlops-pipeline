pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/ac0628334/mlops-pipeline.git']]
                ])
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-pipeline:test .'
            }
        }
        
        stage('Run Tests in Docker') {
            steps {
                bat 'docker run --rm mlops-pipeline:test python -m pytest src/tests -v'
            }
        }
        
        stage('Docker Build & Push') {
            steps {
                // TODO: Add secure Docker Hub credentials in Jenkins
                // For now, skip push to avoid security issues
                bat 'docker build -t abhidocker0288/mlops-pipeline:latest .'
                echo 'Skipping Docker push - add credentials in Jenkins first'
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/'
            }
        }
    }
}