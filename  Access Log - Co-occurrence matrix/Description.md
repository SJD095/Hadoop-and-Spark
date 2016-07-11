uppose we have an access log file from a web server in the following format:
 
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/reset.css HTTP/1.1" 200 1014
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/960.css HTTP/1.1" 200 6206
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/the-associates.css HTTP/1.1" 200 15779
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/the-associates.js HTTP/1.1" 200 4492
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lightbox.js HTTP/1.1" 200 25960
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/search-button.gif HTTP/1.1" 200 168
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/dummy/secondary-news-3.jpg HTTP/1.1" 200 5604
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/dummy/primary-news-1.jpg HTTP/1.1" 200 10556
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/dummy/primary-news-2.jpg HTTP/1.1" 200 9925
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/closelabel.gif HTTP/1.1" 200 979
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/home-logo.png HTTP/1.1" 200 3892
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/dummy/secondary-news-2.jpg HTTP/1.1" 200 5397
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/loading.gif HTTP/1.1" 200 2767
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/dummy/secondary-news-4.jpg HTTP/1.1" 200 5766
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/home-media-block-placeholder.jpg HTTP/1.1" 200 68831
10.223.157.186 - - [15/Jul/2009:15:50:37 -0700] "GET /assets/img/dummy/secondary-news-1.jpg HTTP/1.1" 200 5766
10.223.157.186 - - [15/Jul/2009:15:50:37 -0700] "GET /assets/swf/home-media-block.swf HTTP/1.1" 200 123884
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET / HTTP/1.1" 200 9157
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/css/960.css HTTP/1.1" 304 -
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/css/the-associates.css HTTP/1.1" 304 -
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 304 -
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/js/lightbox.js HTTP/1.1" 304 -
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/css/reset.css HTTP/1.1" 304 -
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/js/the-associates.js HTTP/1.1" 304 -
10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/img/dummy/secondary-news-4.jpg HTTP/1.1" 304 -
......
 
For each jpg image A, calculate the conditional probability P (primary-news-1.jpg | A), that is, |IPs that visit both A and primary-news-1.jpg|/|IPs that visit A|. 
 
 
 
Note: 
1) You can assume that no jpg images in the log has the same name, but different paths.
2) Only consider web visit via HTTP GET and POST command.
 
 
a example data set: access_log.zip
 
The output format shall be like:
primary-news-2.jpg  0.333333333333 

secondary-news-1.jpg 0.666666666

secondary-news-3.jpg  0.666666666666
......

Each line is a jpg file name A, followed by P（primary-news-1.jpg | A）
The order of the output does not matter. The items are separated by tab. 

Time limit:

Hard time limitation: 90 seconds

Standard answer spent time: 61 seconds