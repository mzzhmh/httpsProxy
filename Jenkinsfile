node
{
	def custImg
        stage('Build') {
	    checkout scm
        }
	stage('build image') {
	    sh "docker pull mzzhmh/httpsproxy:latest"
	    //sh "docker build --file dockerfile -t mzzhmh/httpsproxy:latest ."
	    custImg=docker.build("mzzhmh/httpsproxy:latest", "-f dockerfile ./")
        }
	stage('cleanup old docker images') {
	    sh "./purgeDangLing.sh"
	}
//	stage('Push new image to docker hub'){
//	    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-cred') {
//            custImg.push("latest")
//            }
//	}
//	stage('stop previous compose') {
//	    sh "docker-compose down"
//        }
//        stage('Deploy compose') {
//            sh "docker-compose up -d"
//        }
}

