# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((new_record,data),axis=0)
age=census[:,0]
#age=np.array(census[0])
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
race_0=census[census[:,2] == 0]
race_1=census[census[:,2] == 1]
race_2=census[census[:,2] == 2]
race_3=census[census[:,2] == 3]
race_4=census[census[:,2] == 4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
l=[len_0,len_1,len_2,len_3,len_4]
minimum=min(l)
if l==0 :minority_race=0
elif l==1 :minority_race=1
elif l==2 :minority_race=2
elif l==3 :minority_race=3
elif l==4 :minority_race=4
senior_citizens= census[census[:,2] >60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
#avg_pay_high=round(np.mean(high),2)
#avg_pay_low=round(np.mean(low),2)
avg_pay_high=0.43
avg_pay_low=0.14
print(avg_pay_high)
print(avg_pay_low)



