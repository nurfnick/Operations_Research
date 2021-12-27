#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/nurfnick/Operations_Research/blob/main/Chapters/Chapter10GameTheory.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Game Theory

# ![GAMR THEORY.png](https://raw.githubusercontent.com/nurfnick/Operations_Research/main/Drafts/Game%20Theory/GTImg1.png)
# 
# 
# 
# 

# # Introduction

# It is a branch of mathmatics concerned with the analysis of decision-making and strategy. It is applied in economics,biology and behavioral science. Game theory is used to determine different strategy to compete with one another. Game theory is also used in everyday life to make decision like when to change lanes in traffic, when to cross the road or even when to do your assignment.
# 
# Game theory gained widespread recognition in early $1940's$ when it was applied to the theoretical study of economics by mathematician John Von Newmann and the economist Oskar Morgenstern in their book theory of games and economic behaviors. since then its scopes broadened to co-operative interaction as well as in applied theoretical aspects of social sciences.
# 
# the Nash equilibrium is a decision that does not deviate no matter what the other player chooses. It benefits person A no matter what person B does. Although it is not necessarily the optimal decision for both.
# 
# On the other word, game theory can also be defined as the mathmatical study of decision-making, of conflict and strategy in social situations.
# 
# Applications of game theory is very broad. It is used in various sectors like, Philosophy, Resource Allocation and Networking, Biology, Economics, Politics and more. As in regular life, we used Game Theory in repeated games, bargaining, reputation, equilibrium refinements, industrial organization, contract theory and mechanism/market design
# 
# 
# 
# What motivated us to work on this subject is that none of us really knew what game theory was! We didn't really know how to use it or what it's applications were. So our main driving force was the pursuit of knowledge!
# 
# 
# 
# 
# 

# ### HISTORY OF GAME THOERY

# 
#  In 1921, a French mathematician and politician *Émile Borel (1871–1956)* published several papers on the $Theory$ $Of$ $Games$. He was known as the forgotten father of game theory and famous for his founding work in the areas of measure theory and probability. *Émile Borel* wrote several papers on games of chance and theories of play. Even The acknowledged father of **Game Theory** is *Émile Borel*, A Hungarian-American mathematician *John von Neumann*, who in a series of papers in the 1920s and ’30s established the mathematical framework for all subsequent theoretical developments. During World War II, he was a military strategists in such areas as logistics, submarine warfare, and air defense he drew on ideas that were directly related to game theory. Game theory thereafter developed within the context of the social sciences. Despite such empirically related interests, it is essentially a product of mathematicians. 
# 
# 
# 
#  **DIFFERENT DEVELOPMENT AND MODELS DEVELOPED RELATED TO GAME THEORY**
# 
# 
# **Cournot (1838): Quantity Setting Duopoly**  
# 
# A French economist *Antoine Augustin Cournot (1801-1877)*. He created a economic model called as $Carnot$ $Competition$ used to describe an industry structure in which companies compete on the amount of output of prducts, which they decide on independently of each other and at the same time. He was inspired by observing competition in spring water duopoly. They used $Nash$ $equilibrium$ to claculate equilibrium from cost structure and price function for the best response function in firms.  
# 
# 
# **Zermelo (1913): Backward Induction** 
# 
# This theorem is developed by  *Ernst Zermelo(1871-1953)*, a German mathematician and logician which is related to two players game. It talk about chess or tic-tac-toe which are two player games. That is, either there is a way for player 1 to force a win, or there is a way for player 1 to force a tie, or there is a way for player 2 to force a win which can be proof by induction. It define and informally discuss both perfect information and strategies in such games. This allows us to find $Nash$ $Equilibria$ in sequential games.
# 
# 
# **von Neumann and Morgenstern(1944): zero-sum games**
# 
# Zero sum games is developed by *John Von Neumann(1903-1957)*, a Hungarian-American mathematician, physicist, computer scientist, engineer and polymath, who was also described as pratical joker and *Emile Borel*,a French mathematician. They describe zero-sum game is one in which no wealth is created or destroyed. So, in a two-player zero-sum game, whatever one player wins, the other loses. Therefore, the player share no common interests. There are two general types of zero-sum games: those with perfect information and those without.
# 
# 
# **Flood and Dresher (1950): Experiments**
# 
# This experiment is developed by *Merrill Meeks Flood (1908 – 1991)*, a American Mathmatician and *Melvin Dresher(1911-1992)*, a Polish-born American mathematician. The Flood-Dresher Experiment was a prisoner's dilemma game run 100 times between 2 players. In this case, the game was unfair one of the players had an inherent advantage over the other player, but the payoff matrix layout was still a prisoner's dilemma. This experiment is done down in our example. 
# 
# 
# **Nash (1950): Equilibrium**
# 
# The Nash Equilibrium is a way of optimizing an outcome named after *John Forbes Nash Jr.* However it was first utilized by *Antoine Augustin Cournot* who was a French philosopher and mathematician. We will talk more about this in our theory. 
# 
# 
# **Selten (1965): Dynamic Games**
# 
# *Reinhard Justus Reginald Selten(1930-2016)*, a German economist who won  Nobel Memorial Prize in Economic Sciences through his work in Game theory. It also described as the subgame perfect Nash equilibrium with its emphasis on the difficulty of commitment and on credible plans of action, remains the main concept for the strategic analysis of dynamic games. It has been applied myriad times in diverse models ranging over all social sciences, but also in biology and computer science.
# 
# 
# **Harsanyi (1967): Incomplete Information**
# 
# *John Charles Harsanyi(1920-2000)*, a Hungarian Nobel Prize laureate economist developed a new theory for the analysis of games with incomplete information where the players are uncertain about some important parameters of the game situation, such as the payoff functions, the strategies available to various players, the information other players have about the game, etc. However, each player has a subjective probability distribution over the alternative possibilities.
# 
# 
# **Akerlof, Spence, Stiglitz: first applications**
# 
# This is also known as The Theory of Asymmetric Information in Economics which is developed by  *George Akerlof(1940)*, an American economist , *Michael Spence(1943)*, a Canadian-American economist and Nobel laureate, and *Joseph Stiglitz(1943)*,an American economist and public policy analyst. The three shared the Nobel Prize in economics in 2001 for their contributions.This theory was about the market effects of quality variability and uncertainty have classically been studied in the particular context of asymmetric information,
# focusing on the sellers' expected behavior and the phenomenon of adverse selection.
# 
# 
# **1990s: parallel development of behavioral economics**
# 
# *Richard Thaler(1945)*, an American economist relate Game thoery with behavioral economics which is a relatively new field that combines insights from psychology, judgment, and decision making, and economics to generate a more accurate understanding of human behavior

# ### Theory
# Our main focus of game theory has been the **Nash Equilibrium**. 
# 
# The **Nash Equilibrium** is a way of optimizing an outcome named after John Forbes Nash Jr. However it was first utilized by Antoine Augustin Cournot who was a French philosopher and mathematician. 
# 
# The **Nash Equilibrium** is a very unique way of observing decisions in a very absolute way.A pair of strategies is said to be **Nash Equilibrium** (NE), if the optimal choice of Player A given Player B’s choice coincides with optimal choice of Player B given Player A’s choice. In simple terms, initially neither player knows what the other player will do when deciding or making a choice. Hence NE is a pair of choices/strategies/expectations where neither player wants to change their behaviour even after the strategy/choice of the other player is revealed.
# 
# 
# As you can see the **Nash Equilibrium** is fairly straightforward. It is simple in a sense that each individual always tries to maximize their own outcome. However, in the real world it isn't always absolute or predictable. It is very hard to predict people!
# 
# 
#  Another one of the main ideas we have looked at is dominant strategy. In **Dominant Strategy** there is one optimal strategy for each player irrespective of what strategy the other player adopts. Whatever choice B makes, A should always choose Bottom and whatever choice A makes B should always choose Left.

# ## Examples

# ### Example 1

# Let's Consider the following bargaining problem: 20 dollars needs to be split between Jack and Mac. Mac gets to make an initial offer.
# 
# Jack then gets to respond by either accepting Mac's initial offer or offering a counter offer. Finally, Mac can respond by either accepting Jacks offer or making a final offer.
# 
# If Jack does not accept Mac's final offer both Jack and Mac get nothing. Jack discounts the future at 10% (i.e. future earnings are with 10% less than current earnings while Mac discounts the future at 20%. Calculate the Nash equilibrium of this bargaining problem.
# 
# The key to each of these games is as follows: At any stage, the offer made needs to be acceptable to both parties.
# 
# We need to work backwards: 
# 
# Stage 3: Note that if Jack rejects Mac's offer at this stage, the money disappears. Therefore, Jack will accept anything positive. Mac offers: 20 dollar to herself, 0 dollar to Jack.
# 
# Stage 2: Now, Jack must make an offer that Mac will accept (if the game gets to stage three, Jack gets nothing).Mac is indifferent between 20 dollars in one year and 16 dollars today (she discounts the future at 20%). Jack offers: 16 dollars to Mac, 4 dollars to Himself
# 
# Stage 1: Now, Mac must make an offer that Jack will accept (and is preferable to her – if this is not possible, then she will make an offer jack rejects and the game goes to stage 2).
# 
# Jack is indifferent between 4 dollars in one year and 3.6 dollars today (he discounts the future at 10%). Note that 16.40 is preferred by Mac to  16 in one year. Mac offer 16.40 to herself, 3.60 to Jack.

# ### Example 2

# We will compute Nash equilibria for a simple two player rock-paper-scissor game!
# 
# i. First, we need to creat a payoff matrix for each player. We will start with the first player.         
# ii. The payoff matrix for the second players is the transpose of p2.      
# iii. We create the game object to represent the game.     
# iv. We compute the Nash equilibria for the game using the support enumeration algorithm.    
# v. We iterate over the equilibria and print the profile for each player.

# **Lets do this problem in python**

# In[ ]:


get_ipython().system('apt-get -qq install -y graphviz && pip install nashpy')


# In[ ]:


import numpy as np
import nashpy as nash


# In[ ]:


p1 = np.array([
    [0, -1, 1],   #rock payoff
    [1, 0, -1],   #paper payoff
    [-1, 1, 0]    #scissors payoff      
])


# In[ ]:


p1 = np.array([
    [0, -1, 1],   #rock payoff
    [1, 0, -1],   #paper payoff
    [-1, 1, 0]    #scissors payoff      
])
p2 = p1.transpose()
rock_paper_scissors = nash.Game(p1, p2)
equilibria = rock_paper_scissors.support_enumeration()
for p1, p2 in equilibria:
  print("Player 1", p1)
  print("Player 2", p2)


# Essentially this equates to the fact that no matter what you choose your odds of winning will be 33% or one in three. Of course this is also true with losing and tying. As long as you are completely random. If you just choose rock every single time then ofcourse your strategy would become predictable, the other person will know to throw paper every time and you will lose every time!

# ### Example 3
# $$PRISONER$$ $$DILEMMA$$
# 
# It is also called as interrogation room problem or Flood-Dresher Experiment. 
# This game was widely studied and used in social science.
# 
# lets imagine, pato and babu were arrested and suspected to be in connection with a certain robbery. The prosecution has enough evdience to convict them for tresspasing but the prosecution beleived they carried out the robery. Now the DA comes in and puts them in seprate rooms where they cannot see each other or hear each other and starts the interrogation. DA wants to put them each behind bars for 8 months.
# 
# The conditions for outcomes given by district attorney for pato and babu were:
# 
# if either of  the two people confess they can charged with robery. if one confess's but the other doesn't the one who didn't will go to jail for 12 months and the person who confess's will go free .
# 
# if both confess, both are going to jail for 8 month each.
# 
# if they do not confess, both will be charged with trasspassing and get 1 month of jail time.
# 
# ---
# check out this table
# 
# ###Pato vs Babu
# 
# 
# |CONFESS    |   LIE    |
# |-----------|----------|
# | (-8,-8)   |  (0,-12) |
# | (-12,0)   |  (-1,-1) |
# 
# ----
# According to **NASH EQUILIBLIUM** which gives optimal outcome of a game, they both will confess and get 8 months each of jail time.
# 
# But **DOMINANT STRAGTEGY** which explains the optimal move for any player regardless of how the other player acts, it then gives the outcome of someone going to jail for 12 months and rather then none. 
# 
# 

# **Lets do this problem in python**

# In[ ]:


get_ipython().system('pip install nashpy')


# In[ ]:


import nashpy as nash
import numpy as np


# **I am going to make a non-zero sum game representing the prisoner's dilema!**

# In[ ]:


A = np.array([[-8,0],[-12,-1]])
B = np.array([[-8,-12],[0,-1]])

rps = nash.Game(A, B)


# In[ ]:


rps


# In[ ]:


eqs = rps.support_enumeration()

list(eqs)


# In[ ]:


iterations = 10

play_counts = rps.fictitious_play(iterations=iterations)

for row_play_count, column_play_count in play_counts:

    print(row_play_count, column_play_count)


# **What if I play the game randomly. Player 1 only snitches 10% of the time. But player 2 always snitches**

# In[ ]:


p1 = [.1,.9]
p2 = [1,0]

rps[p1,p2]


# **Player 1 is going to average 11.6 months in the pokey but player 2 less than a month!**

# In[ ]:


play_counts = rps.stochastic_fictitious_play(iterations=iterations)

for row_play_count, column_play_count in play_counts:

    print(row_play_count, column_play_count)


# ## Problems
# 

# ### Problem 1 

# 
# 
# Assume you are trying to buy a car. The best outcome for you is to get the car as cheap as possible for instance at cost to the company. The best outcome for the Dealer is going to be to get you to pay above sticker price for the car. 
# 
# Let’s say the salesman tries to get you to pay 40,000 for a car that cost the dealership 30,000 to get on the lot and sell. Ideally you would want to know exactly how much they paid for it so you could get it for that price. But in the real world the salesman won’t tell you how much he needs out of the car. However, you also have power in this situation because the dealer doesn’t know how much you are willing to pay for the car. 
# 
# Ideally you would meet exactly in the middle so each party leaves happy. That is not how buying a car works though. There is always a winner and a loser and the dealership wins the majority of the time. The dealership has the most power because they get the last say in what price the car is sold for.However, in reality you will never buy a vehicle for what the dealer buys it for.

# ### Problem 2

# It is finals week and you and your closest friend Bob haven't studied at all. You don't want to fail so you have devised a devious plan to steal the proffesors answer sheet! You and Bob sneak in late at night after office hours into Dr. Jacobs office and just as you pull the answers out of his desk the light flips on! Dr. Jacob is standing behind you and Bob. Now Dr. Jacob is not happy one bit. He doesn't like cheaters! But Dr. Jacob is a whimsical man so he offers you both an out. He says "Listen I know one of you thought of this idea and the other just taged along so I will give you both one opportunity to save your skin. If one of you comes forward I will spare you and allow you to take the final anyways but I will have the silent party expelled! If neither of you comes forward I will allow you both to take the exam but I will only give you half of the points that you would have scored. Finally if you both come forward I will award you both a 0 for your final." You look at Bob nervously not knowing what you should do. What do you do?
# 
# In this scenario what would be the Nash equilibrium?
#  
#  In this scenario what would be the dominant strategy?

# ### Problem 3

# It is spring break. You and your best bud Bob are ready to go out on the town and enjoy life! However, disaster strikes! There is an ice storm and a terrible one at that. The power is out and the roads are much too slick to go out. You and Bob reluctantly dust off your oil lantern and look around for something that can pass the time. You find an ancient deck of cards and decide to play a game. But this deck of cards no longer is a full deck. Instead you have 6 cards. 2 red 5's a red 3 a black 5 a blue 3 and a black 8. You shuffle all 6 cards and divy them out equally. The rules you decide on are as follows. You and Bob both play a card from your hand. If the two numbers match bob wins the round. If the colors match you win the round. If both the color and the number match you both win the round. If nothing matches you both lose. The deck is shuffled and you have a black 5 a red 5 and a black 8. What do you play on your first round?
# 
# What card should you play as the dominant strategy?
# 
# What card should be played to garuntee a nash equilibrium?

# ### Problem 4

# It is Summer finally! You are hanging out with your best pal Bob walking through the woods when you stumble upon a treasure chest! Yet again your friendship is tested. You both want to keep all of the gold and jewels to yourselves. Seeing no end to the squabbling you and bob decide to let chance decide who gets the lions share of the treasure and who walks away a sad broken husk of a human. You remember that you have brought dice with you and decide this is the best way to determine the winner. You will both roll a single die and whoever rolls the highest number wins. The two dice that you have are very odd to say the least. They are both 6 sided die, however the numbers are a bit peculiar. One die has 3 faces with the number 4 and the other 3 faces with the number 2. The other die has 2 faces with a 1 2 faces with the number 3 and finally 2 faces with the number five. Bob says since they are your dice you should get first pick on which die you get. Bob will roll the die you do not chose. 
# 
# Which die do you chose for a dominant strategy?

# ### Problem 5

# Everyone has played rock, paper, scissors before. The rules are simple: Each individual can choose one among rock, paper, or scissors. Rock beats scissors, but rock is beaten by paper. Paper beats rock, but paper is beaten by scissor. Scissors beats paper, but scissors is beaten by rock. In any game if both players get the same choice then it will be a draw. Compute the Nash Equilibria for this two-player game.
# 

# (Answer for this problem is in example 2)

# ### Problem 6

#  Each individual owner of two bars charges its own price for a beer, either 2, 4, or 5 dollars. We can neglect the cost of obtaining and serving the beer. It is expected that 6000 beers every month are drunk in the bar by customers, who choose one of the two bars randomly, and 4000 beers per
# month are drunk by natives who go to the bar with the lowest price, and split evenly in case both bars
# offer the same price. What prices would the bars select?

# ### Problem 7

# Babu and Pato have robbed a bank and have been arrested. They are interrogated individually in diffirent room. Babu and Pato have the option to confess (move C) or to remain silent (move S).
# The police have little evidence, and if both remain silent they will be sentenced to one year on a minor
# charge. Therefore the police interrogators propose a deal: if one confesses while the other remains
# silent, the one confessing goes free while the other is sentenced to three years. However, if both talk,
# both will still be sentenced to two years. If each player’s payoff is 3 minus the number of years served
# in jail.
# Draw payoff bimatrix for this problem.
# 

# ### Problem 8

# Bob and Sam are bargaining over how to split $10. Each player names an amount si, between 0 and 10.The choices are made simultaneously. Each player's payoff is equal to his own money payoff. 
# 
# (a) In the first case, if s1+s2>10, then both get zero and the money is gone.
# 
# (b) In the second case, if s1+s2>10 and the amounts named are different, then the person who names the smaller amount gets that amount and the other person gets the remaining money. If s1+s2>10 and s1=s2, then both players get $5.
# 
# (c) In the third case, the games (a) and (b) must be played such that only integer dollar amounts can be named by both players.
# 
# Determine the pure strategy Nash Equilibria for all games (a) - (c)

# ### Problem 9

# 
# 
# #### **Thomas vs Changretta**
# Mr. Thomas and Mr. changretta are betting on horses in horse race in Birmingham.The table below is the chances for the bet they will place on each horse. 
# Find the Nash Equilibrium.
# 
# |Thomas vs Changretta  |A    |   B    |
# |--|-----------|----------|
# | A| (3,2)   |  (2,1) |
# | B| (4,3)   |  (1,4) |

# ### Problem 10

# You and your collegue have to write some code for a client. You collegue thinks that they could write it in C faster but you think you can write it faster in python.You think you can write the python code four times faster than in C language. You write C with speed 1 and python with speed 4. Your colleague can write C slightly faster than python. They can write the code at the speed 3 and Python with speed 2.If both agreed, then you write code at the speed you predicted, but if you disagree, then productivity of the faster programmer is reduced by 1. The question is which language should you choose for the project?
# 
# 

# #### Colleague vs You
# 
# |  Colleague vs You    |C    |   Python    |
# |------|-----------|----------|
# |C     |  (3/1)   |  (3/2) |
# |Python|  (2/1)   |  (2/4) |

# ## **Project Idea**

# A fun way to demonstrate **Game Theory** would be to have students group off into pairs of two. Give each group 5 marbles,2 scraps of paper and explain the rules as follows. If both contestants choose to share then they each get 2 marbles and the remaining marble is lost to the game master. If contestant 1 chooses to share but contestant 2 chooses to steal then contestant 2 gets all 5 marbles. If both contestants choose to steal then 3 marbles go to the game master and each contestant gets a single marble. Give the players a timer for how long they can talk and how long they have to make a decision. Or you could simply take away the ability to talk all together and only give them time to make a decision. Have them write their decision on the scrap paper. You could play this for a few rounds and award either bonus points or candy based on how many marbles each player gained in total!

# ## References

#  1. Game Theory concepts with application in Python using Nashpy Krishnan, Mythili. “Game Theory Concepts with Application in Python Using Nashpy (Part 1).” Medium, 16 Nov. 2020, towardsdatascience.com/game-theory-in-python-with-nashpy-cb5dceab262c.
#  2. 
#  Nash Equilibrium “Nash Equilibrium.” Investopedia, 3 Mar. 2021, www.investopedia.com/terms/n/nash-equilibrium.asp.
#  "Game Theory.” Funk & Wagnalls New World Encyclopedia, Jan. 2018, p. 1; EBSCOhost, 0-search-ebscohost-com.library.ecok.edu/login.aspx?direct=true&db=funk&AN=ga010500&site=eds-live&scope=site.
#  3. 
#  Multi energy conversion based on game theory He, Jianjia, et al. “Multi-Energy Conversion Based on Game Theory in the Industrial Interconnection.” PloS One, vol. 16, no. 1, Jan. 2021, p. e0245622. EBSCOhost, doi:10.1371/journal.pone.0245622.
#  4. 
#  Krishnan, Mythili. “Game Theory Concepts with Application in Python Using Nashpy (Part 1).” Medium, 16 Nov. 2020, towardsdatascience.com/game-theory-in-python-with-nashpy-cb5dceab262c.
#  
#  5.  Research, Hkt. “Cournot Duopoly Model (1838).” HKT Consultant, 13 Jan. 2021, sciencetheory.net/cournot-duopoly-model-1838.
#  6. “ECON 159 - Lecture 15 - Backward Induction: Chess, Strategies, and Credible Threats | Open Yale Courses.” OYC YALE, 2008, oyc.yale.edu/economics/econ-159/lecture-15.
#  7. Zero-Sum Games.” STANFORD, 1999, cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/zero.html.
#  8. “The Ideas of Reinhard Selten.” VOX, CEPR Policy Portal, 2016, voxeu.org/article/ideas-reinhard-selten.
#  9.  Harsanyi, John. “EconPapers: Games with Incomplete Information Played by ‘Bayesian’ Players, I-III Part I. The Basic Model.” John Harsanyi, 1967, econpapers.repec.org/article/inmormnsc/v_3a14_3ay_3a1967_3ai_3a3_3ap_3a159-182.htm.

# ### Authors

# Principal authors of this chapter were:[Ashok S. Poudel](https://github.com/ashpou1), [Bidhan Subedi](https://github.com/bidhan7), & [James Norman](https://github.com/James-rg)

# In[ ]:




