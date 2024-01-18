import matplotlib.pyplot as plt
import csv
import pandas as pd

SHOW = True
SAVE = False

years = []
paper_id = []
change_source = []
change_type = []
change_anticipation = []
change_frequency = []

mech_type = []
mech_orgn = []
mech_scpe = []
mech_dura = []
mech_time = []
mech_trig = []

effect_crit = []
effect_pred = []
effect_over = []
effect_resl = []

sw_plat = []
manage_ind = []

# "I0 Mission"
# I1.1 Metadata
# I1.2 Source of Change
# I1.2 Type of Change
# I1.2 Anticipation of Change
# I1.2 Frequency of Change	
# I1.3 Type of Mechanism	
# I1.3 Organization of Mechanism	
# I1.3 Scope of Mechanism	
# I1.3 Duration of Mechanism	
# I1.3 Timeliness of Mechanism	
# I1.3 Trigger of Mechanism	
# I1.4 Criticality of Effects	
# I1.4 Predictability of Effects	
# I1.4 Overhead of Effects	
# I1.4 Resilience of Effects	
# I2 Adap. Purpose	
# I3 Robot Type
# I4 Robo SW	I5 QA	I6 Independence	I7 Deployment Realness	I7 Mission Realness	I8 Evaluation	I9 Adap. Logic	I10 Monitor	I11 Analyze	I12 Plan	I13 Execute	I14 Knowledge


show_or_save = SAVE

plt.style.use('ggplot')

def plot_plot(title):
    plt.tight_layout()
    if(show_or_save == SAVE):
        plt.savefig(title)
    if(show_or_save == SHOW):
        plt.show()


def multi_df_plot(possibilities, original_data, subject_title, plot_title):

    occurrences_of_type = [0] * len(possibilities)

    for i, some__type in enumerate(possibilities):
        for type_occ in original_data:
            if(some__type in type_occ): occurrences_of_type[i]+=1

    type_df = pd.DataFrame(data={subject_title: possibilities, 'Num. Occurrences': occurrences_of_type})
    print(type_df)
    smt = type_df.plot(kind='bar', legend=False, ylabel='Num. Occurrences', xlabel=subject_title)
    smt.set_xticklabels(possibilities)

    plot_plot(plot_title)


def effect_dimension():

    standard_fields = ["I1.4 Criticality of Effects","I1.4 Overhead of Effects", "I1.4 Resilience of Effects"]

    for i, field_name in enumerate(standard_fields):

        eff_elem = effect_csv_titles[field_name]

        some_eff_df = pd.DataFrame(data={'ID': paper_id, csv_title_to_plot_title[field_name]: eff_elem})

        print(some_eff_df)
        count_by_source =  some_eff_df.groupby(csv_title_to_plot_title[field_name]).count()

        plot = count_by_source.plot(kind='bar', legend=False, ylabel="Number of Studies")
        plot_plot("plots/" +  csv_title_to_plot_title[field_name] + ".pdf")


    pred_poss = ["Deterministic", "Non-deterministic"]

    multi_df_plot(pred_poss,effect_pred,csv_title_to_plot_title["I1.4 Predictability of Effects"], "plots/" + csv_title_to_plot_title["I1.4 Predictability of Effects"] + ".pdf")

def mech_dimension():

    standard_fields = ["I1.3 Organization of Mechanism", "I1.3 Duration of Mechanism", "I1.3 Timeliness of Mechanism", "I1.3 Trigger of Mechanism"]

    for i, field_name in enumerate(standard_fields):

        mech_elem = mech_csv_titles[field_name]

        some_mech_df = pd.DataFrame(data={'ID': paper_id, csv_title_to_plot_title[field_name]: mech_elem})

        print(some_mech_df)
        count_by_source =  some_mech_df.groupby(csv_title_to_plot_title[field_name]).count()

        plot = count_by_source.plot(kind='bar', legend=False, ylabel="Number of Studies")
        plot_plot("plots/" +  csv_title_to_plot_title[field_name] + ".pdf")


    multi_df_plot(["Structural", "Parametric"],mech_type,"Type of Mechanism", "plots/Type of Mechanism.pdf")
    multi_df_plot(["Global", "Local"],mech_scpe, "Scope of Mechanism", "plots/Scope of Mechanism.pdf")


def change_dimension():


    for i, change_elem in enumerate( ([change_csv_titles[0]] + change_csv_titles[2:]) ):

        some_change_df = pd.DataFrame(data={'ID': paper_id, csv_title_to_plot_title[change_elem[0]]: change_elem[1]})

        print(some_change_df)
        count_by_source =  some_change_df.groupby(csv_title_to_plot_title[change_elem[0]]).count()

        plot = count_by_source.plot(kind='bar', legend=False, ylabel="Number of Studies")

        plot_plot("plots/" +  csv_title_to_plot_title[change_elem[0]] + ".pdf")



    change_type_poss = ["Technological", "Non-functional", "Functional"]

    multi_df_plot(change_type_poss,change_type, "Type of Change", "plots/Type of Change.pdf")


def barplot_paper_id_by_x(x, plot_filename, x_title):
    x_df = pd.DataFrame(data={'ID': paper_id, x_title: x})

    count_by_x_df =  x_df.groupby(x_title).count()

    plot = count_by_x_df.plot(kind='bar', legend=False, ylabel="Number of Studies")

    plot_plot(plot_filename)


def plot_by_year(p_ids,p_years):
    barplot_paper_id_by_x(p_years,"plots/plot_by_year.pdf","Publication Year")



    

change_csv_titles = [
    ("I1.2 Source of Change",change_source),
    ("I1.2 Type of Change",change_type),
    ("I1.2 Anticipation of Change",change_anticipation),
    ("I1.2 Frequency of Change",change_frequency)
]

mech_csv_titles = {
    "I1.3 Type of Mechanism" : mech_type,
    "I1.3 Organization of Mechanism" : mech_orgn,
    "I1.3 Scope of Mechanism" : mech_scpe,
    "I1.3 Duration of Mechanism" : mech_dura,
    "I1.3 Timeliness of Mechanism" : mech_time,
    "I1.3 Trigger of Mechanism" : mech_trig
}

effect_csv_titles = {
    "I1.4 Criticality of Effects" : effect_crit,
    "I1.4 Predictability of Effects" : effect_pred,
    "I1.4 Overhead of Effects" : effect_over,
    "I1.4 Resilience of Effects" : effect_resl,
}

csv_title_to_plot_title = {
    "I1.2 Source of Change" : "Source of Change",
    "I1.2 Type of Change" : "Type of Change",
    "I1.2 Anticipation of Change" : "Anticipation of Change",
    "I1.2 Frequency of Change" : "Frequency of Change",
    "I1.3 Type of Mechanism" : "Type of Mechanism",
    "I1.3 Organization of Mechanism" : "Organization of Mechanism",
    "I1.3 Duration of Mechanism" : "Duration of Mechanism",
    "I1.3 Scope of Mechanism" : "Scope of Mechanism",
    "I1.3 Timeliness of Mechanism" : "Timeliness of Mechanism",
    "I1.3 Trigger of Mechanism" : "Trigger of Mechanism",
    "I1.4 Predictability of Effects" : "Predictability of Effects",
    "I1.4 Criticality of Effects" : "Criticality of Effects",
    "I1.4 Overhead of Effects" : "Overhead of Effects",
    "I1.4 Resilience of Effects" : "Resilience of Effects",
    "I4 Robo SW" : "Software Platform",
    "I6 Independence" : "Managing System Independence",


}



with open('data/partiallyclean.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(csv_reader):
        paper_id.append(row['Paper ID'])
        years.append(int(row['year']))
        sw_plat.append(row["I4 Robo SW"])
        manage_ind.append(row["I6 Independence"])

        for change_elem in change_csv_titles:
            change_elem[1].append(row[change_elem[0]])
        
        for mech_key in list(mech_csv_titles.keys()):
            mech_csv_titles[mech_key].append(row[mech_key])

        for eff_key in list(effect_csv_titles.keys()):
            effect_csv_titles[eff_key].append(row[eff_key])

    #plot_by_year(years, paper_id)
    # change_dimension()
    mech_dimension()  
    # effect_dimension()
    # barplot_paper_id_by_x(sw_plat,"plots/plot_by_swplat.pdf","Software Platform")
    #barplot_paper_id_by_x(manage_ind,"plots/plot_by_indepedence.pdf",csv_title_to_plot_title["I6 Independence"])
            
            

