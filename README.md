# OrderingAlgorithm
Exhibition paintings arrangement algorithmic problem

You have an exhibition opening. This one is very special, the attendees are robots and have very specific tastes. You are in charge of ordering the paintings in a very large corridor where the robots will look at them. To satisfy them, you have to follow some basic rules.

You are given a list of paintings of types portrait and landscape with ids and specific keywords describing the paintings in the input files.You have to put these painting in frameglass and arrange them to get the best score from the robots.A frame glass can containone landscape or two portraits.


The scoring rules:
For two subsequent frameglass Fi and Fi+1, the local robotic satisfaction is the minimum (the smallest number of the three) of the following three (3) integers :
1 The number of common tags between Fi and Fi+1 2 The number of tags in Fi but not in Fi+1
3 The number of tags in Fi+1 but not in Fi.

The script bestScore is achieved the best score but compromises on time. The script bestTime achieves a nominal score in a short time.
    
