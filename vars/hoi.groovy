def call(){
  withCredentials([usernamePassword(
    credentialsId: "Admins_ID",
    usernameVariable: "my_id",
    passwordVariable: "my_password"
)]){
   sh 'docker login -u "$my_id" -p "$my_password" '
   sh 'docker image tag app:latest "$my_id"/latest'
   sh 'docker push "$my_id"/app '
 }
}
