# py2048
-----------------------
Command Line Arguments
-----------------------
Following two arguments need to be passed for the start of the game:-
--n - size of the board game (should be an integer)
--w - final winning target number of the game (should be an integer)

----------
Functions
----------
-new_tile:
   Adds the tile '2' at a random index at the start of every new move.

-reverse:
   inverts the row/matrix required before execution of movement.

-game_transpose:
   forms a new 'transpose' matrix

-tile_move:
   if two adjacent elements of a particular column are same (or zero) then those tiles are merged
   and every element following those tiles is pulled one tile up until there are no zeros between 
   any two tiles. Also, if two adjacent tiles are unequal and non-zero or if the column does not 
   have any two adjacently equal tiles, then the particular tile or the whole column (respectively)
   is skipped.

-play_move:
   Adjusts the matrix (transpose/reverse) before the execution of movement according to the input move.

-win_check and gameover_check:
   Checks if the user has reached the targeted number or if there are no further moves possible.
 
-------------------------------------
De/re-structuring matrix for movement
-------------------------------------
-The keys 'a,w,d,s' facilitate the left, up, right and down movement respectively.
Here, upward is taken as the basic move and all other moves are executed with respect to it.

-For 's' the matrix is simply inverted and and the function performs the upward movement
which is then inverted again to gain back the original matrix.

-For 'a' the matrix is transposed upon which the upward movement is executed after which it 
is detransposed again.

-For 'd' the the matrix is first inverted, transposed and then detransposed and inverted back
again after the upward movement is executed.

-------------
modules used
-------------
-random : for spawning 2s
-os : for clearing screen after every move
-numpy : for creating an initial matrix
-argparse : for command line inputs
-time (sleep) : for having a time space of 1s after displaying the message "INAVLID MOVE"


