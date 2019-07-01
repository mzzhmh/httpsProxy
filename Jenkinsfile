node
{
        stage('Build') {
	    checkout scm
        }
	stage('build image') {
	    sh "docker build -t pythonserverrun:latest ."
        }
	stage('stop previous compose') {
	    sh "docker-compose down"
        }
        stage('Deploy compose') {
            sh "docker-compose up -d"
        }
}

