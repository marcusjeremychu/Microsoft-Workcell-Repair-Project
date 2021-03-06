#!/usr/bin/env python
"""
@Author: Nano Premvuti @premwong
University of Washington 2020
Department of Electrical & Computer Engineering
"""
import sys
import rospy
from workcell_iiwa_control import MoveGroupLeftArm, Component
from std_msgs.msg import Float64MultiArray
from iiwa_msgs.srv import MoveConveyor
from config import * 

CONVEYOR_ENABLE = False

class ItemState(object):
	"""item that holds components eg. server, tray, etc"""
	def __init__(self, item_id, item_type):
		super(ItemState, self).__init__()
		self._item_id = item_id
		self._item_type = item_type
		self._heatsink1 = True
		self._heatsink2 = True
		self._nic = True
		self._hdd1 = True
		self._hdd2 = True
		self._dimm1 = True
		self._dimm2 = True

	def get_parts_list(self):
		return self.__dict__

def replace_nic(move_group):
	try:
		print "NIC selected. Press to start sequence"
		raw_input()
		move_group.goto_component_position('nic')
		rospy.sleep(2)
		move_group.goto_home_state()

		# move_group.set_gripper(True)
		# rospy.sleep(6)
		# move_group.interpolated_trajectory(move_group.component_map['nic'].get_z_offset() - Z_OFFSET, 0.001)
		# move_group.interpolated_trajectory(Z_OFFSET - move_group.component_map['nic'].get_z_offset(), 0.001)
		# move_group.goto_component_tray('heatsink1')
		# move_group.interpolated_trajectory(-0.03, 0.002)
	except rospy.ROSInterruptException:
	  return
	except KeyboardInterrupt:
	  return

def replace_heatsink(server, move_group):
	try:
		print "Press to start heatsink sequence"
		raw_input()
		move_group.goto_cartesian_state(0.1, 0.7, 0.2, 0, 'heatsink')
	except rospy.ROSInterruptException:
		return
	except KeyboardInterrupt:
		return

def autostop_callback(camera_feed):
	camera_feed_buffer = camera_feed.data
	if camera_feed_buffer[6] <= 200:
		move_conveyor("S")


# dispatch_table = {'nic':replace_nic, 'heatsink1':replace_heatsink1, 'heatsink2':replace_heatsink2, 'hdd1':replaceHddHandler_1, 'hdd2':replaceHddHandler_2}


if CONVEYOR_ENABLE:
	rospy.Subscriber('camera_pose_feed', Float64MultiArray, autostop_callback)
	print 'waiting for conveyor service...'
	try:
		rospy.wait_for_service('move_conveyor', 1)
	except:
		print 'Service call timeout'
	try:
		move_conveyor = rospy.ServiceProxy('move_conveyor', MoveConveyor)
		print 'hello conveyor'
	except rospy.ServiceException as e:
		print(e)

def main():
	try:
		nic = Component('nic', NIC_OFFSET, NIC_SEED_STATE, NIC_ROTATION, (0.6, 0, 0))
		heatsink = Component('heatsink1', HEATSINK_OFFSET, NIC_SEED_STATE, HEATSINK_ROTATION, (0.6, 0, 0), 90)
		hdd = Component('hdd1', HEATSINK_OFFSET, NIC_SEED_STATE, HDD_ROTATION, (0.6, 0, 0), -90)
		myLeftArm = MoveGroupLeftArm()
		myLeftArm.load_component_map([nic, heatsink, hdd])
		myLeftArm.print_state()
		if myLeftArm.query_pose_and_check_ik() == None:
			print 'ik solutions found'
			replace_nic(myLeftArm)
		# pose = myLeftArm.query_pose()
		# myLeftArm.check_ik_validity(pose)


		
		
		# # myLeftArm.goto_fiducial_position()
		# myLeftArm.goto_cartesian_state(0.1, 0.7, 0.25, -30, 'nic')
		# rospy.sleep(4)
		# # myLeftArm.execute_trajectory_from_file('nic_to_heatsink1')
		# # rospy.sleep(8)
		# myLeftArm.gotoartesian_state(0.0, 0.6, 0.25, 90, 'heatsink1')
		# move_conveyor("F")
		rospy.spin()

	except rospy.ROSInterruptException:
	  return
	except KeyboardInterrupt:
	  return

if __name__ == '__main__':
  main()



#Example control flow:
# welcome to the server repair workcell
# starting etc...
# waiting for server mover .... (press ENTER to override)
# server mover arrived!
# retracting conveyor belt...
# server id:... heatsink: old... nic: old... etc...

# Select option to replace: [1] nic card [2] heatsink [3] _hdd2

# replacing.. 

# ABORT: replacement failed. server out of range 
# attempting to reposition:

# Select option to replace: [1] nic card [2] heatsink [3] _hdd2

# Tray full, please replace




