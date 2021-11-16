import configparser

from math import sqrt


def flight_geography(CD):
	s_FG = 400
	h_FG = 10
	if s_FG < 3*CD or h_FG < 3*CD:
		print("ERROR!!!!")
	return(s_FG, h_FG)
	
def contingency_volume(v_0, CD, s_gps, s_pos, s_map, h_baro, h_FG):
	s_rz = v_0 * 1  # reaction time t = 1sec
	h_rz = v_0*0.7*1  # reaction time t = 1sec
	s_cm = 3*v_0*v_0/2/9.81
	h_cm = 0.5*v_0*v_0/9.81
	s_CV = s_gps + s_pos + s_map + s_rz + s_cm
	h_CV = h_FG + h_baro + h_rz + h_cm
	return(s_CV, h_CV)
	
def ground_risk_buffer(v_0, CD, h_CV):
	# Ballistic formula used because multicopter
	s_GRB = v_0 * sqrt(2*h_CV/9.81) + 0.5 * CD
	return(s_GRB)
	

def main():
	config = configparser.ConfigParser()
	config.read_file(open('/home/nati/Desktop/UAV/uav.cfg'))
	model = config.get('GENERAL','MODEL')
	CD = float(config.get('GENERAL','CHARACT_DIM'))
	v_0 = float(config.get('OPERATIONS','v_0'))
	s_gps = float(config.get('INACCURACIES', 'GPS'))
	s_pos = float(config.get('INACCURACIES', 'POS'))
	s_map = float(config.get('INACCURACIES', 'MAP'))
	h_baro = float(config.get('INACCURACIES', 'BARO'))
	
	s_FG, h_FG = flight_geography(CD)
	s_CV, h_CV = contingency_volume(v_0, CD, s_gps, s_pos, s_map, h_baro, h_FG)
	s_GRB = ground_risk_buffer(v_0, CD, h_CV)

	print("Flight geometry --> s_FG=", s_FG, " and h_FG=", h_FG)
	print("Contingency volume --> s_CV=", s_CV, " and h_CV=", h_CV)
	print("Ground risk buffer --> s_GRB", s_GRB)

if __name__ == "__main__":
    main()
