pipeline
{
    agent
any
stages
{
    stage("one")
{
    steps
{
    bat
'echo %USERNAME% >> name.txt'
}
}
stage("two")
{
    steps
{
    bat
'type name.txt'
}
}
stage("three")
{
    steps
{
    bat
'fsutil volume diskfree c:'
}
}
stage("four")
{
    steps
{
    bat
'move name.txt C:/Users/tubulz/Downloads'
}
}

}
}