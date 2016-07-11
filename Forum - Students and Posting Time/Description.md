In this project you will work with discussion forum (also sometimes called discussion board) data. It is one type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things you will do in this project can transfer to other similar projects.

This particular dataset is taken from an online forum similar to the popular StackOverflow forum. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments. If you are not sure how that all looks, please go to StackOverflow and look around!

There are 2 files in the dataset. The first is "forum_nodes.tsv", and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in double quotes. You can find the field names in the first line of the file "forum_node.tsv". The ones that are the most relevant to the task are:

"id": id of the node
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
"tagnames": space separated list of tags
"author_id": id of the author
"body": content of the post
"node_type": type of the node, either "question", "answer" or "comment"
"parent_id": node under which the post is located, will be empty for "questions"
"abs_parent_id": top node where the post is located
"added_at": date added
The second table is "forum_users.tsv". It contains fields for "user_ptr_id" - the id of the user. "Reputation" - the reputation, or karma of the user, earned when other users upvote their posts, and the number of "gold", "silver" and "bronze" badges earned. The actual database has more fields in this table, like user name nickname, bio (if set) etc, but we have removed this information here.

Task1: Students and Posting Time

We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. These are usually chosen from students who already have shown that they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.

In this exercise your task is to find for each student: what is the hour during which the student has posted the most posts. Output from reducers should be:

author_id    hour
For example:

13431511\t13
54525254141\t21
If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

Note: In order to find the hour posted, please use the added_at field and NOT the last_activity_at field.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. The name of the test data set is student_test_posts.csv.

Run the following command to display your code’s output: $ cat student_test_posts.csv | python mapper.py | sort | python reducer.py

Below you will find the output expected for this exercise when using the test data set provided. The output of your code should include all of the rows below, aside from the columns headers, but the order of the rows may be switched around.

Student ID |  Hour

100000005   1

100000066   1

100000066   5

100002460   12

100003192   8

100003268   15

100004467   12

100004467   20

100004819   4

100005156   17

100007808   12

100008254   22

100010128   14

100012200   5

100019875   5

100020526   14

100071170   12



Time limit:

Hard time limitation: 60 seconds

Standard answer spent time: 28 seconds