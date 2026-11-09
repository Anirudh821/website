def call(){
  withCredentials([usernamePassword(
    credentialsId: "Admins_ID",
    usernameVariable: "my_id",
    passwordVariable: "my_password"
)]){
   sh 'docker login -u "$my_id" -p "$my_password" '
   sh 'docker image tag app:1.0 "$my_id"/app:1.0'
   sh 'docker push "$my_id"/app:1.0 '
 }
}
