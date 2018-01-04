from vs import *

obj_handles = []
total_chairs = 0

def GetSelectedHandles():

	num_sel_obj = NumSObj(ActLayer())
	
	for i in range(num_sel_obj):
		current_obj = FSActLayer()
		obj_handles.append(current_obj)
		SetDSelect(current_obj)
	
	for i in obj_handles:
		SetSelect(i)

def GetNumChairs(h):
	
	rec_handle = GetParametricRecord(h, 0)
	rec_name = GetName(rec_handle)
	fld_name = GetFldName(rec_handle, 3)

	return int(GetRField(h, rec_name, fld_name))


GetSelectedHandles()

for i in obj_handles:
	total_chairs += GetNumChairs(i)
	
#AlrtDialog("Total Chairs: ", total_chairs)
Message("Total Chairs: ", total_chairs)
