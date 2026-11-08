def call(){
  withCredentials[(usernamePassword(
    credentialsId: "Admins_ID"
    usernameVariable: "my-id"
    passwordVariable: "my-password"
)])
 {
   sh 'docker login -u "$my-id" -p "$my-password" '
   sh 'docker image tag app "$my-id"/app'
   sh 'docker push "$my-id"/app '
 }
}
