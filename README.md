# auth_agent
An easy-pluggable and configurable api for user authentication. 

![security agent](https://img-aws.ehowcdn.com/340x221p/photos.demandstudios.com/getty/article/110/25/86512177.jpg)



## inception

### Requirements
- it should use client's database instead of maintaining his own. 
- Api Signature should be configurable. Some popular apis will be provided but the response body should be configured.
- create a testing system. For reliability, clients should write tests.
- extreme error handling


### Boundaries
1. Read a config.json file where, at least, these things are mentioned
   
    1. DB
       
        a. user
        
        b. password
        
        c. host
       
        d. port
       
        e. user_table
       
    2. Apis - 
       
        a. get_user -> {
                req_cookie: session,
                req_body:{},
                res_body:{
                    id,
                    name,
                    age
                }
            }
       
        etc
        

### Pointers
- It is only meant for quick solution to auth. It is not a production-suited solution.
- It can cause some inconsistency issues so tests must be written properly
- It is best suitable for demo, poc, mvp etc

### Scope

- provide support for token based auth.
- Make Api Signature fully configurable
- handle more complex structures of user_table
- Provide other auth features like oauth etc.



## todo

[ ] setup django project
[ ] setup a dummy model and provide api 
[ ] polish api keeping frontend in mind
[ ] test the integration with a dummy project