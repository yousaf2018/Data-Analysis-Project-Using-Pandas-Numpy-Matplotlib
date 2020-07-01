# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 08:24:19


Data Analysis Project 

Members for Project 

1) Mahmood Yousaf

2) Hamdan Ali Baloch


"""
#Importing librirary for data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Reading provinding data in csv format by using pandas funtions
data = pd.read_csv("Gapminder.csv")
#By using pandas selection divided data into chunks by yearwise
Year = 1952
Yearly_Country_wise_list = []
while True:
    chunk = data[data['Year']==Year]
    length = len(chunk)
    index = np.arange(length)
    chunk.set_axis(index,inplace=True)
    Yearly_Country_wise_list.append(chunk)
    Year = Year + 4
    if Year == 2016:
        break
#We are ranking each country yearwise using using max and min by pandas
#After Ranking selected columns than inserting into dataframe 
for i in Yearly_Country_wise_list:
    TotalGDPUS = i.loc[:,'TotalGDPUS'].rank(method='max',ascending=False)
    #Handling missing values for proper ranking 
    TotalGDPUS = TotalGDPUS.fillna(0)
    i.insert(55,"RankTotalGDPUS",TotalGDPUS,True)
    AgriculturalLand = i.loc[:,'AgriculturalLand'].rank(method='max',ascending=False)
    AgriculturalLand = AgriculturalLand.fillna(0)
    i.insert(56,"RankAgriculturalLand",AgriculturalLand,True)
    ChildrenPerWoman = i.loc[:,'ChildrenPerWoman'].rank(method='min',ascending=True)
    ChildrenPerWoman = ChildrenPerWoman.fillna(0)
    i.insert(57,"RankChildrenPerWoman",ChildrenPerWoman,True)
    DemocracyScore = i.loc[:,'DemocracyScore'].rank(method='max',ascending=False)
    DemocracyScore = DemocracyScore.fillna(0)
    i.insert(58,"RankDemocracyScore",DemocracyScore,True)
    Exports = i.loc[:,'Exports'].rank(method='max',ascending=False)
    Exports = Exports.fillna(0)
    i.insert(59,"RankExports",Exports,True)
    Imports = i.loc[:,'Imports'].rank(method='min',ascending=True)
    Imports = Imports.fillna(0)
    i.insert(60,"RankImports",Imports,True)
    IncomePerPerson = i.loc[:,'IncomePerPerson'].rank(method='max',ascending=False)
    IncomePerPerson = IncomePerPerson.fillna(0)
    i.insert(61,"RankIncomePerPerson",IncomePerPerson,True)
    LifeExpectancy = i.loc[:,'LifeExpectancy'].rank(method='max',ascending=False)
    LifeExpectancy = LifeExpectancy.fillna(0)
    i.insert(62,"RankLifeExpectancy",LifeExpectancy,True)
    Populationdensity = i.loc[:,'Populationdensity'].rank(method='max',ascending=False)
    Populationdensity = Populationdensity.fillna(0)
    i.insert(63,"RankPopulationdensity",Populationdensity,True)
    YearlyCO2emission = i.loc[:,'YearlyCO2emission'].rank(method='min',ascending=True)
    YearlyCO2emission = YearlyCO2emission.fillna(0)
    i.insert(64,"RankYearlyCO2emission",YearlyCO2emission,True)
    TotalRankValue = i.apply(lambda x:x['RankTotalGDPUS'] 
                                  + x['RankAgriculturalLand'] + x['RankChildrenPerWoman'] 
                                  + x['RankDemocracyScore'] + x['RankExports']
                                  + x['RankImports'] + x['RankIncomePerPerson']
                                  + x['RankLifeExpectancy'] + x['RankPopulationdensity']
                                  + x['RankYearlyCO2emission']
                                  ,axis=1)
    i.insert(65,"TotalRankValue",TotalRankValue,True)
#After ranking selected coulumns than sum up all ranked columns to totalRank
#After sum of all ranked coulumns than take average rank by yearwise
for i in Yearly_Country_wise_list:
    index = 0
    array_zeros = np.zeros(len(i))
    i.insert(66,"AverageRanking",array_zeros,True)
    for x in range(len(i)):
        #Handling missing complete column rank values
        #For average we have to divide only sum count of participated columns 
        row = i.iloc[index]
        count = row[row==0].count()
        count = 10-count+1
        totalRanking = i.loc[index,'TotalRankValue']
        if count!=0:
            averageRanking = totalRanking/count
        else:
            averageRanking = totalRanking/10
        i.loc[index,'AverageRanking'] = averageRanking
        index += 1
#We are generating csv files for our each ranked dataset yearwise
Temp = 1952
index = 0
for i in Yearly_Country_wise_list:
    Yearly_Country_wise_list[index].to_csv(f"Ranking_countries_{Temp}.csv")
    index += 1
    Temp = Temp + 4
#Below procedure to set Paremeters for plotting bar graphs 
disct_countryName_indicator = {}
indicators = ['RankTotalGDPUS','RankAgriculturalLand','RankChildrenPerWoman',
              'RankDemocracyScore','RankExports','RankImports',
             'RankIncomePerPerson','RankLifeExpectancy','RankPopulationdensity'
              ,'RankYearlyCO2emission','AverageRanking']
diction = {}
for year_wise in range(len(Yearly_Country_wise_list)):
        countries = Yearly_Country_wise_list[year_wise].Country
        index = 0
        for country in countries:
            diction[country,'RankTotalGDPUS',year_wise]=Yearly_Country_wise_list[year_wise].loc[index,'RankTotalGDPUS']
            diction[(country,'RankAgriculturalLand',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankAgriculturalLand']
            diction[(country,'RankChildrenPerWoman',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankChildrenPerWoman']
            diction[(country,'RankDemocracyScore',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankDemocracyScore']
            diction[(country,'RankExports',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankExports']
            diction[(country,'RankImports',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankImports']
            diction[(country,'RankIncomePerPerson',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankIncomePerPerson']
            diction[(country,'RankLifeExpectancy',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankLifeExpectancy']    
            diction[(country,'RankPopulationdensity',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankPopulationdensity']
            diction[(country,'RankYearlyCO2emission',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'RankYearlyCO2emission']
            diction[(country,'TotalRankValue',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'TotalRankValue']
            diction[(country,'AverageRanking',year_wise)]=Yearly_Country_wise_list[year_wise].loc[index,'AverageRanking']
            index += 1
indicators = Yearly_Country_wise_list[0].iloc[:0,55:]
indicators_list = []
for i in indicators:
    indicators_list.append(i)
year = 1952
countries = ['Pakistan','India','United States of America','China','Somalia','Bangladesh','United Kingdom','Norway']
#by using matplotlib we are plotting ranking yearwise 
for index in range(len(Yearly_Country_wise_list)):
    for indicat in indicators_list:
        Ranking = [diction[('Pakistan',indicat,index)],diction[('India',indicat,index)],
                 diction[('United States of America',indicat,index)],diction[('China',indicat,index)],
                 diction[('Somalia',indicat,index)],diction[('Bangladesh',indicat,index)],
                 diction[('United Kingdom',indicat,index)],diction[('Norway',indicat,index)]]
        if any(Ranking)==False:
            continue
        y_position = np.arange(len(countries))
        plt.figure(figsize=(14,8))
        plt.bar(y_position,Ranking,align='center',alpha=0.5)
        plt.xticks(y_position,countries)
        plt.ylabel(indicat)
        plt.title(f"{indicat} {year}")
        plt.show()
    year = year + 4

    