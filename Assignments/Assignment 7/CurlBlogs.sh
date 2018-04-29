#!/usr/bin/env bash

for i in {0..497};
 do
	filename='CurlFiles/curlFile'${i}'.txt'
	curl -L -o /dev/null -w %{url_effective} 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117' > ${filename}
	echo ${i}
 done
curl -L -o /dev/null  -w %{url_effective} 'http://f-measure.blogspot.com/' > "CurlFiles/curlFile498.txt"
curl -L -o /dev/null  -w %{url_effective} 'http://ws-dl.blogspot.com/' > "CurlFiles/curlFile499.txt"

