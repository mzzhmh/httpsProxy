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
	stage('Push new image to docker hub'){
	    docker.withRegistry('https://registry.hub.docker.com', 'dockerKey') {
            custImg.push("latest")
            }
	}
	stage('cleanup old docker images') {
            sh "./purgeDangLing.sh"
        }
	stage('stop previous compose') {
	    sh "docker-compose down"
        }
        stage('Deploy compose') {
            sh "docker-compose up -d"
        }
}

