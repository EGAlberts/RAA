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
        category_to_list[row["venue_category"]].append(row)


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

create_reviewer_file("p2reviewer1b",REVIEWER1)
create_reviewer_file("p2reviewer2b",REVIEWER2)
create_reviewer_file("p2reviewer3b",REVIEWER3)
