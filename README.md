# wayBackMachine

Language : Python 

Tool : Pycharm

Input : a Csv File  that contains Domain Names 
 
Processing :
1. read Csv File
2. it will read all domains 
3. call api for all domains one by one (http://archive.org/wayback/available?url=realomni.com ) i.e. domain : realomni.com
4. capture screenshot of all domains.
5. save them one by one locally.
6. sae name of those domains whose status is 404 ! 
