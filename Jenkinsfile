pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ac0628334/mlops-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r src/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -q'
            }
        }

        stage('Docker Build & Push') {
            steps {
                sh 'docker login -u abhidocker0288 -p T5qaFk6GpeaDGE4xGwpRrU_aN5I'
                sh 'docker build -t abhidocker0288/mlops-pipeline:latest .'
                sh 'docker push abhidocker0288/mlops-pipeline:latest'

            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
