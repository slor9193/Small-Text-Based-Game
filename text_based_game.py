from sys import exit
from random import randint
armory_check=0

#Global variables
stuff=[]

code=randint(1,9999)

endtoken=False
deadspider=False
firstpass=True

#Classes##
##The enviroment class
class enviro_status(object):
    
    def __init__(self, items, location, name):
        self.items=items
        self.location=location
        self.name=name

##The character class
class char_status(object):

    def __init__(self, current_location,current_location_word, nearby_locations, inventory=stuff):
        self.inventory=inventory
        self.current_location=current_location 
        self.current_location_word=current_location_word
        self.nearby_locations=nearby_locations
        
    def kill_thineself():
        exit()
    
    def give_stuff():
        print stuff


#Non-imported functions

import random

seen_room=0

#Game Over
def game_over():
    print "Nice try, but it's...\n\n\t\tGAME OVER."
    
    exit()
    
def armory_text_1():

    if "laser_rifle" not in stuff:   
        print "It looks like the CRYSTAL SPIDER made it here before you did."
        print "\nToo bad your stupid ass doesn't have a gun. The spider impales you with it's CRYSTAL LEG and drags you to the corner of the armory. It appears he's saving you for later."
    
        game_over()
    
    else:
        pass
    
    
    
def armory_text_2():
    global firstpass
    
    if "laser_rifle" in stuff and firstpass is True:
        print "It looks like the CRYSTAL SPIDER made it here before you did."
        print "\nNot giving you much of a choice, you fire on the CRYSTAL SPIDER. The Mizcerian National Zoo won't be happy about this."
        print "\nLooks like he emptied out the room.\n*********************************************************"
        firstpass=False
    else:
        pass
    
    
    
    
    
def armory_text_3():

    global firstpass
    
    if ("laser_rifle" in stuff) and firstpass is False:
    
        rand_armory=random.randint(1,4)
        print "You're in the armory. Not much to look at, bare metal walls and a dead spider."
    
        if rand_armory==1:
            print "\n\nPoor crystal spider :("
        elif rand_armory==2:
            print "\n\nWhat a mess, there goes my 15,000 credits."
        else:
            print "\n\nThe spider twitches for second, then stops."
    else:
        pass
    
    


def engine_room_text():
    
    rand_engine=random.randint(1,4)
    
    print "You are in the engine room. The pale blue emergency lights are on, indicating the secondary system is active.\n"
    
    if rand_engine==1:
        print "\n\nIt smells like sulpher and shoe polish."
    elif rand_engine==2:
        print "\n\nThe room is covered in a thin layer of ash."
    else:
        print "\n\nYou hear a faint rasping. That can't be good."
    




def star_hall_text():
    rand_star=random.randint(1,4)
    
    print "You're in the starboard hall of the ship. You've got a nice view of Teria from the window."
    
    if rand_star==1:
        print "\n\nThe room smells vaguely of feet."
    elif rand_star==2:
        print "\n\nYou can see the Crasias Cluster from here."
    else:
        print "\n\nA You can barely make out a long wall across one of the Terian continents. Or maybe it's a road."
        




def bow_text():

    rand_bow=random.randint(1,4)
    
    print "You're in the ship's bow. Only a few buttons on your control module are lit, and it looks like the massage function on your chair is now out.\nThis room doubles as an escape pod when necessary (eeeehh)."
    
    if rand_bow==1:
        print "\n\nYou hear some tapping from the armory."
    elif rand_bow==2:
        print "\n\nThe 'request assistance' button is out."
    else:
        print "\n\nThe room is covered in beer cans, maybe I can build something with these?"
        
        

    
        
def port_hall_text():
    
    rand_port=random.randint(1,4)
    
    print "You're in the portside hall of the ship. You view from the window is saturated with engine and asteroid debris."
    
    if rand_port==1:
        print "\n\nThere's a smudge on the window that kind of looks like a frog."
    elif rand_port==2:
        print "\n\nThe room smells like ozone and peppermint."
    else:
        print "\n\nYou can make out the Milky Way Galaxy in the distance. I hear they have monkey people there."
        
        

def prisoners_bay_text():
    global seen_room
    rand_prisoners=random.randint(1,4)
    
    if  seen_room==0:
    
        print "You're now in the Prisoners Bay. AKA the place the Crystal Spider was supposed to be. It looks like he's been back here, and made a little nest from melted-down firearms. \nMaybe one of them still works..."
        
        seen_room+= 1
        
    else:
        print "You're in the Prisoners Bay."
        
        
        
    if rand_prisoners==1:
        print "\n\nThe door's paint is scratched and the frame bent. Not going to be a cheap fix."
    elif rand_prisoners==2:
        print "\n\nThe spider generously left a pile of round jewels in the corner of the room. I think I'll leave them there."
    else:
        print "\n\nIronically, this is the nicest room in the ship."
        
def ending1():
    raw_input("\n\n\n\n\nThe Cresmelian engineers try their best to salvage the ship, but return unsuccessful. \nWith the ship's engines no longer function, the remains of your ship fall towards Teria, likely landing in the Teriaen ammonia sea.\n\n")
    print "Without a way to leave, you'll be stuck here for awhile. Welcome to your new home!\n"
    print "You got: Ending 1!"
    
def ending2():
    raw_input("\n\n\n\n\nYou made a bbbiiiiggg mistake.\n The Teriaen Police are here and are not happy about that live, angry crystal spider you happened to be transporting. \nAccording to the police, neither is the remaining Cresmelian engineer.")
    print "The Teriaens take this sort of thing very seriously{}"
    print "You got: Ending 2!"
def ending3():
    raw_input("X")
    print "\n You got: Ending 3(the good one)!"
    
        

            
#Inputs location word, outputs location code(number)

def word_to_location(words):
    if "ARMORY" in words:
        return 6
    elif "PRISONER" in words or "PRISONER'S" in words or "PRISONERS" in words:
        return 5
    elif "PORT" in words:
        return 4
    elif "BOW" in words:
        return 3
    elif "STARBOARD" in words:
        return 2
    elif "ENGINE" in words:
        return 1
    else:
        print "Fundamental error. Check code. #WTL"


#Returns word for current location, will be used for map function
def location_to_word(YMB):
    if YMB == 6:
        return "Armory"
    elif YMB==5:
        return "Prisoner's Bay"
    elif YMB==4:
        return "Port Hall"
    elif YMB==3:
        return "Ship's Bow"
    elif YMB==2:
        return "Starboard Hall"
    elif YMB==1:
        return "Engine Room"
    else:
        print "Fundamental error. Check code. #LTW"
    
#Gives dialogue associated with given room (location)        
def associated_dia(YMA):
    if YMA == 6:
        armory_text_1()
        armory_text_2()
        armory_text_3()
    elif YMA == 5:
        prisoners_bay_text()
    elif YMA == 4:
        port_hall_text()
    elif YMA == 3:
        bow_text()
    elif YMA == 2:
        star_hall_text()
    elif YMA == 1:
        engine_room_text()
    else:
        print "Fundamental error. Check code. #ASD"
        
    print "\nNow what?\n"
    




def nearby_sanitizer(locale):
    if locale==1:
        mainc.nearby_locations=[2]
    elif locale==2:
        mainc.nearby_locations=[1,3]
    elif locale==3:
        mainc.nearby_locations=[2,4,6]
    elif locale==4:
        mainc.nearby_locations=[3,5]
    elif locale==5:
        mainc.nearby_locations=[4]
    elif locale==6:
        mainc.nearby_locations=[3]
    else:
        print "Nearby sanitizer error. Check code."
        
def current_room_items():
    if mainc.current_location == 1:
        for eri in engine_inv.items:
            print eri            
    elif mainc.current_location == 2:
        for sii in starboard_inv.items:
            print sii
    elif mainc.current_location == 3:
        for bii in bow_inv.items:
           print bii
    elif mainc.current_location == 4:
        for pii in port_inv.items:
            print pii
    elif mainc.current_location == 5:
        for pri in prisoners_inv.items:
          print pri
    elif mainc.current_location == 6:
        for ari in armory_inv.items:
         print ari 
    else:
        print "Fudamental error. Check code. #CRI"    

def nearby_checker(location_list_nearby):

    locations=["ARMORY","ENGINE", "BOW", "PORT", "PRISONER","STARBOARD", "PRISONERS", "PRISONER\'S"]

    if location_checker(location_list_nearby)==0 or location_checker(location_list_nearby)==2:
        return False
    
    else:
       
        Y=location_checker(location_list_nearby)
        if Y=="STARBOARD" and mainc.current_location==1:
           
            return True
        elif (Y=="ENGINE" or Y== "BOW") and mainc.current_location==2:
        
            return True
        elif ((Y=="ARMORY" or Y== "PORT") or Y== "STARBOARD") and mainc.current_location==3:
           
            return True
        elif (Y=="BOW" or Y=="PRISONER" or Y=="PRISONERS" or Y=="PRISONER\'S") and mainc.current_location==4:
            
            return True
        elif Y== "PORT" and mainc.current_location==5:
            
            return True
        elif Y=="BOW" and mainc.current_location==6:
           
            return True
            
        else:
            return False
   
def location_checker(input_list):

    locations=["ARMORY","ENGINE", "BOW", "PORT", "PRISONER","STARBOARD", "PRISONERS", "PRISONER\'S"]
    instances=0
    location_in_question=None
    
    
    for input_word in input_list:
        for place in locations:
            
            if place==input_word:
                instances+=1
                location_in_question=str(place)
                
            else:
                continue    


    if instances==1:
        return location_in_question
    elif instances==0:
        return 0
    else:
        return 2
        
def is_this_item_in_this_room(YMB,item_list, actual=False):
    
    counter=0
    item=None 
    identifier=None
    
    if YMB == 6:
       for itemzsix in item_list:
           for roomzsix in armory_inv.items:  
             if roomzsix.upper()==itemzsix:
               counter+=1
               item=roomzsix
               identifier=armory_inv.items
              
             else:
               continue
                 
    elif YMB==5:
        for itemzfive in item_list:
            for roomzfive in prisoners_inv.items:
                      
                if roomzfive.upper()==itemzfive:
                    counter+=1
                    item=roomzfive
                    identifier=prisoners_inv.items
                   
                else:
                    continue
    elif YMB==4:
        for itemzfour in item_list:
            for roomzfour in port_inv.items:
                 
                if roomzfour.upper()==itemzfour:
                    counter+=1
                    item=roomzfour
                    identifier=port_inv.items
                    
                else:
                    continue
    elif YMB==3:
        
        for itemzthree in item_list:
            for roomzthree in bow_inv.items:
                  
                if roomzthree.upper()==itemzthree:
                    counter+=1
                    
                    item=roomzthree
                    identifier=bow_inv.items
                   
                else:
                    
                    continue
                    
    elif YMB==2:
        for itemztwo in item_list:
            for roomztwo in starboard_inv.items:  
              if roomztwo.upper()==itemztwo:
                counter+=1
                item=roomztwo
                identifier=starboard_inv.items
                
              else:
                continue
    elif YMB==1:
        for itemzone in item_list:
            for roomzone in engine_inv.items:  
              if roomzone.upper()==itemzone:
                counter+=1
                item=roomzone
                identifier=engine_inv.items
                
              else:
                continue
    else:
        print "Fundamental error. Check code. #LTW"
    
    
    if counter >= 2:
        
        return 2
    elif counter==0:
        
        return 0
    elif counter==1:
        
        if actual is True:
            identifier.remove(item)
            return item
        else:
            return item
    else:
        print "Invalid command!"


def drop(room_in, p_list, actual=False):
    counter=0
    item_to_drop=None
    room=None
    for ps in p_list:
        for szs in stuff:
            zoop = szs.upper()
            if zoop==ps:
                
                counter+=1
                item_to_drop=szs
                if zoop== "LASER_RIFLE":
                    armory_check=0
                else:
                    pass
            else:
                continue
                
    if room_in == 1:
        room=engine_inv
    elif room_in ==2:
        room=starboard_inv
    elif room_in ==3:
        room=bow_inv
    elif room_in ==4:
        room=port_inv
    elif room_in ==5:
        room=prisoners_inv
    elif room_in ==6:
        room=armory_inv
    else:
        print "Fundamental error. Check code #DRP"
        
    if counter==0:
        print "What are you trying to drop?"
    elif counter > 2:
        print "One at a time pal."
    elif counter==1:
        print "Dropped %r " % (item_to_drop), "!\n"
        
        str(item_to_drop)
        room.items.append(item_to_drop)
        stuff.remove(item_to_drop)
        print "You now have %r items in your inventory." % (len(stuff)) 
        
                
                
            
    


#Character instance
mainc=char_status(3,"bow",[2,4,6])



#Room inventory instances
engine_inv=enviro_status(["matches", "flashlight"], 1, "Engine Room")
starboard_inv=enviro_status(["socks","Cresmelian_maintenance_manual","cattoy"], 2, "Starboard Hall")
bow_inv=enviro_status(["beer_cans","bowl", "spacesnackz"], 3, "Bow")
port_inv=enviro_status(["small_ship_fragment"], 4, "Port Hall")
prisoners_inv=enviro_status(["laser_rifle", "spider_slime"], 5, "Prisoner\'s Bay")
armory_inv=enviro_status(["spider_corpse"], 6, "Armory")
inventory_rooms_list=[engine_inv,starboard_inv, bow_inv, port_inv, prisoners_inv,armory_inv]



# Introduction dialogue
raw_input( "It's not going to be a good day.\n \nIt appears an asteroid has come into 'agressive contact' with your ship and knocked out the electrical system. \nFortunately, this ship was crafted by the finest Cresmelion engineers and the reserve system works.")

raw_input("you'll have to take a pod down to the closest planet to request repairs if you want to reactivate the primary system.")
raw_input("\n\nAs soon as possible too, that crystal spider you're transporting might claw it's way out of the Prisoners Bay.")
raw_input ("Let's get the error code from the ship's engine room before we go.")
raw_input("\n\n\nTo change rooms, say \"go\"...\"room name\".\nTo check your inventory, say \"inventory\".\n\"Investigate\" to investigate a room for items, \"take\" to put and item in inventory.\n\"Drop\" to drop an item in the current room.\n\"Help\" to get this prompt again.")
raw_input("\n\nGood luck!\n\n\n")

print "****************************************************************"

bow_text()

###################Skeleton structure############################

while endtoken is False:

    prim_raw= raw_input(">")
    str(prim_raw)
    primary=prim_raw.upper()
    primary_list=primary.split()
    

    #Go Tree#
    if "GO" in primary_list or "MOVE" in primary_list:
        
        if nearby_checker(primary_list)==True:
            print "Moving...\n*  *  *  *  *  *  *  *  *  *  *"
            print"\n\n"
            
            mainc.current_location=word_to_location(primary_list)
            mainc.current_location_word=location_to_word(mainc.current_location)
            nearby_sanitizer(mainc.current_location)
            associated_dia(mainc.current_location)
            
            print "Nearby rooms are:\n"
            for near_locs in mainc.nearby_locations:
                print location_to_word(near_locs), "\n===========++\n"
            
        else:
            print "Invalid input!"
    
    if "INVESTIGATE" in primary_list:
    
        print "\nInvestigating...\n\n"
        
        print "Items in this room:\n"
        current_room_items()
        print "\n==========="
        
    elif "HELP" in primary_list:
        
        raw_input("\n\n\nTo change rooms, say \"go\"...\"room name\".\nTo check your inventory, say \"inventory\".\n\"Investigate\" to investigate a room for items, \"take\" to put and item in inventory.\n\"Drop\" to drop an item in the current room.\n\"Help\" to get this prompt again.")
    elif "INVENTORY" in primary_list:
        print "Items in inventory: "
        for zoot in stuff:
            print "\n > ", zoot
        print "\n==========="
           
        
            
    elif "TAKE" in primary_list or "GRAB" in primary_list  or "GET" in primary_list:  
        if len(stuff) < 3 and not ( is_this_item_in_this_room(mainc.current_location ,primary_list)==2 or is_this_item_in_this_room(mainc.current_location ,primary_list))==0:
        
            to_add=is_this_item_in_this_room(mainc.current_location ,primary_list)
            stuff.append(to_add)
            
            print "Added %r to inventory" % (to_add)
            is_this_item_in_this_room(mainc.current_location ,primary_list, True)
            
            for lr in stuff:
                if lr=="laser_rifle":    
                    armory_check=1
                
                else:
                    pass
                

        elif len(stuff)>= 3:
            print "Inventory is full, drop an item to add."
            
        else:
            print "Take... what?"
      
    elif "DROP" in primary_list:
        drop(mainc.current_location,primary_list)
        
    elif "CODE" in primary_list:
        if mainc.current_location==1:
            print "The code displayed on the engine display module is %r. \n" % (code)
            if firstpass is True:
                print "Perfect! Now let's get off this ship before I run into that spider."
            else:
                print "Perfect! \n\nThe emergency system is starting to fail, we should go soon!"
        else:
            print "Wrong room. You'll need to go to the Engine Room to find the error code.\n"
            
    elif "POD" in primary_list or "ESCAPE" in primary_list:
        if mainc.current_location ==3:
            endtoken=True
            print "You manage to find the escape pod engage and the bow begins to seperate from the ship.\nYour escape pod shuttles you to the nearby planet of Teria and landing you in a mid-sized city called Certe!"
        
     
    else:
        continue
        
        

print "You run into a small group of Cresmelian engineers and after a bit of back and forth, they agree to repair your ship for the small fee of 35,000 credits. How generous.\n"
print "Before they go, they ask if your ship gave any error codes. Do you tell them yes or no?"
response=raw_input(">")
response=response.upper()
response= response.split()
coderesponse=0

while 1==1:
    if "YES" in response:
      
        print "What code do you give them?"
        coderesponse=raw_input(">")
        int(coderesponse)
        int(code)
        
        if coderesponse==code and firstpass is False:
            ending3()
            break
            
        elif firstpass is False:
            ending1()
            break
        else:
            ending2()
            break
                
    elif "NO" in response:
        if firstpass is True:
            ending2()
            break
        elif firstpass is False:
            ending1()
            break
        else:
            print "\nYES OR NO MOTHERFUCKER?"
    else:
        print "\nYES OR NO MOTHERFUCKER?"  
            
       
        

  
