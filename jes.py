from jes_sim import Sim
from jes_ui import UI

c_input = input("How many creatures do you want?\n100: Lightweight\n250: Standard (if you don't type anything, I'll go with this)\n500: Strenuous (this is what my carykh video used)\n")
if c_input == "":
    c_input = "250"
sc_input = input("What are the dimensions of the screen? Answer in form XxY (e.g. 1920x1078).\n1920x1078 is the default if you do not answer (These are the stablest dimensions).")
if sc_input == "":
    sc_input = "1920x1078"
screen = [int(i) for i in sc_input.split('x')]

# Simulation
# population size is 250 here, because that runs faster. You can increase it to 500 to replicate what was in my video, but do that at your own risk!

sim = Sim(_c_count=int(c_input), _stabilization_time=200, _trial_time=300,
_beat_time=20, _beat_fade_time=5, _c_dim=[4,4],
_beats_per_cycle=3, _node_coor_count=4, # x_position, y_position, x_velocity, y_velocity
_y_clips=[-10000000,0], _ground_friction_coef=25,
_gravity_acceleration_coef=0.002, _calming_friction_coef=0.7,
_typical_friction_coef=0.8, _muscle_coef=0.08,
_traits_per_box=3, # desired width, desired height, rigidity
_traits_extra=1, # heartbeat (time)
_mutation_rate=0.07, _big_mutation_rate=0.025,
_UNITS_PER_METER=0.05)

# Cosmetic UI variables
ratio = [screen[0]/1920, screen[1]/1078]
ui = UI(_W_W=1920 * ratio[0], _W_H=1078 * ratio[1], _MOVIE_SINGLE_DIM=(650*ratio[0],650*ratio[1]),
_GRAPH_COOR=(850*ratio[0],50*ratio[1],900*ratio[0],500*ratio[1]), _SAC_COOR=(850*ratio[0],560*ratio[1],900*ratio[0],300*ratio[1]),
_GENEALOGY_COOR=(20,105*ratio[0],530*ratio[1],802*ratio[0],42*ratio[1]),
_COLUMN_MARGIN=330*ratio[0], _MOSAIC_DIM=[10*ratio[0],24*ratio[1],24*ratio[0],30*ratio[1]], #_MOSAIC_DIM=[10,10,17,22],
_MENU_TEXT_UP=180*ratio[1], _CM_MARGIN1=20*ratio[1], _CM_MARGIN2=1, RATIO=ratio)

sim.ui = ui
ui.sim = sim
ui.addButtonsAndSliders()
    
sim.initializeUniverse()
while ui.running:
    sim.checkALAP()
    ui.detectMouseMotion()
    ui.detectEvents()
    ui.detectSliders()
    ui.doMovies()
    ui.drawMenu()
    ui.show()
