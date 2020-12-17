import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import gzip,pickle

# ---------------------------------------------------------------------------------------------------------------------
def read_raw_data(file_path):
    with gzip.open(file_path) as fp:
        datapkl_raw = pickle.load(fp)

    return datapkl_raw

# ---------------------------------------------------------------------------------------------------------------------
def run():
    # ---  Initialization  ---
    ColorDictionary = {'respiration_thoracic': '#1f77b4',
                       'respiration_abdominal': '#ff7f0e',
                       'acceleration_X': '#2ca02c',
                       'acceleration_Y': '#d62728',
                       'acceleration_Z': '#9467bd'}

    CoughColorDictionary = {0: '#581845',
                           1: '#d62728',
                       2: '#9467bd',
                       3: '#8c564b',
                       4: '#e377c2',
                       5: '#7f7f7f',
                       6: '#bcbd22',
                       7: '#17becf'}

    TypeOfCoughDictionary = {0: 'cough sitting',
                            1: 'cough standing',
                            2: 'clearing of throat',
                            3: 'slight cough',
                            4: 'laugh',
                            5: 'surprise effect',
                            6: 'sentence',
                            7: 'inspiration'}

    #la lecture du disctionnaire
    pkl_raw='data/Cough_dataset/data_raw.pkl.zip'
    datapkl_raw=read_raw_data(pkl_raw)

    datatype_spec = datapkl_raw['datatype_spec']
    record_specs  = datapkl_raw['record_specs']
    patients_data = datapkl_raw['data']
    annotation    = datapkl_raw['annotation']

    for Patient in patients_data:
        fig = plt.figure()
        ax = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)
        ax3 = ax2.twinx()
        ax4 = ax.twinx()

        Time1 = np.arange(0, len(patients_data[Patient]['acceleration_X'])) * (
                    1 / datatype_spec['acceleration_X']['freq'])
        Time2 = np.arange(0, len(patients_data[Patient]['respiration_thoracic'])) * (
                    1 / datatype_spec['respiration_thoracic']['freq'])

        Cough = annotation[annotation[:, 1] == Patient]
        pltCough1 = {}
        for i in range(len(Cough)):
            x = np.where(Time1 <= Cough[i, 2])
            pltCough1 = ax4.axvline(x=x[0][-1] * (1 / datatype_spec['acceleration_X']['freq']),
                                    label=TypeOfCoughDictionary[Cough[i, 0]],
                                    c=CoughColorDictionary[Cough[i, 0]], linestyle=':', linewidth=1.5, alpha=0.7)
            x = np.where(Time2 <= Cough[i, 2])
            pltCough2 = ax2.axvline(x=x[0][-1] * (1 / datatype_spec['respiration_thoracic']['freq']),
                                    label=TypeOfCoughDictionary[Cough[i, 0]],
                                    c=CoughColorDictionary[Cough[i, 0]], linestyle=':', linewidth=1.5, alpha=0.7)

        pltAccX = ax.plot(Time1, patients_data[Patient]['acceleration_X'], label='acceleration_X', c=ColorDictionary['acceleration_X'], linewidth=0.5)
        pltAccY = ax.plot(Time1, patients_data[Patient]['acceleration_Y'], label='acceleration_Y', c=ColorDictionary['acceleration_Y'], linewidth=0.5)
        pltAccZ = ax.plot(Time1, patients_data[Patient]['acceleration_Z'], label='acceleration_Z', c=ColorDictionary['acceleration_Z'], linewidth=0.5)

        pltResT = ax2.plot(Time2, patients_data[Patient]['respiration_thoracic'], label='respiration_thoracic', c=ColorDictionary['respiration_thoracic'], linewidth=0.5)
        pltResA = ax3.plot(Time2, patients_data[Patient]['respiration_abdominal'], label='respiration_abdominal', c=ColorDictionary['respiration_abdominal'], linewidth=0.5)

        #ax.set_xlabel("Time (S)", color="black", fontsize=10)
        ax2.set_xlabel("Time (S)", color="black", fontsize=10)
        #ax2.set_xlabel("Time Respiration (S)", color="black", fontsize=10)
        ax.set_ylabel(r"Acceleration $(m/s^2)$", color="black", fontsize=10)
        ax2.set_ylabel("Respiration Thoracic", color="black", fontsize=10)
        ax3.set_ylabel("Respiration Abdominal", color="black", fontsize=10)

        ax.set_title("Acceleration", fontsize=12)
        ax2.set_title("Respiration", fontsize=12)
        fig.suptitle("Patient (" + str(Patient) + ")", fontsize=18)
        plt.grid()

        leg = pltAccX+pltAccY+pltAccZ+pltResT+pltResA
        labs = [l.get_label() for l in leg]
        Legend1 =ax.legend(leg, labs, loc='lower', ncol=5, bbox_to_anchor=(0.80, -1.35))

        for legobj in Legend1.legendHandles:
            legobj.set_linewidth(2.0)

        Legend2 = ax4.legend(*[*zip(*{l: h for h, l in zip(*ax4.get_legend_handles_labels())}.items())][::-1], ncol=8, bbox_to_anchor=(0.90, 1.20))
        for legobj in Legend2.legendHandles:
            legobj.set_linewidth(2.0)

        # Add second legend "Legend2" will be removed from figure
        ax.add_artist(Legend1)

        StartIter=0
        EndIter=len(patients_data[Patient]['acceleration_X'])*(1/64)
        majorStepIter=10
        minorStepIter = 5

        major_ticks = np.arange(StartIter, EndIter, majorStepIter)
        minor_ticks = np.arange(StartIter, EndIter, minorStepIter)
        ax.set_xticks(major_ticks)
        ax2.set_xticks(major_ticks)
        ax.tick_params(axis='x', rotation=45)
        ax2.tick_params(axis='x', rotation=45)
        ax.set_xticks(minor_ticks, minor=True)
        ax2.set_xticks(minor_ticks, minor=True)
        ax.tick_params(axis='both', which='major', labelsize=8)
        ax2.tick_params(axis='both', which='major', labelsize=8)
        ax3.tick_params(axis='both', which='major', labelsize=8)
        # ax3.spines["right"].set_position(("axes", 1.05))

        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        ax2.grid(which='both')
        ax2.grid(which='minor', alpha=0.2)
        ax2.grid(which='major', alpha=0.5)

        mng = plt.get_current_fig_manager()
        mng.window.showMaximized()
        plt.show(block=False)

        # Save figure
        MyFolder = "data/Figures/" + str(Patient) + "/"
        Path(MyFolder).mkdir(parents=True, exist_ok=True)
        filename = "Signals_Patient_" + str(Patient)
        fig.savefig(MyFolder + filename + ".png", dpi=600)  # Change is over here
        fig.savefig(MyFolder + filename + ".eps", format='eps')

        # Close Plot
        plt.close()

# ----------------------------------------------------------------------------------------------------------------------
# Main
if __name__ == '__main__':
    run()
