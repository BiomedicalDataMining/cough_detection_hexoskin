import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from pathlib import Path
import gzip,pickle
import csv
import ast

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

    #la lecture du disctionnaire
    pkl_raw='data/Cough_dataset/data_raw.pkl.zip'
    datapkl_raw=read_raw_data(pkl_raw)

    datatype_spec = datapkl_raw['datatype_spec']
    record_specs  = datapkl_raw['record_specs']
    patients_data          = datapkl_raw['data']
    annotation    = datapkl_raw['annotation']

    for Patient in patients_data:
        #fig = plt.gcf()
        fig, ax = plt.subplots()
        ax2 = ax.twinx()#.twiny()
        ax3 = ax.twinx()  # .twiny()

        for Signal in patients_data[Patient]:
            SignalData = patients_data[Patient][Signal]
            Time = np.arange(0, len(patients_data[Patient][Signal])) * (1/datatype_spec[Signal]['freq'])
            #x = np.where(Time == record_specs[Patient]['offset_start'])

            if "acceleration_" in Signal:
                ax.plot(Time, SignalData, label=Signal, c=ColorDictionary[Signal], linewidth=0.5)
            elif "respiration_thoracic" in Signal:
                ax2.plot(Time, SignalData, label=Signal, c=ColorDictionary[Signal], linewidth=0.5)
            elif "respiration_abdominal" in Signal:
                ax3.plot(Time, SignalData, label=Signal, c=ColorDictionary[Signal], linewidth=0.5)

        ax.set_xlabel("Time (S)", color="black", fontsize=10)
        #ax2.set_xlabel("Time Respiration (S)", color="black", fontsize=10)
        ax.set_ylabel(r"Acceleration $(m/s^2)$", color="black", fontsize=10)
        ax2.set_ylabel("Respiration", color="black", fontsize=10)

        plt.title("Patient (" + str(Patient) + ")\n", fontsize=18)
        plt.grid()

        leg = ax.legend(loc='lower left', borderaxespad=0.1,  title="Acceleration", bbox_to_anchor=(0.1, -0.13), ncol = 3)
        for legobj in leg.legendHandles:
            legobj.set_linewidth(2.0)

        leg = ax2.legend(loc='lower right', borderaxespad=0.1,  title="Respiration", bbox_to_anchor=(0.85, -0.13), ncol = 2)
        for legobj in leg.legendHandles:
            legobj.set_linewidth(2.0)



        StartIter=0
        EndIter=len(patients_data[Patient]['acceleration_X'])*(1/64)
        majorStepIter=10
        minorStepIter = 5
        major_ticks = np.arange(StartIter, EndIter, majorStepIter)
        minor_ticks = np.arange(StartIter, EndIter, minorStepIter)
        ax.set_xticks(major_ticks)
        #plt.xticks(rotation=54)
        ax.tick_params(axis='x', rotation=45)
        #ax2.tick_params(axis='x', rotation=45)
        ax.set_xticks(minor_ticks, minor=True)

        ax.tick_params(axis='both', which='major', labelsize=8)
        ax2.tick_params(axis='both', which='major', labelsize=8)
        ax3.tick_params(axis='both', which='major', labelsize=8)
        ax3.spines["right"].set_position(("axes", 1.05))

        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

        mng = plt.get_current_fig_manager()
        mng.window.showMaximized()
        plt.show()

        # # Save figure
        # MyFolder = "data/Figures/" + Patient + "/"
        # Path(MyFolder).mkdir(parents=True, exist_ok=True)
        # filename = Signal + "_Patient_" + Patient
        # fig.set_size_inches((32 / 2, 16.05 / 2), forward=False)
        # fig.savefig(MyFolder + filename + ".png", dpi=600)  # Change is over here
        # fig.savefig(MyFolder + filename + ".eps", format='eps')


# ----------------------------------------------------------------------------------------------------------------------
# Main
if __name__ == '__main__':
    run()
