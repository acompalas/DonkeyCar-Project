# 04Jan22
# UCSD mods to make easier for the UCSD students to use the Donkey-Sim
# the following uncommented lines where copied here from the body of myconfig.py below
DONKEY_GYM = True
# DONKEY_SIM_PATH = "remote"
DONKEY_SIM_PATH = "remote"# "/home/ucsd/projects/DonkeySimLinux/donkey_sim.x86_64"
DONKEY_GYM_ENV_NAME = "donkey-warren-track-v0"
# DONKEY_GYM_ENV_NAME = “donkey-mountain-track-v0”
# UCSD yellow color in RGB = 255, 205, 0
# UCSD blue color in RGB = 0, 106, 150
GYM_CONF = { "body_style" : "car01", "body_rgb" : (255, 205, 0), "car_name" : "UCSD-148-Anderson", "font_size" : 30} # body style(donkey|bare|car01) body rgb 0-255
GYM_CONF["racer_name"] = "UCSD-148-Anderson"
GYM_CONF["country"] = "USA"
GYM_CONF["bio"] = "My dad in the US Navy once snuck me onto the USS Peleliu aircraft carrier and hid me in the supply closet during a short routine around the bay. He didn't want to leave me at a hotel I guess"
#
# SIM_HOST = "donkey-sim.roboticist.dev"
SIM_ARTIFICIAL_LATENCY = 0
SIM_HOST = "donkey-sim.roboticist.dev" #"127.0.0.1"              # when racing on virtual-race-league use host "roboticists.dev"
# SIM_ARTIFICIAL_LATENCY = 30          # Use the value when you ping roboticists.dev. When racing on virtual-race league, use 0 (zero)

# When racing, to give the ai a boost, configure these values.
AI_LAUNCH_DURATION = 3            # the ai will output throttle for this many seconds
AI_LAUNCH_THROTTLE = 1.0           # the ai will output this throttle value
AI_LAUNCH_KEEP_ENABLED = True      # when False ( default) you will need to hit the AI_LAUNCH_ENABLE_BUTTON for each use. This is safest. When this True, is active on each trip into "local" ai mode.
#
# When using a joystick modify these specially USE_JOYSTICK_AS_DEFAULT = True
# JOYSTICK
USE_JOYSTICK_AS_DEFAULT = True     #when starting the manage.py, when True, will not require a --js option to use the joystick. If you want to use the web controller, you must explicitly declare this as false or else it will not respond to the web controller and just search for an imaginary joystick
JOYSTICK_MAX_THROTTLE = 0.5         #this scalar is multiplied with the -1 to 1 throttle value to limit the maximum throttle. This can help if you drop the controller or just don't need the full speed available.
JOYSTICK_STEERING_SCALE = 0.6   #some people want a steering that is less sensitve. This scalar is multiplied with the steering -1 to 1. It can be negative to reverse dir.
AUTO_RECORD_ON_THROTTLE = True      #if true, we will record whenever throttle is not zero. if false, you must manually toggle recording with some other trigger. Usually circle button on joystick.
CONTROLLER_TYPE='xbox'
JOYSTICK_DEADZONE = 0.0             # when non zero, this is the smallest throttle before recording triggered.
# #Scale the output of the throttle of the ai pilot for all model types.
AI_THROTTLE_MULT = 0.87              # this multiplier will scale every throttle value for all output from NN models
