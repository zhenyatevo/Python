class_rawinfo = {}
#new_heights = 0
#new_students = 0
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#class_info = []

with open('fileFOR ShamanstvoStepik.txt') as in_f_obj:
	for line in in_f_obj:
		string = line.rstrip().split('\t')

		if string[0] not in class_rawinfo:
			class_rawinfo[string[0]] = [int(string[2]), 1]
		elif string[0] in class_rawinfo:
			heights = class_rawinfo[string[0]][0] + int(string[2])
			students = class_rawinfo[string[0]][1] + 1
			class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
	class_info[int(k)-1] = v[0] / v[1]

with open('03_07_05_output.txt', 'w') as out_f_obj:	
	for i in range(len(class_info)):

		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
		print(output)
		out_f_obj.write(output)
