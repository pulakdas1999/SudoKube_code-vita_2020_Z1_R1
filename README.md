# SudoKube_code-vita_2020_Z1_R1
SudoKube  Problem Description  John, a research scholar / Professor / Puzzle solver wants your help in publishing his work on SudoKube on his online blog for his followers and students. A SudoKube is a mixture of Rubics cube and Sudoku. A SudoKube has exactly 6 appearances of every digit from 1 to 9 across the cube, whereas Rubics cube has 6 different colours. As John wants to publish his work in text /document form (no video) he's concerned how he would depict the step by step work of rotation in 2D form. Following are the notions and concepts  John follows: 1. The six faces of the cube are named FRONT, BACK, UP, DOWN, LEFT and RIGHT respectively. 2. Just like a Rubics cube which move in 90 and 180 degrees in both clockwise and anti clockwise directions, so can the SudoKube 3. Any given face of the cube is a 3x3 square matrix whose indices are denoted by (0,0) to (2,2). Diagram below illustrates the same. 4. An elementary move is denoted in the following fashion.  i. If a given face is rotated by 90 degrees clockwise about the axis passing from the centre of the face to the centre of the cube, the move is denoted by the first letter of the name of  the face. ii. If the rotation is anticlockwise by 90 degrees, the letter is followed by an apostrophe ('). iii. If the rotation is by 180 degrees, the letter is followed by a 2.
John wants to test his notations on you. He has given you the initial position of the SudoKube and he has given you a set of operations to be performed on the SudoKube basis his notation.
After applying all the operations, the final SudoKube state should be the same as what John expects. Your task is to apply the operations and print the final SudoKube state.

Constraints
Values in SudoKube will be between 1 and 9
No of moves < 15

Input
• First eighteen lines contain the values of the faces on SudoKube in the order given below
D D D
D D D
D D D
U U U
U U U
U U U
L L L
L L L
L L L
F F F
F F F
F F F
R R R
R R R
R R R
B B B
B B B
B B B

where
o D for Down face
o U for upper face
o L for Left face
o F for Front face
o R for Right face
o B for Back face.

Input contains digits from 1 to 9 instead of letters; letters are displayed for better understanding of the faces and the expected input format
• Nineteenth line contains a sequence of space delimited moves that need to be performed on the SudoKube
Example 1: D F2 R' U - to understand this please refer second example from the Examples section below
Example 2: L2 U B F' D2 R - lets understand how to interpret this set of operations
o L2 means rotate the Left side by 180 degrees
o U means rotate the Up side by 90 degrees clockwise
o B means rotate the Back side by 90 degrees clockwise
o F' means rotate the Front side by 90 degrees anticlockwise
o D2 means rotate the Down side by 180 degrees
o R means rotate the Right side by 90 degrees clockwise

In summary, first eighteen lines denotes the state of the SudoKube, 19th line denotes the operation to be performed on that state and output should be the resulting state.
Output

Print 3x3 matrix corresponding to the order (D, U, L, F, R, B). Between every 3x3 matrix there should be a new line.

Time Limit
1

Examples

Example 1

Input
4 7 1
2 8 7
6 3 5
5 8 3
3 1 6
9 4 2
5 2 4
3 7 8
5 1 9
6 1 4
9 4 8
2 5 7
7 9 1
1 9 6
6 2 8
8 6 3
7 2 5
3 9 4
F

Output
6 1 7
2 8 7
6 3 5

5 8 3
3 1 6
9 8 4

5 2 4
3 7 7
5 1 1

2 9 6
5 4 1
7 8 4

9 9 1
4 9 6
2 2 8

8 6 3
7 2 5
3 9 4

Explanation:

The output shows the state of SudoKube when the front side is rotated clockwise
	5 8 3
	3 1 6
	9 4 2

5 2 4	6 1 4	7 9 1	8 6 3
3 7 8	9 4 8	1 9 6	7 2 5
5 1 9	2 5 7	6 2 8	3 9 4

	4 7 1
	2 8 7
	6 3 5


	5 8 3
	3 1 6
	9 8 4

5 2 4	2 9 6	9 9 1	8 6 3
3 7 7	5 4 1	4 9 6	7 2 5
5 1 1	7 8 4	2 2 8	3 9 4

	6 1 7
	2 8 7
	6 3 5

Example 2

Input
4 7 1
2 8 7
6 3 5
5 8 3
3 1 6
9 4 2
5 2 4
3 7 8
5 1 9
6 1 4
9 4 8
2 5 7
7 9 1
1 9 6
6 2 8
8 6 3
7 2 5
3 9 4
D F2 R' U

Output
2 4 5
3 8 9
5 7 6

4 3 5
2 1 8
8 7 6

9 1 3
3 7 1
3 9 7

1 6 7
8 4 6
4 1 6

1 6 3
9 9 5
4 8 4

5 2 2
7 2 5
9 2 8

Explanation

The above output prints the state of cube after D F2 R' U operation are performed. Here
· D means rotate the Down side by 90 degrees clockwise
· F2 means rotate the Front side by 180 degrees
· R' means rotate the Right side by 90 degrees anti clockwise
· U means rotate the Up side by 90 degrees clockwise
