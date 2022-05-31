def calculate_score(salary,financialSituation,age , loanAmount, loanDuration, loanPurpose):
    initial_score=0
    if(age<20):
        initial_score=initial_score+0
    if (age >=20 and age < 40):
        initial_score+=20
    if (age >=40 and age < 60):
        initial_score+=10
    if (age >=60 and age < 80):
        initial_score+=5
    if (age >=80):
        initial_score+=0
    if (financialSituation=="good"):
        initial_score+=10
    if (financialSituation=="bad"):
        initial_score+=0
    if (loanAmount<=100000):
        initial_score+=20
    if (loanAmount>=100000 and loanAmount<200000):
        initial_score+=20
    if (loanAmount>=200000 and loanAmount<300000):
        initial_score+=10
    if (loanAmount>=300000):
        initial_score+=5
    if (loanDuration>=1 and loanDuration<3):
        initial_score+=20
    if (loanDuration>=3 and loanDuration<5):
        initial_score+=10
    if (loanDuration>=5):
        initial_score+=5
    if (loanPurpose=="car"):
        initial_score+=10
    if (loanPurpose=="house"):
        initial_score+=5
    if (loanPurpose=="other"):
        initial_score+=0
    if (salary>=1000 and salary<2000):
        initial_score+=5
    if (salary>=2000 and salary<3000):
        initial_score+=10
    if (salary>=3000):
        initial_score+=20
    return initial_score


    