pipeline {
    agent {node{label'raspberry pi'}}
    stages {
    stage("ping"){
        steps{
            echo "pingen naar de slave..."
            sh " ansible-playbook ping.yml"
      }
    }
    stage("image") {
      steps{
          echo "image aan het maken..."
          sh " ansible-playbook nicholas_playbook.yml"
      }
    }
    stage("dockerfile") {
      steps{
          echo "dockerfile aan het lezen..."
          sh "pwd"
          sh "ls"
          sh " ansible-playbook nicholas_dockerfile.yml"
      }
    }
    stage("container") {
      steps{
          echo "container aan het maken..."
          sh " ansible-playbook nicholas_container.yml"
      }
    }
    
  }
}
