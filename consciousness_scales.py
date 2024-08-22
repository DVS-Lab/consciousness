
# Initialization
import os
from turtle import pd


def clear_all():
    # Close all variables
    globals().clear()

def close_all():
    # Close all figures (if any)
    import matplotlib.pyplot as plt # type: ignore
    plt.close('all')

def clc():
    # Clear console (no direct equivalent in Python)
    os.system('cls' if os.name == 'nt' else 'clear')

clear_all()
clear_all()
clc()

# Adapted from Daniel Sazhin StayGo 2 Project
# 03/23/24
# Neuroeconomics Lab
# Temple University.
# Consciousness Project

# This code takes in raw sourcedata and extracts the survey data

# FFMQ, SCD-Q, EBDM, Confirmation Bias, MCQ, Scam, FEVS

# Set directories
usedir = os.path.dirname(os.getcwd())
maindir = os.path.join(usedir, 'bids')
outputdir = os.path.join(usedir, 'bids')
codedir = os.path.join(usedir, 'code')

N = 34  # Total participants

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
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int) # type: ignore
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
            

# SCD-Q Questionanire
fname = 'scdq_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)
    
    with open(output, 'w') as fid:
        fid.write('participant_id\\tscdq_q1\tscdq_q2\tscdq_q3\tscdq_q4\tscdq_q5\tscdq_q5\tscdq_q6\tscdq_q7\tscdq_q8\tscdq_q9\tscdq_q10\tscdq_q11\tscdq_q12\tscdq_q13\tscdq_q14\tscdq_q15\tscdq_q16\tscdq_q17\tscdq_q17\tscdq_q18\tscdq_q19\tscdq_q20\tscdq_q21\tscdq_q22\tscdq_q23\tscdq_q24\tscdq_q25\tscdq_q26\tscdq_q27\n')
              
 
    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:27}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # SCD-Q
            start = data.iloc[0].tolist().index('scdq_q1')
            finish = data.iloc[0].tolist().index('scdq_q27')
            T = 27  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int) # type: ignore
            FF_Data = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_SCDQ_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                Yes = 1 if 'Yes' in question else 0
                No = 2 if 'No' in question else 0
            
                result = [Yes,No]
                
                Output_SCDQ_Data.extend(result)
                
            Output_SCDQ_Data = [str(x) for x in Output_SCDQ_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_SCDQ_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}") 
            
            # EBDM Questionnaire
fname = 'ebdm_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as fid:
    fid.write('participant_id\tEBDM_q1\tEBDM_q2\tEBDM_q3\tEBDM_q4\tEBDM_q5\tEBDM_q5\tEBDM_q6\tEBDM_q7\tEBDM_q8\tEBDM_q9\tEBDM_q10\tEBDM_q11\n')
              

    
    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:11}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # EBDM
            start = data.iloc[0].tolist().index('EBDM_q1')
            finish = data.iloc[0].tolist().index('EBDM_q11')
            T = 11  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int)
            FF_Data = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_EBDM_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                VeryInaccurate = 1 if 'Never inaccurate' in question else 0
                ModeratelyInaccurate = 2 if 'Moderately inaccurate' in question else 0
                NeitherAccurate = 3 if 'Neither accurate' in question else 0
                ModeratelyAccurate = 4 if 'Moderately accurate' in question else 0 
                VeryAccurate = 5 if 'Very accurate' in question else 0
                
                result = [VeryInaccurate, ModeratelyInaccurate, NeitherAccurate, ModeratelyAccurate, VeryAccurate]
                
                Output_EBDM_Data.extend(result)
                
            Output_EBDM_Data = [str(x) for x in Output_EBDM_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_EBDM_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}")
            
            # Confirmation Bias Questionnaire
fname = 'confirmationbias_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as fid:
   fid.write('participant_id\tconfirmationbias_q1\tconfirmationbias_q2\tconfirmationbias_q3\tconfirmationbias_q4\tconfirmationbias_q5\tconfirmationbias_q5\tconfirmationbias_q6\tconfirmationbias_q7\tconfirmationbias_q8\tconfirmationbias_q9\tconfirmationbias_q10\tconfirmationbias_q11\tconfirmationbias_q12\tconfirmationbias_q13\tconfirmationbias_q14\n')
     
                      

    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:14}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # Confirmation Bias
            start = data.iloc[0].tolist().index('Confirmationbias_q1')
            finish = data.iloc[0].tolist().index('Confirmationbias_q14')
            T = 14  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int)
            FF_Data = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_confirmationbias_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                StronglyDisagree = 1 if 'Strongly Disagree' in question else 0
                Disagree = 2 if 'Disagree' in question else 0
                Neutral = 3 if 'Neutral' in question else 0
                Agree = 4 if 'Agree' in question else 0 
                StronglyAgree = 5 if 'Strongly Agree' in question else 0
                
                result = [Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree]
                
                Output_confirmationbias_Data.extend(result)
                
            Output_confirmationbias_Data = [str(x) for x in Output_confirmationbias_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_confirmation_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}")
            
            
              # Metacognition Questionnaire
fname = 'MCQ_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as fid:
fid.write('participant_id\tMCQ_q1\tMCQ_q2\tMCQ_q3\tMCQ_q4\tMCQ_q5\tMCQ_q5\tMCQ_q6\tMCQ_q7\tMCQ_q8\tMCQ_q9\tMCQ_q10\tMCQ_q11\tMCQ_q12\tMCQ_q13\tMCQ_q14\tMCQ_q15\tMCQ_q16\tMCQ_q17\tMCQ_q17\tMCQ_q18\tMCQ_q19\tMCQ_q20\tMCQ_q21\tMCQ_q22\tMCQ_q23\tMCQ_q24\tMCQ_q25\tMCQ_q26\tMCQ_q27\tMCQ_q28\tMCQ_29\tMCQ_30\tMCQ_31\n')
              

    
    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:31}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # MCQ
            start = data.iloc[0].tolist().index('MCQ_q1')
            finish = data.iloc[0].tolist().index('MCQ_q31')
            T = 31  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int)
            FF_Data = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_MCQ_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                DonotAgree = 1 if 'Do not Agree' in question else 0
                AgreeSlightly = 2 if 'Agree Slightly' in question else 0
                AgreeModerately = 3 if 'Agree Moderately' in question else 0
                AgreeveryMuch = 4 if 'Agree very Much' in question else 0 
                
                result = [DonotAgree, AgreeSlightly, AgreeModerately, AgreeveryMuch]
                
                Output_MCQ_Data.extend(result)
                
            Output_MCQ_Data = [str(x) for x in Output_MCQ_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_MCQ_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}")
            
            
            # Scam Susceptibility Questionnaire
fname = 'scamsusceptibility_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as fid:
    fid.write('participant_id\tscamsusceptibility_q1\tscamsusceptibility_q2\tscamsusceptibility_q3\tscamsusceptibility_q4\tscamsusceptibility_q5\n')
                        

    
    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:5}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # Scam susceptibility
            start = data.iloc[0].tolist().index('scamsusceptibility_q1')
            finish = data.iloc[0].tolist().index('scamsusceptibility_q5')
            T = 5  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int)
          scamsusceptibility = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_scamsusceptibility_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                Stronglyagree = 1 if 'Strongly agree' in question else 0
                Agree = 2 if 'Agree' in question else 0
                Slightlyagree = 3 if 'Slightly agree' in question else 0
                Neitheragree = 4 if 'Neither agree' in question else 0 
                Slightlydisagree = 5 if 'Slightly disagree' in question else 0
                Disagree = 6 if 'Disagree'in question else 0
                Stronglydisagree = 7 if 'Strongly disagree'in question else 0
                
                result = [Stronglyagree, Agree, Slightlyagree, Neitheragree, Slightlydisagree, Disagree, Stronglydisagree ]
                
                Output_scamsusceptibility_Data.extend(result)
                
            Output_scamsusceptibility_Data = [str(x) for x in Output_scamsusceptibility_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_scamsusceptibility_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}")
            
            # FEVS Questionnaire
fname = 'FEVS_questionnaire.tsv'
output = os.path.join(usedir, 'bids', 'phenotype', fname)

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as fid:
    fid.write('participant_id\tFEVS_q1\tFEVS_q2\tFEVS_q3\n')
              

    
    for ii in range(1, N + 1):  # For each Participant
        try:
            partnum = f'{ii:3}'
            inputdir_name = os.path.join(maindir, 'sourcedata', f'sub-{partnum}', f'sub-{partnum}.xlsx')
            data = pd.read_excel(inputdir_name, header=None)
            
            # FEVS
            start = data.iloc[0].tolist().index('FEVS_q1')
            finish = data.iloc[0].tolist().index('FEVS_q3')
            T = 3  # Number of questions
            IndexedColumns = np.round(np.linspace(start, finish, T)).astype(int)
            FF_Data = data.iloc[:, IndexedColumns]  # Save them
            
            # Convert text into values
            Output_FEVS_Data = []
            for kk in range(T):
                question = data.iloc[1, IndexedColumns[kk]]
                
                Yes = 1 if 'Yes' in question else 0
                Somewhat = 2 if 'Somewhat' in question else 0
                No = 3 if 'No' in question else 0
            
                result = [Yes, Somewhat, No]
                
                Output_FEVS_Data.extend(result)
                
            Output_FEVS_Data = [str(x) for x in Output_FFMQ_Data]
            fid.write(f'sub-{partnum}\t' + '\t'.join(Output_FFMQ_Data) + '\n')
        
        except Exception as e:
            print(f"Error processing participant {ii}: {e}")

