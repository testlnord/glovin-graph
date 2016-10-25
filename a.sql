SELECT
  t1.tagname AS tag1,
  t2.tagname AS tag2,
  count(*)   AS post_count
FROM posttags AS pt1
  INNER JOIN
  posttags AS pt2 ON pt1.postid = pt2.postid
  INNER JOIN
  tags AS t1 ON t1.id = pt1.tagid
  INNER JOIN
  tags AS t2 ON t2.id = pt2.tagid
WHERE pt1.postid IN
      (SELECT id
       FROM posts
       WHERE tags LIKE '%<logarithm>%')
GROUP BY t1.tagname, t2.tagname