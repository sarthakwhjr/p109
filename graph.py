import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics

df=pd.read_csv("data.csv")
height=df["Height(Inches)"].to_list()
weight=df["Weight(Pounds)"].to_list()
heightmean=statistics.mean(height)
weightmean=statistics.mean(weight)
heightmedian=statistics.median(height)
weightmedian=statistics.median(weight)
heightmode=statistics.mode(height)
weightmode=statistics.mode(weight)
heightstdev=statistics.stdev(height)
weightstdev=statistics.stdev(weight)
print("mean,median,mode of the height is {}, {} and {} respectively".format(heightmean,heightmedian,heightmode))
print("mean,median,mode of the wieght is {}, {} and {} respectively".format(weightmean,weightmedian,weightmode))
height1stdevstart,height1stdevend=heightmean-heightstdev,heightstdev+heightmean
height2stdevstart,height2stdevend=heightmean-(2*heightstdev),(2*heightstdev)+heightmean
height3stdevstart,height3stdevend=heightmean-(3*heightstdev),(3*heightstdev)+heightmean
weight1stdevstart,weight1stdevend=weightmean-weightstdev,weightstdev+weightmean
weight2stdevstart,weight2stdevend=weightmean-(2*weightstdev),(2*weightstdev)+weightmean
weight3stdevstart,weight3stdevend=weightmean-(3*weightstdev),(3*weightstdev)+weightmean

heightlist1stdev=[results for results in height if results >height1stdevstart and results<height1stdevend]
heightlist2stdev=[results for results in height if results >height2stdevstart and results<height2stdevend]
heightlist3stdev=[results for results in height if results >height3stdevstart and results<height3stdevend]
weightlist1stdev=[results for results in weight if results >weight1stdevstart and results<weight1stdevend]
weightlist2stdev=[results for results in weight if results >weight2stdevstart and results<weight2stdevend]
weightlist3stdev=[results for results in weight if results >weight3stdevstart and results<weight3stdevend]

print("{}% of data for height in first stdev".format(len(heightlist1stdev)*100/len(height)))
print("{}% of data for height in first stdev".format(len(heightlist2stdev)*100/len(height)))
print("{}% of data for height in first stdev".format(len(heightlist3stdev)*100/len(height)))
print("{}% of data for weight in first stdev".format(len(weightlist1stdev)*100/len(weight)))
print("{}% of data for weight in first stdev".format(len(weightlist2stdev)*100/len(weight)))
print("{}% of data for weight in first stdev".format(len(weightlist3stdev)*100/len(weight)))


graph=pff.create_distplot([heightlist1stdev],["heightlist1stdev"],show_hist=False)
graph.show()