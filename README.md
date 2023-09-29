# Nginx Logs Pipeline


This project implements a pipeline to count sit visitors, by using data from web server logs.<br>
Every time someone visits a web page, their browsers will send data from a web server.

The process of sending a request from a web browser to a server:

![](https://www.dataquest.io/wp-content/uploads/2019/01/server_request.svg)

First, the client sends a request to the web server asking for a certain page, then The web server loads the page from the filesystem and returns it to the client. As it serves the request, the web server writes a line to a log file on the filesystem that contains some metadata about the client and the request.


Here are a few lines from the Nginx log for this blog:

```
X.X.X.X - - [09/Mar/2017:01:15:59 +0000] "GET /blog/assets/css/jupyter.css HTTP/1.1" 200 30294 "https://www.dataquest.io/blog/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +https://www.pingdom.com/)"
X.X.X.X - - [09/Mar/2017:01:15:59 +0000] "GET /blog/assets/js/jquery-1.11.1.min.js HTTP/1.1" 200 95786 "https://www.dataquest.io/blog/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +https://www.pingdom.com/)
X.X.X.X - - [09/Mar/2017:01:15:59 +0000] "GET /blog/assets/js/markdeep.min.js HTTP/1.1" 200 58713 "https://www.dataquest.io/blog/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +https://www.pingdom.com/)"
X.X.X.X - - [09/Mar/2017:01:15:59 +0000] "GET /blog/assets/js/index.js HTTP/1.1" 200 3075 "https://www.dataquest.io/blog/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +https://www.pingdom.com/)"
X.X.X.X - - [09/Mar/2017:01:16:00 +0000] "GET /blog/atom.xml HTTP/1.1" 301 194 "-" "UniversalFeedParser/5.2.1 +https://code.google.com/p/feedparser/"
X.X.X.X - - [09/Mar/2017:01:16:01 +0000] "GET /blog/feed.xml HTTP/1.1" 200 48285 "-" "UniversalFeedParser/5.2.1 +https://code.google.com/p/feedparser/"
```


## pipeline

![](https://www.dataquest.io/wp-content/uploads/visitors_per_day.svg)


fisrt step is opening  the log files and reading line by line, parse each line into fields, then write each line and the parsed fields to a database.
Second, executing a query to count number of user per day by their IPs.
