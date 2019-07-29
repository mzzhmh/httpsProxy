node
{
        stage('Build') {
	    checkout scm
        }
	stage('build image') {
	    sh "docker pull mzzhmh/httpsproxy:latest"
	    docker.build("mzzhmh/httpsproxy:latest")
        }
//	stage('stop previous compose') {
//	    sh "docker-compose down"
//        }
//        stage('Deploy compose') {
//            sh "docker-compose up -d"
//        }
}

