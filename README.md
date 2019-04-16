# directory: xss-game
# Tae Jin Kim (tkim80)
# Hopkins Web Security

DETAILS

This directory has 6 separate folders for each of the levels, a requirements.txt, and a README.

The README contains a basic description of all the files while the requirements.txt contains all of
the necessary imports to run my files.

In order to run each of the levels, run the following commands:
    - python level_1/level1.py
    - python level_2/level2.py
    - python level_3/level3.py
    - python level_4/level4.py
    - python level_5/level5.py
    - python level_6/level6.py

Each of these files run on the local host at port 8000, so please make sure to type the following as
the URL when running the above programs: http://127.0.0.1:8000/. Each of the levels should automati-
cally be redirected to http://127.0.0.1:8000/levelX (where X is the level #) after running. 


REPORT
    Please read ws_hw2_report.pdf in order to obtain a more comprehensive report of what I did.


BUG in LEVEL 6
    Unfortunately, I can not seem to figure out why my code for level 6 is not able to update the page
    right after updating the URL. In order to update the page, you must first change the URL, then you
    must refresh the page. I made very few changes to the original html file, so I ended up concluding
    the error is probably due to the fact that I am using Flask rather than webapp2.