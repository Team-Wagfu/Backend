from enum import Enum

# pets types
class PetType(str, Enum):
	dog = "dog"
	cat = "cat"
	bird = "bird"
	fish = "fish"
	reptile = "reptile"
	other = "other"

# user types
class UserType(str, Enum):
	pet_owner="pet_owner"
	emergency="emergency"
	doctor="doctor"
	admin="admin"
	pharm="pharmaceutical"

class Intervals(int, Enum):
	daily=1
	weekly=7
	monthly=30
	# TODO

class Vaccines:
	class dVaccine:
		rv="rabies"
		dv="distemper"
		cpv="canine parvovirus"
		adv="canine adenovirus"
		bb="bordetella bronchiseptica"
		cpv="canine parainfluenza virus"
		lepto="leptospirosis"
		lyme="lyme disease"
		ci="canine influenza"

	class cVaccine:
		rabies="rabies"
		fh1="feline herpesvirus-1"
		fcv="feline calicivirus"
		fpv="feline panleukopenia virus"
		flv="feline leukemia virus"
		chf="chlamydophila felis"
		bb="bordetella bronchiseptica"

	class rVaccine:
		rhdv="rabbit haemorrhagic disease virus"
		myxo="myxomatosis"

	class bVaccine:
		pox="poxvirus"
		para="paramyxovirus"
		poly="polyomavirus"

	class fVaccine:
		aero="aeromonas"
		vib="vibrio"
		yr="yersinia ruckeri"

class Colors:

	# mapped from SCHEMA.md 

	class dog(str, Enum):
		black="black"
		white="white"
		brown="brown"
		gold="golden"
		brindle="brindle"
		cream="cream"

	class cat(str, Enum):
		black="black"
		white="white"
		calico="calico"
		tabby="tabby"
		ginger="ginger"
		grey="grey"
		torquiseshell="torquiseshell"
	
	class bird(str, Enum):
		blue="blue"
		green="green"
		yellow="yellow"
		red="red"
		white="white"
		multi_colored="multi-colored"
		grey="grey"

	class fish(str, Enum):
		red='red'
		blue='blue'
		gold='gold'
		silver='silver'
		orange='orange'
		spotted='spotted'
		neon='neon'
	
	class Reptile(str, Enum):
		green='green'
		brown='brown'
		yellow='yellow'
		grey='grey'

	class Rabbit(str, Enum):
		white='white'
		black='black'
		grey='grey'
		cinnamon='cinnamon'
		spotted='spotted'
		agouti='agouti'
		brown='brown'

	class other(str, Enum):
		# TODO
		pass
		
class Breed: #TODO
	class dog(str, Enum):
		gr="golden retriever"
		
class VehicleType(str, Enum): # TODO
	ambulance="ambulance"
	van="van"
	car="car"
	bike="bike"
	pickup="pickup"

class Liscence:
	StateCodes = ["AP","AR","AS","BR","CH","DD","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LD","MP","MH","MN","ML","MZ","NL","OD","PB","PY","RJ","SK","TN","TS","TR","UP","UK","WB","AN","CG","CG"]


__all__ = ["Vaccines", "CompletionStatus", "Intervals", "PetType", "Colors", "Breed", "UserType", "VehicleType", "Liscence"]