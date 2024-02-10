```sh
docker build -t reminders . -f deploy/Dockerfile 
docker run --name reminders -p 8005:8000 reminders
```

```text
    {
       "schemaVersion": 2,
       "dockerfilePath": "./deploy/Dockerfile" # the path to your dockerfile
    }
```