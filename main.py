import math
import random

xp = 0
level = (math.floor(xp ** (1./2.25))) + 1
level = int(level)
hp = 100
strength = 20
defence = 10
magicalstrength = 20
magicaldefence = 10
mp = 20
speed = 10
specialstatuspoints = 0
x = 0
i = level
i = math.ceil(i/100)
y = 0
reply = ""
reply2 = 0
#slime
slimehp = 10
slimestrength = 5
slimespeed = 5
slimexp = 2
#goblin
goblinhp = 30
goblinstrength = 15
goblindefence = 5
goblinmagicaldefence = 5
goblinspeed = 5
goblinxp = 4
#spider
spiderhp = 25
spiderstrength = 17
spiderdefence = 4
spidermagicaldefence = 4
spiderspeed = 6
spiderxp = 7
#zombie
zombiehp = 35
zombiestrength = 15
zombiedefence = 7
zombiemagicaldefence = 7
zombiespeed = 4
zombiexp = 15
encounters = ["Slime", "Goblin", "Spider", "Zombie", "Orc", "Lizardman", "Elf", "Dwarf", "Beastman", "Ogre", "Group of Bandits", "Werewolf", "Golem", "Chimera", "Kraken", "Spirit", "Dragon", "Demon", "Demon General", "Devil"]
yourencounter = ""
randomencounters = random.randint(0, random.randint(10, 19))
youraction = ""

while True:
  level = (math.floor(xp ** (1./2.25))) + 1
  level = int(level)
  #slime
  slimehp = 10
  slimestrength = 5
  slimespeed = 5
  slimexp = 2
  #goblin
  goblinhp = 30
  goblinstrength = 15
  goblindefence = 5
  goblinmagicaldefence = 5
  goblinspeed = 5
  goblinxp = 4
  #spider
  spiderhp = 25
  spiderstrength = 17
  spiderdefence = 4
  spidermagicaldefence = 4
  spiderspeed = 6
  spiderxp = 7
  #zombie
  zombiehp = 35
  zombiestrength = 15
  zombiedefence = 7
  zombiemagicaldefence = 7
  zombiespeed = 4
  zombiexp = 15
  #calculates stats
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      hp += (100 * x - y) * x * x * 2
    else:
      hp += (level - y) * x * x * 2
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      strength += math.ceil(((100 * x - y) * x * x) / 5 * 2)
    else:
      strength += math.ceil(((level - y) * x * x) / 5 * 2)
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      defence += math.ceil(((100 * x - y) * x * x) / 10 * 2)
    else:
      defence += math.ceil(((level - y) * x * x) / 10 * 2)
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      magicalstrength += math.ceil(((100 * x - y) * x * x) / 5 * 2)
    else:
      magicalstrength += math.ceil(((level - y) * x * x) / 5 * 2)
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      magicaldefence += math.ceil(((100 * x - y) * x * x) / 10 * 2)
    else:
      magicaldefence += math.ceil(((level - y) * x * x) / 10 * 2)
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      mp += math.ceil(((100 * x - y) * x * x) / 5 * 2)
    else:
      mp += math.ceil(((level - y) * x * x) / 5 * 2)
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
    x += 1
    if x == 1:
      y = 1
    else:
      y = 100 * (x - 1)
    if level > (100 * x):
      speed += math.ceil(((100 * x - y) * x * x) / 5)
    else:
      speed += math.ceil(((level - y) * x * x) / 5)
    i -= 1
  x = 0
  i = level
  i = math.ceil(i/100)
  y = 0
  while i != 0:
   x += 1
   if x == 1:
     y = 1
   else:
     y = 100 * (x - 1)
   if level > (100 * x):
     specialstatuspoints += math.ceil(((100 * x - y) * x * x))
   else:
     specialstatuspoints += math.ceil(((level - y) * x * x))
   i -= 1
  
  #states stats
  print("Your stats are")
  print("")
  print("level: " + str(level))
  print("hp: " + str(hp))
  print("strength: " + str(strength))
  print("defence: " + str(defence))
  print("magicalstrength: " + str(magicalstrength))
  print("magicaldefence: " + str(magicaldefence))
  print("mp: " + str(mp))
  print("speed: " + str(speed))
  print("")
  print("You have " + str(specialstatuspoints) + " status points you can use to upgrade any status you have!")
  print("")
  
  #calculates and prints status points
  while specialstatuspoints != 0:
      reply = input("Which status would you like to upgrade?: ")
      reply2 = input("How many status points would you like to use?: ")
      reply2 = int(reply2)
      if str(reply) == "hp" and int(reply2) <= specialstatuspoints:
        hp += int(reply2)
        print("Your hp stat is now " + str(hp))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      if str(reply) == "strength" and int(reply2) <= specialstatuspoints:
        strength += int(reply2)
        print("Your strength stat is now " + str(strength))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      if str(reply) == "defence" and int(reply2) <= specialstatuspoints:
        defence += int(reply2)
        print("Your defence stat is now " + str(defence))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      if str(reply) == "magicalstrength" and int(reply2) <= specialstatuspoints:
        magicalstrength += int(reply2)
        print("Your magicalstrength stat is now " + str(magicalstrength))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      if str(reply) == "magicaldefence" and int(reply2) <= specialstatuspoints:
        magicaldefence += int(reply2)
        print("Your magicaldefence stat is now " + str(magicaldefence))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      if str(reply) == "mp" and int(reply2) <= specialstatuspoints:
        mp += int(reply2)
        print("Your mp stat is now " + str(mp))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      if str(reply) == "speed" and int(reply2) <= specialstatuspoints:
        speed += int(reply2)
        print("Your speed stat is now " + str(speed))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
        reply2 = 0
      elif int(reply2) > specialstatuspoints:
        print("You do not have enough status points to do this.")
  #encounters
  yourencounter = encounters[randomencounters]
  print("You encounter a " + str(yourencounter) + ".")
  randomencounters = random.randint(0, random.randint(10, 19))
  print("")
  youraction = input("What would you like to do? If you want to attack with your weapon, type weapon. If you want to attack with magic, type magic. If you want to escape, type run: ")
  #slime
  if yourencounter == "Slime":
    if youraction == "weapon":
      if speed >= slimespeed:
        slimehp -= strength
        print("You dealt " + str(strength) + " damage to the slime")
        print("")
        if slimehp > 0:
          hp =(slimestrength - defence)
        else:
          print("")
      if slimespeed > speed:
        hp -= (slimestrength - defence)
        print("The slime dealt " + str(slimestrength - defence) + " damge to you.")
        slimehp -= strength
    if youraction == "magic":
      if speed >= slimespeed:
        slimehp -= magicalstrength
        print("You dealt " + str(magicalstrength) + " damage to the slime")
        print("")
        if slimehp > 0:
          hp =(slimestrength - defence)
        else:
          print("")
      if slimespeed > speed:
        hp -= (slimestrength - defence)
        print("The slime dealt " + str(slimestrength - defence) + " damge to you.")
        slimehp -= magicalstrength
    if youraction == "run":
      break
    if slimehp <= 0:
      print("You defeated the slime! Congratulations!")
      print("")
      xp += slimexp
      print("You gained " + str(slimexp) + " xp!")
      print("")
    while slimehp > 0:
      print("")
      youraction = input("What would you like to do? If you want to attack with your weapon, type weapon. If you want to attack with magic, type magic. If you want to escape, type run: ")
      if youraction == "weapon":
        if speed >= slimespeed:
          slimehp -= strength
          print("You dealt " + str(strength) + " damage to the slime")
          print("")
          if slimehp > 0:
            hp =(slimestrength - defence)
          else:
            print("")
        if slimespeed > speed:
          hp -= (slimestrength - defence)
          print("The slime dealt " + str(slimestrength - defence) + " damge to you.")
          slimehp -= strength
      if youraction == "magic":
        if speed >= slimespeed:
          slimehp -= magicalstrength
          print("You dealt " + str(magicalstrength) + " damage to the slime")
          print("")
          if slimehp > 0:
            hp =(slimestrength - defence)
          else:
            print("")
        if slimespeed > speed:
          hp -= (slimestrength - defence)
          print("The slime dealt " + str(slimestrength - defence) + " damge to you.")
          slimehp -= magicalstrength
      if youraction == "run":
        print("")
      if youraction != "weapon" and youraction != "magic" and youraction != "run":
        print("Sorry, could not compute your move. please try again.")
      if slimehp <= 0:
        print("You defeated the slime! Congratulations!")
        print("")
        xp += slimexp
        print("You gained " + str(slimexp) + " xp!")
        print("")
  #Goblin
  if yourencounter == "Goblin":
    if youraction == "weapon":
      goblinhp -= (strength - goblindefence)
      print("You dealt " + str(strength - goblindefence) + " damage to the goblin")
      print("")
    if youraction == "magic":
      goblinhp -= (magicalstrength - goblinmagicaldefence)
      print("You dealt " + str(magicalstrength - goblinmagicaldefence) + " damage to the goblin")
      print("")
    if youraction == "run":
      print("")
    if goblinhp <= 0:
      print("You defeated the goblin! Congratulations!")
      print("")
      xp += goblinxp
      print("You gained " + str(goblinxp) + " xp!")
      print("")
    while goblinhp > 0:
      print("")
      youraction = input("What would you like to do? If you want to attack with your weapon, type weapon. If you want to attack with magic, type magic. If you want to escape, type run: ")
      if youraction == "weapon":
        goblinhp -= (strength - goblindefence)
        print("You dealt " + str(strength - goblindefence) + " damage to the goblin")
      print("")
      if youraction == "magic":
        goblinhp -= (magicalstrength - goblinmagicaldefence)
        print("You dealt " + str(magicalstrength - goblinmagicaldefence) + " damage to the goblin")
      print("")
      if youraction == "run":
        break
      if youraction != "weapon" and youraction != "magic" and youraction != "run":
        print("Sorry, could not compute your move. please try again.")
    if goblinhp <= 0:
      print("You defeated the goblin! Congratulations!")
      print("")
      xp += goblinxp
      print("You gained " + str(goblinxp) + " xp!")
      print("")
  #Spider
  if yourencounter == "Spider":
    if youraction == "weapon":
      spiderhp -= (strength - spiderdefence)
      print("You dealt " + str(strength - spiderdefence) + " damage to the spider")
      print("")
    if youraction == "magic":
      spiderhp -= (magicalstrength - spidermagicaldefence)
      print("You dealt " + str(magicalstrength - spidermagicaldefence) + " damage to the spider")
      print("")
    if youraction == "run":
      print("")
    if spiderhp <= 0:
      print("You defeated the spider! Congratulations!")
      print("")
      xp += spiderxp
      print("You gained " + str(spiderxp) + " xp!")
      print("")
    while spiderhp > 0:
      print("")
      youraction = input("What would you like to do? If you want to attack with your weapon, type weapon. If you want to attack with magic, type magic. If you want to escape, type run: ")
      if youraction == "weapon":
        spiderhp -= (strength - spiderdefence)
        print("You dealt " + str(strength - spiderdefence) + " damage to the spider")
      print("")
      if youraction == "magic":
        spiderhp -= (magicalstrength - spidermagicaldefence)
        print("You dealt " + str(magicalstrength - spidermagicaldefence) + " damage to the spider")
      print("")
      if youraction == "run":
        break
      if youraction != "weapon" and youraction != "magic" and youraction != "run":
        print("Sorry, could not compute your move. please try again.")
    if spiderhp <= 0:
      print("You defeated the spider! Congratulations!")
      print("")
      xp += spiderxp
      print("You gained " + str(spiderxp) + " xp!")
      print("")
  #Zombie
  if yourencounter == "Zombie":
    if youraction == "weapon":
      zombiehp -= (strength - zombiedefence)
      print("You dealt " + str(strength - zombiedefence) + " damage to the zombie")
      print("")
    if youraction == "magic":
      zombiehp -= (magicalstrength - zombiemagicaldefence)
      print("You dealt " + str(magicalstrength - zombiemagicaldefence) + " damage to the zombie")
      print("")
    if youraction == "run":
      print("")
    if zombiehp <= 0:
      print("You defeated the zombie! Congratulations!")
      print("")
      xp += zombiexp
      print("You gained " + str(zombiexp) + " xp!")
      print("")
    while zombiehp > 0:
      print("")
      youraction = input("What would you like to do? If you want to attack with your weapon, type weapon. If you want to attack with magic, type magic. If you want to escape, type run: ")
      if youraction == "weapon":
        zombiehp -= (strength - zombiedefence)
        print("You dealt " + str(strength - zombiedefence) + " damage to the zombie")
      print("")
      if youraction == "magic":
        zombiehp -= (magicalstrength - zombiemagicaldefence)
        print("You dealt " + str(magicalstrength - zombiemagicaldefence) + " damage to the zombie")
      print("")
      if youraction == "run":
        break
      if youraction != "weapon" and youraction != "magic" and youraction != "run":
        print("Sorry, could not compute your move. please try again.")
    if zombiehp <= 0:
      print("You defeated the zombie! Congratulations!")
      print("")
      xp += zombiexp
      print("You gained " + str(zombiexp) + " xp!")
      print("")
