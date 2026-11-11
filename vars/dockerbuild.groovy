def call(String ImageName, String ImageTag , String DockerUserName){
  sh ' docker build -t "DockerUserName"/"$ImageNamr":"$ImageTag" .'
