# Description

The cough detection Dataset contains 9 subjects that performed the following steps 10 consecutive times:

## Subjects description
The physiological information can be found in *Anthropometry.csv* file.
- Read as per the header (record_id, weight, height, age, gender)
- NA value mean subject measurement is not available

## Types of activity labeled
- 0: cough sitting
- 1: cough standing
- 2: clearing of throat
- 3: slight cough
- 4: laugh
- 5: surprise effect
- 6: sentence
- 7: inspiration

Following the acquisition, the event were manually annotated by one operator.

# Data
The data found in *data.pkl.zip* can be extracted in python using the command:

    import gzip,pickle

    pkl_raw='data_raw.pkl.zip'
    with gzip.open(pkl_zip_file) as fp:
        datapkl = cPickle.load(fp)
        
The datapkl['data'] contains the following channels recorded by Hexoskin devices:

- datapkl['data']: {dict}
  - acceleration_X, 64 Hz
  - acceleration_Y, 64 Hz
  - acceleration_Z, 64 Hz
  - respiration_thoracic, 128 Hz
  - respiration_abdominal, 128 Hz
- data['annotation']: {ndarray}
  - The annotation as found in *annotation.csv*
  - read as (datatype_spec_type, record_spec_id, time(sec) )
- data['datatype_spec']: {dict}
  - Acquisition frequency for each channel
  - Read 
- data['record_specs']: {dict}
  - Offset of the original record. This is stored for reference purpose only.
 
# Annotation
The annotation are found in the file  *annotation.csv* as well as in *data.pkl.zip*



# Internal Note
Original data found in /Google Drive/Hexoskin_Protocoles/Rapports_Techniques/Cough_protocol
git@bitbucket.org:carre/cough_detection.git