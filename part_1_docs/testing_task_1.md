### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# The __init__ function is missing here

  def check_for_ace(self, card):
    # The below line should have "==" instead of "=" to check for equality
    if card.value = 1:
      return True
    # The below line is missing ":" after "else"
    else
      return False
   
# The below line incorrectly spells "def" as "dif", and is missing a comma after card1
  dif highest_card(self, card1 card2):
  # The if/else code block below should be intended as it is inside a function
  if card1.value > card2.value:
  # The below line should have "card1" instead of "card", as "card" is not one of the parameters
    return card
  # The below line should be an elif statement, otherwise card2 will be returned even if both cards have the same value
  else:
    return card2
  

# The below block of code should be indented as it is part of the CardGame class
def cards_total(self, cards):
  # The below line should define the "total" variable, e.g. "total = 0"
  total
  for card in cards:
    total += card.value
    # the below line should be outside of the for loop (i.e. less indented), otherwise the for loop will end after adding only one card value
    return "You have a total of" + total
  
```
