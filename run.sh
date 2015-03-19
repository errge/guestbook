#!/bin/sh

docker run -P -it --name app --link mongo:mongo --rm errge/guestbook
