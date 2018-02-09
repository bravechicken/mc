import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
	time.sleep(1)
	pos = mc.player.getTilePos()
	if pos.x == 80 and pos.y == 35 and pos.z == -9:
		mc.postToChat("Welcome home")