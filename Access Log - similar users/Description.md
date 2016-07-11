In this final project, the data you are going to analyze is the dataset consists of requests made to the 1998 World Cup Web site. 
The data format is described at http://ita.ee.lbl.gov/html/contrib/WorldCup.html. We will only use part of the full dataset.
Here are some samples:
34600 - - [30/Apr/1998:21:30:17 +0000] "GET /images/hm_bg.jpg HTTP/1.0" 200 24736
232 - - [30/Apr/1998:21:30:53 +0000] "GET /images/hm_bg.jpg HTTP/1.0" 200 24736
282 - - [30/Apr/1998:21:31:12 +0000] "GET /images/hm_bg.jpg HTTP/1.0" 200 24736
9719 - - [30/Apr/1998:21:31:19 +0000] "GET /french/splash_inet.html HTTP/1.0" 200 3781
9719 - - [30/Apr/1998:21:31:22 +0000] "GET /images/hm_nbg.jpg HTTP/1.0" 304 -
252 - - [30/Apr/1998:21:31:27 +0000] "GET /images/hm_bg.jpg HTTP/1.0" 200 24736
9719 - - [30/Apr/1998:21:31:29 +0000] "GET /images/hm_brdl.gif HTTP/1.0" 304 -
9719 - - [30/Apr/1998:21:31:29 +0000] "GET /images/hm_arw.gif HTTP/1.0" 304 -
9719 - - [30/Apr/1998:21:31:32 +0000] "GET /images/nav_bg_top.gif HTTP/1.0" 200 929
9719 - - [30/Apr/1998:21:31:43 +0000] "GET /french/images/nav_venue_off.gif HTTP/1.0" 304 -
9719 - - [30/Apr/1998:21:31:44 +0000] "GET /french/images/nav_hosts_off.gif HTTP/1.0" 200 1139
 
The first item in each line is the user index (identified by the IPs. The real IP is removed for privacy concern).
 
To assist your task, we have built a url dictionary file that maps each URL to an index. This dictionary is provided to you by url_dict in the main function. Note: due to unicode problem, not all urls in the log file will find the entry in url_dict. You can ignore such urls.
 
0 /images/home_intro.anim.gif
1 /images/home_bg_stars.gif
2 /images/home_fr_phrase.gif
3 /images/nav_bg_top.gif
4 /images/home_logo.gif
5 /images/logo_cfo.gif
6 /images/home_eng_phrase.gif
7 /english/index.html
8 /english/frntpage.htm
9 /images/hm_f98_top.gif
10 /images/team_hm_concacaf.gif
11 /images/team_hm_afc.gif
12 /images/team_hm_caf.gif
13 /english/playing/mascot/mascot.html
14 /images/home_tool.gif
15 /english/images/comp_bu_stage1n.gif
16 /english/images/comp_bu_stage2n_on.gif
17 /images/comp_stage2_brc_top.gif

....

 
Now your task is to find top-1000 pairs of users (identified by their user_index) whose visited URLs are the most similar. The similarity is measured by Jaccard coefficient.  Formally, the Jaccard coefficient between a pair of users A, B is defined as: 
|the set of URLs visited by both A and B| / |the set of URLs that are visited by either A or B|
 
The output format shall be "Jaccard-similarity-value  user_idx1  user_idx2" in each line. For example:
0.90123  123  2312

0.81232 2343  45413

....

....

 

 

Requirement:

Pairs of users who visit the same set of URLs (that is, the jaccard similarity is 1.000) are ignored. These users are likely the same.
Only users who visit 10 or more urls are considered. 
Your answer can have a limited amount of false positives/negatives (that is, not exactly the same as the standard answer).  
 

Note:

Items in each line are separated by ''\t"
The list is ordered by the jaccard-similarity-value, from high to low.
For each pair, the smaller user index is listed first.
The jaccard similarity value is accurate to five decimal places. For example: 1.00000, 