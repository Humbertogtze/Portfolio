For this project I wanted to create a machine learning model that predicted the outcomes of several chess endgames.

If you are not familiar with chess, I will try to briefly explain it. 

In chess, you have different types of pieces with different capabilities. The strongest one, the queen, can be summoned if any of your pawns advances to the enemies rank. Then you have a rook, which is powerful, but not a rival to a queen.

In this case, all the pieces of the board has been removed except 4. Both kings, black's rook and white's pawn. White's pawn is on a7, one step before the final rank. It is assumed that if white summons the queen and retains it, he will win. There are only two outcomes, either whites wins or black manages to draw.

The dataset describe the chess board, it gives whose turn is it as well as multiple other factors such as pieces positioning. 


Now onto the project itself, I first mapped the letters in the dataset to dummy variables using Pandas. Then selected my feature columns and used Scikit Learn to get a Logistic Regression model. Afterwards, I used Matplotlib and Seaborn to plot a confusion matrix.

Data source:
https://archive.ics.uci.edu/ml/datasets/Chess+(King-Rook+vs.+King-Pawn)