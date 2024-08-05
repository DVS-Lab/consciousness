import os
import shutil
import pandas as pd

# Initialization
def clear_all():
    # Clear all variables
    globals().clear()

def close_all():
    # Close all figures (if any)
    import matplotlib.pyplot as plt
    plt.close('all')

def clc():
    # Clear console (no direct equivalent in Python)
    os.system('cls' if os.name == 'nt' else 'clear')

clear_all()
close_all()
clc()

# Adapted by Daniel Sazhin StayGo 2 Project
# 03/23/24
# Neuroeconomics Lab
# Temple University.
# Consciousness Project

# This code takes in raw sourcedata and extracts the survey data

# FFMQ

# Set directories
usedir = os.path.dirname(os.getcwd())
maindir = os.path.join(usedir, 'bids')
outputdir = os.path.join(usedir, 'bids')
codedir = os.path.join(usedir, 'code')

N = 9  # Total participants

# FFMQ Questionnaire
fname = 'ffmq_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as fid:
    fid.write('participant_id\tFF_q1\tFF_q2\tFF_q3\tFF_q4\tFF_q5\tFF_q5\tFF_q6\tFF_q7\tFF_q8\tFF_q9\tFF_q10\tFF_q11\tFF_q12\tFF_q13\tFF_q14\tFF_q15\tFF_q16\tFF_q17\tFF_q17\tFF_q18\tFF_q19\tFF_q20\tFF_q21\tFF_q22\tFF_q23\tFF_q24\tFF_q25\tFF_q26\tFF_q27\tFF_q28\tFF_29\tFF_30\tFF_31\tFF_32\tFF_q33\tFF_q34\tFF_q35\tFF_q36\tFF_q37\tFF_q38\tFF_q39\n')
              

    
    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:39}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # FFMQ
            start = data.iloc[0].tolist().index('FF_q1')
            finish = data.iloc[0].tolist().index('FF_q39')
            T = 39  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int)
            FF_Data = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_FFMQ_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                NeverTrue = 1 if 'Never or very rarely true' in question else 0
                RarelyTrue = 2 if 'Rarely true' in question else 0
                SometimesTrue = 3 if 'Sometime true' in question else 0
                OftenTrue = 4 if 'Often true' in question else 0 
                VeryTrue = 5 if 'Very often or always true' in question else 0
                
                result = [NeverTrue, RarelyTrue, SometimesTrue, OftenTrue, VeryTrue]
                
                Output_FFMQ_Data.extend(result)
                
            Output_FFMQ_Data = [str(x) for x in Output_FFMQ_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_FFMQ_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}")
