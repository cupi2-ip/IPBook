docker run --security-opt label:disable  \
   -v /Users/giove/temp/GITProjects/IPBook:/srv/jekyll \
   -p 4000:4000 \
   -it -u 1000:1000 \
   emdupre/jupyter-book
