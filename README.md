```sh
docker build -t reminders . -f deploy/Dockerfile 
docker run --name reminders -p 8005:8000 reminders
```

s6-rc: fatal: timed out
s6-sudoc: fatal: unable to get exit status from server: Operation timed out