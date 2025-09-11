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
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install --user -r src/requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    export PATH=$HOME/.local/bin:$PATH
                    python3 -m pytest src/tests -v
                '''
            }
        }
        
        stage('Docker Build & Push') {
            steps {
                sh 'docker login -u abhidocker0288 -p T5qaFk6GpeaDGE4xGwpRU_aN5I'
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