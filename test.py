pipeline{
agent any
stages
{
  stage('BUild')
  {
  steps{
  echo "Building the project"
}
}
stage('Test')
  {
  steps{
  echo "Testing the project"
}
}
stage('Deploy')
  {
  steps{
  echo "Deploying the project"
}
}
}
}

