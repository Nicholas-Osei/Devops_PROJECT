pipeline {
    agent {node{label'raspberry pi'}}
    "HostConfig": {
        "Devices": [
            {
                "PathOnHost": "/dev/gpiomem",
                "PathInContainer": "/dev/gpiomem",
                "CgroupPermissions": "rwm"
            }
        ]
    }
    stages {
    stage("Ping"){
        steps{
            echo "Pingen naar rpi(connectie test)..."
            sh " ansible-playbook ping.yml"
            echo "Ping Gelukt!"
      }
    }
    stage("Image") {
      steps{
          echo "Image aan het maken..."
          sh " ansible-playbook nicholas_playbook.yml"
          echo "Image aangemaakt!"
      }
    }
    stage("Dockerfile") {
      steps{
          echo "Lezen van het dockerfile..."
          sh "pwd"
          sh "ls"
          sh " ansible-playbook nicholas_dockerfile.yml"
          echo "Dockerfile Playbook gelukt!"
      }
    }
    stage("Container") {
      steps{
          echo "Container aan het maken..."
          sh " ansible-playbook nicholas_container.yml"
          echo "Containtainer is aangemaakt!"
          
      }
    }
    
  }
}
