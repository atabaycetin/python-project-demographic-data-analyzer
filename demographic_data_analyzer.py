import numpy as np
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df[df.sex == 'Male'].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df.education == 'Bachelors'].education.count() / df.education.count() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(df[((df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')) & (df.salary == '>50K')].salary.count() / df[((df.education == 'Bachelors') | (df.education == 'Masters')|( df.education == 'Doctorate'))].salary.count() * 100, 1)
    lower_education = round(df[(~((df.education == 'Bachelors') | (df.education == 'Masters')|( df.education == 'Doctorate'))) & (df.salary == '>50K')].salary.count() / df[(~((df.education == 'Bachelors') | (df.education == 'Masters')|( df.education == 'Doctorate')))].salary.count()*100, 1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = round(df[(df['hours-per-week'] == min_work_hours) & (df.salary == '>50K')].salary.count() / df[(df['hours-per-week'] == min_work_hours)].salary.count() * 100, 1)
    rich_percentage = num_min_workers

    # What country has the highest percentage of people that earn >50K?
    richest_country = (df['native-country'][df.salary == '>50K'].value_counts() / df['native-country'].value_counts() * 100).idxmax()
    max_perc = max(round(df['native-country'][df.salary == '>50K'].value_counts() / df['native-country'].value_counts() * 100, 1))
    highest_earning_country = richest_country
    highest_earning_country_percentage = max_perc

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[df['native-country'] == 'India'][df.salary == '>50K'].occupation.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == "__main__":
    calculate_demographic_data()

# These are my old codes that I've used because of my lack of knowledge in Pandas module when I first started. I know that these are the most unefficient way to complete the tasks, and I know that they look terrible, that's why I decided to re-code this project.
  
    """edu_count = 0
    bach_count = 0
    for i in df['education']:
        edu_count += 1
        if i == 'Bachelors':
            bach_count += 1"""
    """sum_age_men = 0
    male_count = 0
    for i in df.index:
        if df.loc[i]['sex'] == 'Male':
            male_count += 1
            sum_age_men += df.loc[i]['age']"""
    """advedu_count = 0
    advk50_count = 0
    for i in df.index:
        if df.loc[i]['education'] == 'Bachelors' or df.loc[i]['education'] == 'Masters' or df.loc[i]['education'] == 'Doctorate':
            advedu_count += 1
            if df.loc[i]['salary'] == '>50K':
                advk50_count += 1
    higher_education = round(advk50_count / advedu_count * 100, 1)"""
    """nonadvedu_count = 0
    k50_count = 0
    for i in df.index:
        if df.loc[i]['education'] != 'Bachelors' and df.loc[i]['education'] != 'Masters' and df.loc[i]['education'] != 'Doctorate':
            nonadvedu_count += 1
            if df.loc[i]['salary'] == '>50K':
                k50_count += 1

    lower_education = round(k50_count / nonadvedu_count * 100, 1)
    """
    """min_count = 0
    minsal_count = 0
    for i in df.index:
        if df.loc[i]['hours-per-week'] == min_work_hours:
            min_count += 1
            if df.loc[i]['salary'] == '>50K':
                minsal_count += 1
    num_min_workers = round(minsal_count / min_count * 100, 1)"""
    """richcountryrich_dict = dict()
        richcountrycount_dict = dict()
        richcountry_list = list()
        for i in df.index:
            if df.loc[i]['native-country'] not in richcountrycount_dict:
                richcountrycount_dict[df.loc[i]['native-country']] = 1
            else:
                richcountrycount_dict[df.loc[i]['native-country']] += 1
            if df.loc[i]['native-country'] not in richcountryrich_dict:
                if df.loc[i]['salary'] == '>50K':
                    richcountryrich_dict[df.loc[i]['native-country']] = 1
            else:
                if df.loc[i]['salary'] == '>50K':
                    richcountryrich_dict[df.loc[i]['native-country']] += 1
        for i in richcountryrich_dict:
            if i in richcountrycount_dict:
                richcountry_list.append((i, round(richcountryrich_dict[i] / richcountrycount_dict[i] * 100, 1)))
        maxperc_list = list()
        for i in range(len(richcountry_list)):
            maxperc_list.append(richcountry_list[i][1])
        max_perc = max(maxperc_list)
        for i in range(len(richcountry_list)):
            if richcountry_list[i][1] == max_perc:
                richest_country = richcountry_list[i][0]"""
    """occ_dict = dict()
    for i in df.index:
        if df.loc[i]['native-country'] == 'India':
            if df.loc[i]['salary'] == '>50K':
                if df.loc[i]['occupation'] not in occ_dict:
                    occ_dict[df.loc[i]['occupation']] = 1
                else:
                    occ_dict[df.loc[i]['occupation']] += 1
    max_occ = max(occ_dict.values())
    for k, v in occ_dict.items():
        if v >= max_occ:
            top_IN_occupation = k
    print(top_IN_occupation)"""