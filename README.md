# Blackjack

python version 3.8.9 was used to complete this task

## setup environment
```
make init
```

## run tests
```
make test
```

## run app
```
make run
```

## format code
```
make format
```

### Current Rules
- Each player takes two cards each from the top of a randomly shuffled deck
    - You take the first two cards, Bob takes the next two
- Calculate the total sum of each players cards
    - Numbered cards have the value on the card
    - Jack (J), Queen (Q) and King (K) each counts as 10 points
    - Ace (A) counts as 11 points
- If either player has 21 points - blackjack - that player wins the round
- Otherwise continue drawing cards following the following rules:
    - You draw cards first until
        - the sum of your cards is 17 or higher
        - if you exceed 21 points you loose without Bob having to draw more cards
    - Bob draws cards until
        - the sum of his cards is higher than yours
        - if his cards exceed 21 points he looses


### Furthering this application
- add post method to specify number of players & names
- add the ability for Ace to be valued as 1 / 11
- add a gui
- cache the deck call & implement shuffle functionality
- add docker image & have tests and app run from container
- create infrastructure as code for automated release into cloud
- add more verbose logging
