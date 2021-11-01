<p align="center">
	<img width="250" src="https://dailycandidnews.com/wp-content/uploads/2019/10/sphe-21_2008-Full-Image_GalleryCover-en-US-1484000130237._UY500_UX667_RI_VnHhcIo852m4Dj7aUBcsnVlucmitZAou_TTW_.jpg">
</p>

<!-- About the project -->
## About the project
Most casino games have randomness as arguably its biggest element of the game, which leads to some to believe the concept of luck as superstition to varying degrees. However I personally believe Blackjack has room for skill and strategy more than any other well known casino game. Thus I decided to create this project of an AI for Blackjack. My inpsiriations came from both the concept of winning money on a short amount of time (gambling), and the feature film basaed on the same game, 21, released in 2008, and directed by Robert Luketic.

The project utilizies a created model to attempt to win every Blackjack game. There is not (yet) a way the user can interact with the games while they play. Until further improvements, for now the program only involves 1 dealer, and 1 AI player. SKlearn and Scipy is used to develop the algorithm for the AI. Joblib is used for saving the AI model. Pandas is used to help format and organize the data for the model.

<!-- Built with -->
##  Built with 
* [Python 3.7.4 32-bit](https://www.python.org/downloads/release/python-374/)
* [Scipy 1.7.1](https://www.scipy.org/)
* [Joblib 1.0.1](https://joblib.readthedocs.io/en/latest/)
* [Pandas 1.3.3](https://pandas.pydata.org/pandas-docs/stable/index.html)
* [SKlearn 1.0](https://scikit-learn.org/stable/)

<!-- Getting started -->
## Getting started
### Installation
Clone the repository
   ```sh
   git clone https://github.com/ArthurDayot/BlackjackAI.git
   ```
Install required packages
   ```sh
   pip install -r requirements.txt
   ```
### Running the game
Command to open a running window of the game
   ```sh
   $py blackjack.py
   ```
### Creating a new model
Command to create a new model file
   ```sh
   $py generate_dataset.py
   ```
### Testing the winrate of the model
Command to test the winrate of the model
   ```sh
   $py win_rate.py
   ```

<!-- Future improvements -->
## Future improvements
- Fixing issue with compatibility between 32-bit and 64-bit versions of python
- Option for multiple players of AI
- Option for user to join in as a player
- Selection of # of decks
- Betting system with chips
- More photogenic GUI
- Implement a separate model that follows "blackjack perfect strategy" for comparison against the AI(s)