```sh
docker build -t reminders . -f deploy/Dockerfile 
docker run --name reminders -p 8005:80 reminders
docker run -v ${PWD}/data:/data -e LITESTREAM_ACCESS_KEY_ID=XXX -e LITESTREAM_SECRET_ACCESS_KEY=XXX -name reminders -p 8005:80 reminders
```

s6-rc: fatal: timed out
s6-sudoc: fatal: unable to get exit status from server: Operation timed out