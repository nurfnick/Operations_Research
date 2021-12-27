#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/dhirajbbasnet/Operations_Research/blob/main/Chapters/Chapter7Queuing.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Queuing Theory
# 
# 
# 
# 

# ## Introduction
# 
# 
# 
# 
# 

# This project is a research on queuing process. In this project we go through the basic idea of how queuing process works. We also go through some of the simple mathematical problems. Python programming language has been used for solving math problems in this project. We will be utilising necessary packages in python to demonstrate our problem and solve it. 
# 
# 
# 

# ##Theory
# 
# ###Queue
# Queue is a line or sequence of people or vehicles awaiting their turn to be attended to or to proceed.(Shortle, J. F., Thompson, J. M., Gross, D., & Harris, C. M., 2018)
# The simplest example of a queue is the typical line that we all participate in from time to time. We wait in a line for a movie, we wait in the check-out line at a grocery store, and we wait in the cafeteria line. Well-behaved lines, or queues, are very restrictive in that they have only one way in and only one way out. These queues must be managed and organized properly; this is where Queuing theory comes in.
# 
# ###Queuing Theory
# 
# ![Blank diagram.png](data:image/png;base64,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)
# 
# Queueing theory is the mathematical study of how line is form, how it functions (Shortle, et.al, 2018). Queuing theory scrutinizes the entire system of waiting in line, including elements like the customer arrival rate, number of servers, number of customers, capacity of the waiting area, average service completion time, and queuing discipline. The Queuing Theory is concerned with studying all the various dynamics of lines – or “queues” – and how they may be made to operate more efficiently.  In other words, Queuing theory is the study of queues and the random processes that characterize them. It deals with making mathematical sense of real-life scenarios.
# 

# ## Motivation

# Queuing theory is used in our everyday life. Just by knowing a basic knowledge of queueing theory, life can be much easier and convenient. 
# In library queuing theory is used to organize collection of books, and some special materials like audio or visual materials.
# A queuing system helps minimizing the waiting time of patients and maximizing the utilization of the servers in hospitals.
# The capability of these systems can have an important result on the quality of human life and productivity of the process. We have all been in a situation of waiting in line. This process is more common where areas are more congested meaning places with large number of people. We basically must wait in line for everything and every day. We wait in line in our cars in jams or at checkout counters in our grocery stores, So queuing is a model of waiting in lines.
# Queuing systems are successfully used for the performance analysis of different systems such as computer, communications, transportation networks and manufacturing. (Bhat, U. N., 2015) 
# In easy words, a queuing system consists of customers arriving for a service and waiting if the service is not provided immediately and leaving the system as soon as they are served. Customer does not just mean people here. For instance, it could be an airplane waiting in line for take-off, or a computer program waiting to be run.
# 
# 

# #Historical information about queuing theory

# Queueing theory was developed to predict the behavior of systems that provide service for randomly arising demands. This does not include unnatural demands. The earliest problems that were studied were of telephone traffic congestion. The investigator was a **Danish mathematician, A. K. Erlang**. He worked towards analyzing telephone traffic congestion with a goal of satisfying the randomly arising demand for the services of the Telephone exchange. Queuing theory was first introduced in the early 20th century.(Shortle, et.al, 2018)
# 
# Erlang worked for the Copenhagen Telephone Exchange and wanted to analyze and optimize its operations. He sought to determine how many circuits were needed to provide an acceptable level of telephone service, for people not to be “on hold” (or in a telephone queue) for too long. He was also curious to find out how many telephone operators were needed to process a given volume of calls.
# The first paper on queuing theory, “The Theory of Probabilities and Telephone Conversations” was published in 1909 by A.K. Erlang, now considered the father of the field. His work with the Copenhagen Telephone Company is what prompted his initial foray into the field. He pondered the problem of determining how many telephone circuits were necessary to provide phone service that would prevent customers from waiting too long for an available circuit. In developing a solution to this problem, he began to realize that the problem of minimizing waiting time was applicable to many fields, and began developing the theory further.(Shortle, et.al, 2018)
# Erlang’s switchboard problem laid the path for modern queuing theory.
# 

# ## Problem 1
# 
# The main project that we are working on is the queueing system of Mc Donalds. If we have ever noticed how the drive thru system of Mc Donald's works, most locations have two lines leading up to the ordering booth. The lines later merge into one as they move through the payment window and serving window. Moreover, the server suggests some customers to park at a designated spot to keep the queue moving. So, we will be modelling the queueing system of Mc Donald's and figure out why most locations are constructed in that way.
# 
# We will be using the "ciw" package to demonstrate the queue system which is a python package which makes our tasks a lot easier to model queues. 
# 
# We will start by installing the package first.

# In[ ]:


pip install ciw


# Let's import the ciw package now.

# In[ ]:


import ciw


# Now we will create a network to model the queueing system. Note that this model consists of only one server, one cashier and one server. This does not represent the designated parking spot. In other words, we have only 3 nodes. We have the following assumptions for the model:
# 1. Every hour, about 45 customers arrive to the drivethru and get into the line
# 2. There are no arrivals at any other part of the drivethru since it is a queue.
# 3. For the service distribution, we assume that an order is made every 10 minutes.
# 4. The cashier processes one payment every minute.
# 5. The server serves one order in 2 to 6 minutes assuming that smaller orders take less time and some larger orders take more
# 
# Notice that the 3 x 3 matrix named routing represents the overall model.
# 

# In[ ]:


N = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(0.75), # 45 customers arrive every hour
                             ciw.dists.NoArrivals(), #No arrivals at the other nodes
                             ciw.dists.NoArrivals()],
    service_distributions = [ciw.dists.Exponential(0.5), #1 order is made every 10 minutes
                             ciw.dists.Exponential(1.0),  #A cashier takes one payments every minute
                             ciw.dists.Uniform(2,6)],  #A server serves one order in 2 to 6 minutes   #Customer exits the queue
    routing = [[0.0, 1.0, 0.0],  #The matrix for the network
               [0.0,0.0,1.0],
               [0.0,0.0,0.0]],
    number_of_servers = [1,1,1] #Number of servers
)


# Now we will calculate the wait times for the model. We will run the simulation 20 times and calculate the average to get the best representation of wait times. Moreover, we will run the simulation for a period of 180 minutes. Notice that the parameter we have provided is 200 instead of 180. This is to give some cool down time to take some customers out of the queue who are already in there. 

# In[ ]:


average_waits = []
for trial in range(20):
  ciw.seed(trial)
  Q = ciw.Simulation(N)
  Q.simulate_until_max_time(200)
  recs = Q.get_all_records()
  waits = [r.waiting_time for r in recs]
  mean_wait = sum(waits)/len(waits)
  average_waits.append(mean_wait)
print (sum(average_waits)/len(average_waits))


# So, it looks like average wait times for customers at Mc Donalds is **23.17 minutes** according to our calculations. Like we discussed above, this wait time is in case we have only one ordering booth, one server and one cashier.

# In the above code, we can easily change the number of servers and see what kind of difference do they make in the system. We can also calculate how many customers passed through the system after receiving the service within the given time frame. To calculate that we will see how many records lie at node 3 which is our last node since we can be sure that the individuals that go through node 3 have completed the queue. Note that there are certain constraints on our resources as there is a certain amount of time that our resources(booth, cashier, server) take to provide their respective services and only 45 customers come into the drivethru every hour.

# In[ ]:


completed_custs = []
for trial in range(20):
  ciw.seed(trial)
  Q = ciw.Simulation(N)
  Q.simulate_until_max_time(200)
  recs = Q.get_all_records()
  num_completed = len([r for r in recs if r.node==3 and r.arrival_date < 180])
  completed_custs.append(num_completed)


# In[ ]:


sum(completed_custs)/len(completed_custs)


# This means that the Mc Donald's location will be able to serve around **47** customers within 3 hours with the resources that they have in this situation.

# In the above example, we have only demonstrated a simple system without the designated parking spot. 

# ##Problem 2
# 
# ###Adding a designated parking spot
# 
# For this part of the problem, we will be adding a designated parking spot so that the customer that have larger orders have to wait at the spot to keep the queue moving. Since it is complex to have multiple parking spots like Mc Donald's usually do, we will be using a single parking spot to makes things easier. We will assume that 30% of the customers have large orders and have to go through the parking spot before leaving the queue. We will be using the same parameters that we used in previous problem to keep the comparisons fair.

# In[ ]:


N = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(0.75), # 45 customers arrive every hour
                             ciw.dists.NoArrivals(), #No arrivals at the other nodes
                             ciw.dists.NoArrivals(),
                             ciw.dists.NoArrivals(),
                             ciw.dists.NoArrivals()],
    service_distributions = [ciw.dists.Exponential(0.5), #1 order is made every 2 minutes
                             ciw.dists.Exponential(1.0),  #A cashier takes one payments every minute
                             ciw.dists.Exponential(0.5),  #A server serves one order two minutes
                             ciw.dists.Exponential(0.25),    #1 order is given out every 4 minutes]2
                             ciw.dists.Deterministic(0.0)],   #Customer exits the queue
    routing = [[0.0, 1.0, 0.0, 0.0, 0.0],  #The matrix for the network
               [0.0,0.0,1.0,0.0, 0.0],
               [0.0,0.0,0.0,0.3,0.7],
               [0.0,0.0,0.0,0.0,1.0],
               [0.0, 0.0, 0.0, 0.0, 0.0]],
    number_of_servers = [1, 1, 1, 1, 1] #Number of servers
)


# Lets simulate this for one shift of breakfast of 3 hours (180 mins). At the beginning of breakfast, the store opens from an empty system. Therefore, no warm-up is required. We will use 20 minutes of cool-down time. We will run 10 trials to get a measure of average number of customers that pass through the system. To find the average number of customers that pass through the system, we ca count the number of data that have passed through node 

# In[ ]:


average_waits = []
for trial in range(20):
  ciw.seed(trial)
  Q = ciw.Simulation(N)
  Q.simulate_until_max_time(200)
  recs = Q.get_all_records()
  waits = [r.waiting_time for r in recs]
  mean_wait = sum(waits)/len(waits)
  average_waits.append(mean_wait)
print (sum(average_waits)/len(average_waits))


# This shows how much of a difference does it make for Mc Donalds to have a designated parking spot for customers waiting due to large orders. The wait time in this condition goes down to approximately **10 minutes** whereas it was around 23 minutes in the last condition.

# In[ ]:


completed_custs = []
for trial in range(20):
  ciw.seed(trial)
  Q = ciw.Simulation(N)
  Q.simulate_until_max_time(200)
  recs = Q.get_all_records()
  num_completed = len([r for r in recs if r.node==5 and r.arrival_date < 180])
  completed_custs.append(num_completed)


# In[ ]:


sum(completed_custs)/len(completed_custs)


# We have also found an improvement in how many customers can pass through the queue within 3 hours. The number is now **76** which is much higher than what we had in the first situation. So, by adding only a single parking spot, Mc Donalds can take a lot more customers and provide them with almost half wait times.

# ##Problem Set
# 
# 1. In the above example, we have only demonstrated a simple system that includes 1 servers. what kind of difference do they make in the system if we had 2 servers?
# 
# 2. What does it mean to have an exponential distribution of 0.5 for customer arrival?
# 
# 3. How would you add a designated parking spot after the pickup window so that customers with large orders are made to wait separately?
# 
# 4. Compare the wait times for the two models with same number of servers. What kind of difference do you see?
# 
# 5. What kind of difference do they make in the system if we had 2 servers in the second model?
# 
# 6. For model two, what would be the best configuration for the queue given that we have 5 employees to work it that we can use for the ordering station, cashier and server? Try playing with different number of cashiers and servers.
# 
# 7. What queueing discipline does the two models follow? 
# 
# 8. What kind of limitations do we have on the models above? Could we speed up the queues by making servers more efficient that is decreasing serving times?
# 
# 9. You replace cashier 1 with a cashier that is twice as fast (the new cashier services jobs at an average rate of 2 payments every minute). Does this “improve- ment” affect the average wait time in the system?
# 
# 10. What does a M/M/1 queue represent? (Kendall Notation)
# 
# 
# 
# 
# 

# ##Project Idea
# 
# 1. In ATM, bank customers arrive randomly and the service time i.e. the time customer takes to do transaction in ATM, is also random.Figure out how queuing can help bank ATM to increase its quality of service, by anticipating, if there are many customers in the queue.
# 
# 2. A basic model of vehicular traffic based on queuing theory. It will determine the best times of the red, amber, and green lights to be either on or off. Using queuing theory, explore to reduce the delay on the roads.

# ## References
# 
# Shortle, J. F., Thompson, J. M., Gross, D., &amp; Harris, C. M. (2018). Fundamentals of queueing theory. John Wiley &amp; Sons. 
# 
# Khinchin A. I︠A︡. (2013). Mathematical methods in the theory of queuing. Dover. 
# 
# Bhat, U. N. (2015). An introduction to queueing theory: Modeling and analysis in applications. Birkhäuser. 
# 
# 

# ### Authors

# Subin Manandhar
# 
# Dhiraj Basnet
# 
# Dichendra Shrestha
