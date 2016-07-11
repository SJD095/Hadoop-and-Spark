In this assignment, we will use Wikipedia traffic statistics data obtained from http://aws.amazon.com/datasets/4182 . To make the analysis feasible (within the short timeframe of the exercise), we only took a small sample.

The data files contain traffic statistics for all pages in a specific hour. In total there are nine input files, each with around 200MB data:

smart_programmer/wiki/part-00097
smart_programmer/wiki/part-00098
smart_programmer/wiki/part-00099
smart_programmer/wiki/part-00100
smart_programmer/wiki/part-00101
smart_programmer/wiki/part-00102
smart_programmer/wiki/part-00103
smart_programmer/wiki/part-00104
smart_programmer/wiki/part-00105
 

The content of each file is like the follows:

 

20090507-040000 aa ?page=http://www.stockphotosharing.com/Themes/Images/users_raw/id.txt 3 39267

20090507-040000 aa Main_Page 7 51309

20090507-040000 aa Special:Boardvote 1 11631

20090507-040000 aa Special:Imagelist 1 931

 

Each line, delimited by a space, contains stats for one page. The schema is:

 

The <date_time> field specifies a date in the YYYYMMDD format (year, month, day) followed by a hyphen and then the hour in the HHmmSS format (hour, minute, second). There is no information in mmSS. The <project_code> field contains information about the language of the pages. For example, project code “en” indicates an English page. The <page_title> field gives the title of the Wikipedia page. The <num_hits> field gives the number of page views in the hour-long time slot starting at <data_time>. The <page_size> field gives the size in bytes of the Wikipedia page.

 

Your task in this assignment is to write a spark program to find the top-10 frequently visited pages. The visit count is summed across the whole dataset in the nine input files. 

Note: Pages with different project_code are considered different pages.

 

The output shall be like:

aa  XXX    100000

aa  YYY     53123

en  ZZZ     23112

…

 

Note:

The items in each line shall be separated by "/t"

 

The spark program shall consist of two python code file. One is "driver.py", which is given to you by the smart_programmer system. You can read its code in the assignment page. "driver.py" will create the spark context and load the input data files as intial RDDs, then pass these input RDDs to the function "main" that shall be written by you in "main.py"

To output the result, simply use "print" to print the result in stdout in the main function.