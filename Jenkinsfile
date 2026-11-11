@Library("hoi") _
pipeline{
    agent{label "Anirudh"}
    stages{
        stage("code"){
            steps{
                script{
                    clone("https://github.com/Anirudh821/website.git","main")
                }
            }
        }
        stage("Build"){
            steps{
                script{
                    dockerbuild("app","1.0")
                 }
            }
        }
        stage("Push to docker hub"){
            steps{
                script{
                    hoi()
                   }
                }  
            }
            stage("Deploy"){
                steps{
                    echo "container running"
                    sh 'docker compose -f "docker-compose.yaml" up -d'
                    }
                }
            }
      }  
