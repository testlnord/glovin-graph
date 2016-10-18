# Using GLoVe for graph drawing

read this:

http://textminingonline.com/getting-started-with-word2vec-and-glove-in-python

and

https://github.com/maciejkula/glove-python

## getting data

I got data from data.stackexchange.com with query:
```
select pt1.tagid, pt2.tagid, count(*) from posttags as pt1
inner join posttags as pt2 on pt1.postid = pt2.postid where pt1.postid in
( select id from posts where tags like '<logarithm>')
group by pt1.tagid, pt2.tagid
```


note for myself:

already many people draw SO networks:
* https://github.com/stared/tag-graph-map-of-stackexchange/wiki
