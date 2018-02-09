import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
X1 = 150
Z1 = 3
X2 = 160
Z2 = 13
HOME_X = X2 + 2
HOME_y = 10
HOME_Z = X2 + 2
rent = 0
inField = 0

while True:
	time.sleep(1)
	pos = mc.player.getTilePos()
	if pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z<Z2:
		print "i am in pos:",X1,Z1
		rent = rent+1
		mc.postToChat("You own rent:"+str(rent))
		inField = inField+1
	else:
		inField = 0
	if inField>3:
		mc.postToChat("You are too slow!")
		mc.player.setPos(HOME_X,HOME_y,HOME_Z)

