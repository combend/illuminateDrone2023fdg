from djitellopy import Tello

tello = Tello()
tello.connect()

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(1)  # forward detection only  只识别前方
#test
tello.land ()
tello.takeoff()
tello.get_mission_pad_id()
pad = tello.get_mission_pad_id()

tello.go_xyz_speed_yaw_mid(225, 0, 100, 20, 0, 1, 2)

tello.disable_mission_pads()
tello.land()
tello.end()
