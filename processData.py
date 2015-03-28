import re
import sqlite3
from collections import defaultdict
from django.conf import settings
from hackday2.wsgi.openshift.models import models




text_file = open("school.txt", "r")
file_students = open("student.txt","r")
file_network_school = open("network.txt")

conn = sqlite3.connect('sqlite3.db')

c = conn.cursor()
# openshift_aluno
#openshift_rede
#openshift_escola





def process_text(text_file):
	locations = []
	lines = text_file.read().decode('iso8859-1').split('\n') #this geretaes the u before string
	for line in lines:
		line = line.replace('"', '')
		locations.append(line.split("\t"))
	return locations


#location[3] == login
#location[4] == student id
#location[2] == turma
locations = process_text(text_file)
logins = defaultdict(lambda: 1)
for item in locations:
	if(len(item)==1):
		break
	elif(len(item)>4):
		if(item[3] not in logins.keys()):
			logins[item[3]] = defaultdict(list)

		logins[item[3]][item[2]].append(item[4])
# locations[1][1] -> primeira rede
students_list = process_text(file_students)
network_list = process_text(file_network_school)




network_dict = defaultdict(list)
for element in network_list:
	if(len(element) == 1):
		break
	elif(len(element)>3):
		if(element[3] not in network_dict.keys()):
			network_dict[element[3]].append(element[1])
			network_dict[element[3]].append(element[2])




#popular o banco
networks = []
for item in network_dict.values():
	if (item[0] not in networks):
		networks.append(item[0])
		c.execute("INSERT INTO openshift_rede VALUES (NULL,?)", (item[0],))




student_dict = defaultdict(lambda: 1)
for student in students_list:
	if(len(student) == 0):
		break
	elif(len(student)>13):
		if(student[1] not in student_dict.keys()):
			student_dict[student[1]] = defaultdict(lambda: 1)
		if(student[2] not in student_dict[student[1]].keys()):
			student_dict[student[1]][student[2]] = defaultdict(list)
		if(student[3] != "#N/A"):
			#"com.dificuldade"	"precisa_praticar"	"praticado"	"nivel1"	"nivel2"	"dominado"	"pontos"	"exerciseminutes"	"videominutes"	"totalminutes"
			student_dict[student[1]][student[2]][int(student[3])].append(student[4])
			student_dict[student[1]][student[2]][int(student[3])].append(student[5])
			student_dict[student[1]][student[2]][int(student[3])].append(student[6])
			student_dict[student[1]][student[2]][int(student[3])].append(student[7])
			student_dict[student[1]][student[2]][int(student[3])].append(student[8])
			student_dict[student[1]][student[2]][int(student[3])].append(student[9])
			student_dict[student[1]][student[2]][int(student[3])].append(student[10])
			student_dict[student[1]][student[2]][int(student[3])].append(student[11])
			student_dict[student[1]][student[2]][int(student[3])].append(student[12])
			student_dict[student[1]][student[2]][int(student[3])].append(student[13])
			c.execute("INSERT INTO openshift_aluno VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", (student[3], student[2], student[1], student[4], student[5],
	student[6], student[7], student[8], student[9], student[10], student[11], student[12], student[13]))



print student_dict['Week2014_09_14']['cimepeterpan@gmail.com'][1]





#Ta tendo duplicacao de dados e eu n sei o motivo entao eu fiz um set
#faz um set pra remover dados duplicados

for element in logins:
	tmp = []
	tmp_student = []	
	for single_element in logins[element]:
		logins[element][single_element] = set(logins[element][single_element])
		logins[element][single_element] = list(logins[element][single_element])
		tmp.append(single_element)
		tmp_student.append(logins[element][single_element])

	#print element
	#print type(str(tmp)
	#print tmp_student
	#print network_dict['sp.alvescruz']
	c.execute("SELECT * FROM openshift_rede WHERE nome = ?",(network_dict[element][0],))
	test = c.fetchone() 
	c.execute("INSERT INTO openshift_escola VALUES (?,?,?,?)", (test,element,str(tmp_student),str(tmp_student),))




print logins['cimepeterpan@gmail.com']["[u'PETERPAN_5B_2014_AM']"]

conn.commit()
conn.close()

