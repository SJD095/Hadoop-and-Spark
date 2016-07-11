In this project you will work with discussion forum (also sometimes called discussion board) data. It is one type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things you will do in this project can transfer to other similar projects.

This particular dataset is taken from an online forum similar to the popular StackOverflow forum. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments. If you are not sure how that all looks, please go to StackOverflow and look around!

You shall run the code mostly on your VMs. The dataset is in the file  forum_data.tar.gz. To unarchive it, download it to your VM, put in the data directory and run:

tar zxvf forum_data.tar.gz

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

 

Write a MapReduce program that would output Top 10 tags, ordered by the number of questions they appear in.

Please note that you should only look at tags appearing in questions themselves (i.e. nodes with node_type "question"), not on answers or comments.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. The name of the test data set is student_test_posts.csv.

Run the following command to display your code’s output: $ cat student_test_posts.csv | python mapper.py | sort | python reducer.py

Below you will find the output expected for when using the test data set provided. The output of your code should include all of the rows below, aside from the columns headers. The order of the rows does matter for this question. Tags that tie for the same number of counts can be switched with one another, but the list as a whole needs to show tags starting with the highest count and descending.

Time limit:

Hard time limitation: 60 seconds

Standard answer spent time: 50 seconds