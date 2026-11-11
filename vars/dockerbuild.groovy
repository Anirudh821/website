def call(String ImageName, String ImageTag ){
  sh ' docker build -t "$ImageNamr":"$ImageTag" .'
