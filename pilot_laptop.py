import csv
import numpy as np

robotics_entries = []
architecture_entries = []
adaptive_entries = []

SEED = 1337

PILOT_SIZE = 120
np.random.seed(SEED)

def create_reviewer_file(file_name, reviewer_studies):
    csv_file = open(file_name+'.csv', 'w', encoding='utf-8', newline="")

    fieldnames =  list(reviewer_studies[0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for study in reviewer_studies:
        writer.writerow(study)
    
    csv_file.close()


category_to_list = {
    "Software_Architecture" : architecture_entries,
    "Robotics" : robotics_entries,
    "Self-Adaptive_Systems" : adaptive_entries
}




with open(input("csv input file name > "), 'r', encoding='utf-8', newline="") as csvfile:
    venue_reader = csv.DictReader(csvfile)
    #next(venue_reader) #skip header

    for row in venue_reader:
        del row['hit num']
        category_to_list[row["venue_category"]].append(row)


all_entries_before_pilots = architecture_entries + robotics_entries + adaptive_entries
identifiers_before_pilots = []
for entry in all_entries_before_pilots:
    identifiers_before_pilots.append(entry['ee'])


one_third_chunk = int(PILOT_SIZE/3)

robot_selection = list(np.random.choice(robotics_entries,one_third_chunk,replace=False))
archi_selection = list(np.random.choice(architecture_entries,one_third_chunk,replace=False))
adapt_selection = list(np.random.choice(adaptive_entries,one_third_chunk,replace=False))

pilot_studies = robot_selection + archi_selection + adapt_selection

np.random.shuffle(pilot_studies)


REVIEWER1 = pilot_studies[:one_third_chunk]
REVIEWER2 = pilot_studies[one_third_chunk:2*one_third_chunk]
REVIEWER3 = pilot_studies[2*one_third_chunk:]

# create_reviewer_file("reviewer1b",REVIEWER1)
# create_reviewer_file("reviewer2b",REVIEWER2)
# create_reviewer_file("reviewer3b",REVIEWER3)

#PILOT 2
for selected in robot_selection: robotics_entries.remove(selected)
for selected in archi_selection: architecture_entries.remove(selected)
for selected in adapt_selection: adaptive_entries.remove(selected)

robot_selection = list(np.random.choice(robotics_entries,one_third_chunk,replace=False))
archi_selection = list(np.random.choice(architecture_entries,one_third_chunk,replace=False))
adapt_selection = list(np.random.choice(adaptive_entries,one_third_chunk,replace=False))

pilot_studies = robot_selection + archi_selection + adapt_selection
np.random.shuffle(pilot_studies)

REVIEWER1 = pilot_studies[:one_third_chunk]
REVIEWER2 = pilot_studies[one_third_chunk:2*one_third_chunk]
REVIEWER3 = pilot_studies[2*one_third_chunk:]

# create_reviewer_file("p2reviewer1b",REVIEWER1)
# create_reviewer_file("p2reviewer2b",REVIEWER2)
# create_reviewer_file("p2reviewer3b",REVIEWER3)

###FINAL SELECTIONS
new_stuff = []

with open(input("second csv input file name > "), 'r', encoding='utf-8', newline="") as csvfile:
    venue_reader = csv.DictReader(csvfile)
    #next(venue_reader) #skip header
    for row in venue_reader:
        del row['hit num']
        new_stuff.append(row)

# print(new_stuff)
# input("wow")

to_be_removed = []
for entry in new_stuff: 
    try:
        if(entry['ee'] in identifiers_before_pilots):
            to_be_removed.append(entry)
    except ValueError:
        print("err")

for to_remove in to_be_removed: new_stuff.remove(to_remove)

for selected in robot_selection: robotics_entries.remove(selected)
for selected in archi_selection: architecture_entries.remove(selected)
for selected in adapt_selection: adaptive_entries.remove(selected)

remaining_after_pilots = robotics_entries + architecture_entries + adaptive_entries

final_set = remaining_after_pilots + new_stuff

np.random.shuffle(final_set)

total_num = len(final_set)

equal_part = int(total_num/6)
print(equal_part)
input("ah")

first_share = equal_part * 3 #Elvin does the work of 3
print(len(final_set))
ELVIN = final_set[:first_share]

REVIEWER1 = final_set[first_share:first_share+equal_part] #reviewer1 does 1/6th
REVIEWER2 = final_set[first_share+equal_part:first_share+equal_part+equal_part] #reviewer 2 does the 1/6th after that
REVIEWER3 = final_set[first_share+equal_part+equal_part:] #the remaining 1/6th or so goes to reviewer3

print(len(ELVIN))
input("ELFEEN")
print(len(REVIEWER1))
input('R1')
print(len(REVIEWER2))
input('R2')
print(len(REVIEWER3))
input("R3")

# create_reviewer_file("finalreviewerE",ELVIN)
# create_reviewer_file("finalreviewer1",REVIEWER1)
# create_reviewer_file("finalreviewer2",REVIEWER2)
# create_reviewer_file("finalreviewer3",REVIEWER3)