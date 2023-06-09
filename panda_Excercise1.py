import pandas as  pd

sal = pd.read_csv('Salaries.csv')
print(sal)
print(sal['BasePay'].mean())

# print(sal.describe())

print(sal['OvertimePay'].max())

print(sal[sal['EmployeeName'] =='JOSEPH DRISCOLL']['JobTitle'])

print(sal[sal['EmployeeName'] =='JOSEPH DRISCOLL']['TotalPayBenefits'])


print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()])

print(sal.loc[sal['TotalPayBenefits'].idxmax()])

print(sal.loc[sal['TotalPayBenefits'].idxmin()])

print(sal.groupby('Year')['BasePay'].mean())

print( len(sal.groupby('JobTitle')))
print( sal['JobTitle'].nunique())

print(sal['JobTitle'].value_counts().head(5))

print(sum(sal[sal['Year'] ==2013]['JobTitle'].value_counts()==1))
def cheif_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: cheif_string(x))))

sal['title_len'] = sal['JobTitle'].apply(len)

print(sal[['TotalPayBenefits','title_len']].corr())