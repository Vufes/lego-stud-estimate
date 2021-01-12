import pybullet as p
import time

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setGravity(0,0,-10)

brickSpawnPos = [0,0,3]
brickSpawnOri = p.getQuaternionFromEuler([0,0,0])

boxPos = [0,0,0]
boxOri = p.getQuaternionFromEuler([3.1415/2,0,0])

boxId = p.loadURDF("../models/box.urdf", boxPos, boxOri,flags = p.GEOM_FORCE_CONCAVE_TRIMESH)

bricksId = []
for i in range(1000):
    if i%5==0:
        bricksId.append(p.loadURDF("../models/brick.urdf",
                                   brickSpawnPos, brickSpawnOri))
    p.stepSimulation()
    time.sleep(1./240.)

cubePos, cubeOrn = p.getBasePositionAndOrientation(bricksId[0])
print(cubePos,cubeOrn)
p.disconnect()
