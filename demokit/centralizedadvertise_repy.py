# -*- coding: utf-8 -*-
### Automatically generated by repyhelper.py ### /home/chris/Documents/Distributed_Systems/Labs/Lab1/minimal/demokit/centralizedadvertise.repy

### THIS FILE WILL BE OVERWRITTEN!
### DO NOT MAKE CHANGES HERE, INSTEAD EDIT THE ORIGINAL SOURCE FILE
###
### If changes to the src aren't propagating here, try manually deleting this file. 
### Deleting this file forces regeneration of a repy translation


from repyportability import *
import repyhelper
mycontext = repyhelper.get_shared_context()
callfunc = 'import'
callargs = []

""" 
Author: Justin Cappos

Start Date: July 8, 2008

Description:
Advertisements to a central server (similar to openDHT)


"""

repyhelper.translate_and_import('centralizedadvertise_base.repy')

# Hmm, perhaps I should make an initialization call instead of hardcoding this?
# I suppose it doesn't matter since one can always override these values
servername = "advertiseserver.poly.edu"
# This port is updated to use the new port (legacy port is 10101)
serverport = 10102


def centralizedadvertise_announce(key, value, ttlval):
  """
   <Purpose>
     Announce a key / value pair into the CHT.

   <Arguments>
     key: the key to put the value under. This will be converted to a string.

     value: the value to store at the key. This is also converted to a string.

     ttlval: the amount of time until the value expires.   Must be an integer

   <Exceptions>
     TypeError if ttlval is of the wrong type.

     ValueError if ttlval is not positive 

     CentralAdvertiseError is raised the server response is corrupted

     Various network and timeout exceptions are raised by timeout_openconn
     and session_sendmessage / session_recvmessage

   <Side Effects>
     The CHT will store the key / value pair.

   <Returns>
     None
  """
  return centralizedadvertisebase_announce(servername, serverport, key, value, ttlval)


def centralizedadvertise_lookup(key, maxvals=100):
  """
   <Purpose>
     Returns a list of valid values stored under a key

   <Arguments>
     key: the key to put the value under. This will be converted to a string.

     maxvals: the maximum number of values to return.   Must be an integer

   <Exceptions>
     TypeError if maxvals is of the wrong type.

     ValueError if maxvals is not a positive number

     CentralAdvertiseError is raised the server response is corrupted

     Various network and timeout exceptions are raised by timeout_openconn
     and session_sendmessage / session_recvmessage

   <Side Effects>
     None

   <Returns>
     The list of values
  """
  return centralizedadvertisebase_lookup(servername, serverport, key, maxvals)

### Automatically generated by repyhelper.py ### /home/chris/Documents/Distributed_Systems/Labs/Lab1/minimal/demokit/centralizedadvertise.repy
