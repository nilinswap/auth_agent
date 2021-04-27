# commands

`ps aux | grep postgres` search a process

` createuser --interactive postgres` to create new user in postgres




#### docker commands
to see logs
```bash
docker run -it -p 8000:8000 auth-app
```

stop docker
```bash
docker stop <container id>
```

enter docker in shell mode (after docker run was a success.)
```bash
docker exec -it <container name> bash
```