# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 08:30:43 2016

@author: lz714
"""


import numpy 
import pandas 
import matplotlib.pyplot as plt
import os

#data = pandas.read_csv('H:/Python Scripts/test/compiled_ild_file(2509).csv', sep=',')
#total_ild=data['detector']
#testdata_frame=data.loc[:, ['date_time', 'detector', 'flow', 'occupancy']]
#testild=testdata_frame.loc[[testdata_frame['detector']=['N01/14611','N01/14612', 'N01/149d1','N01/149d2', 'N01/148u1', 'N01/148u2'], :]

#testdata_frame=testdata_frame.set_index('detector')

#detectorlist=['N01/146l1','N01/146l2', 'N01/149d1','N01/149d2', 'N01/148u1', 'N01/148u2']

#testild=testdata_frame.ix[detectorlist]

def importCSV(filename):
    '''
    import csv and then transpose
    '''
    data=pd.read_csv(os.path.join(os.getcwd(),filename), header=None)
    #df=pd.DataFrame.transpose(data)
    return data

def selectcolumn(dataframe, columnlist):
    '''
    select columns, i.e. flow, occupancy, datetime and detectorName
    '''
    return dataframe.loc[:, columnlist]

def detectorlist(dataframe, detectorindex, detectorlist):
    '''
    return dataframe of detectorlist
    '''
    dataframe.set_index(detectorindex)
    data=dataframe.ix[detectorlist]
    return data
    
def ILDperioddate(dataframe, onedetector, datetimeindex, begindate, enddate):
    '''
    Output detector with period/interval date
    '''
    onedetector=dataframe.ix[detector]
    onedetector['date_time_reindex']=pandas.to_datetime(onedetector[datetimeindex])
    onedetector=onedetector.drop([datetimeindex], axis=1)
    perioddatedata=onedetector.set_index('date_time_reindex')[begindate:enddate]
    return perioddatedata


def ILDperiodtime(dataframe, onedetector, datetimeindex, begintime, endtime, begindate, enddate):
    '''
    Output detector with period/interval time every day
    '''
    onedetector=dataframe.ix[detector]
    onedetector['date_time_reindex']=pandas.to_datetime(onedetector[datetimeindex])
    onedetector=onedetector.drop([datetimeindex], axis=1)
    periodtimedata=onedetector.set_index('date_time_reindex').between_time(begintime, endtime)
    return periodtimedata
    

def ILDfixedtime(dataframe, onedetector, datetimeindex, fixedtime):
    '''
    Output detector with fixed time every day
    '''
    onedetector=dataframe.ix[detector]
    onedetector['date_time_reindex']=pandas.to_datetime(onedetector[datetimeindex])
    onedetector=onedetector.drop([datetimeindex], axis=1)
    data=onedetector.set_index('date_time_reindex')
    locs=data.index.indexer_at_time(fixedtime)
    fixedtimedata=data.iloc[locs]
    
    return fixedtimedata
    


def missingdata(dataframe):
    return dataframe.interpolate(method='index')
    
    
def calculateFlow(dataframe, detector):
    '''
    output the sum of flow
    '''
    dataframelist=importlist()
    #find the same detector name
    
    
    
    return flow
def calculateOccupancy():
    '''
    output the average of occuapancy
    '''
    return occupancy

    

def saveDataframetoCSV():
    return csvfile

    
    
    
def occupancydata(dataframes):
    return 
    
    
if __name__=='__main__':
    #global variable
    filename='compiled_ild_file(2509).csv'
    columnlist= ['date_time', 'detector', 'flow', 'occupancy']
    detectorindex='detector'
    detectorlist=['N01/146l1','N01/146l2', 'N01/149d1','N01/149d2', 'N01/148u1', 'N01/148u2']
    onedetector='N01/146l1'
    datetimeindex='date_time'
    begintime='7:00:00'
    endtime='21:00:00'
    begindate='2015-02-16'
    enddate='2015-02-26'
    fixedtime='7:00:00'
    
    
    
        
        
    
    ild146_1=testild.ix['N01/146l1']
    ild146_1['date_time1']=pandas.to_datetime(ild146_1['date_time'])
    ild146_1 = ild146_1.drop(['date_time'], axis=1)
    period146_1=ild146_1.set_index('date_time1')['2015-02-16':'2015-02-20']
    
    
    
    ild146_2=testild.ix['N01/146l2']
    
    ild149_1=testild.ix['N01/149d1']
    ild149_2=testild.ix['N01/149d2']
    
    ild148_1=testild.ix['N01/148u1']
    ild148_2=testild.ix['N01/148u2']
    
    selectdata['date_time']=pandas.to_datetime(selectdata['date_time'])
    
     set_index('date_time')['2015-02-16':'2015-02-20']
    locs = selectdata.index.indexer_at_time('7:00:00':'21:00:00')
    #aframe.iloc[locs]
    
    perioddata=selectdata.between_time('7:00:00','21:00:00')
    
    
    ild146=[]
    ild148=[]
    ild149=[]
    
    ild146['detector']='N01/146'
    ild148['detector']='N01/148'
    ild148['detector']='N01/149'
    
    
    ild146['occupancy']=(ild146_1['occupancy']+ild146_2['occupancy'])/2
    ild148['occupancy']=(ild148_1['occupancy']+ild148_2['occupancy'])/2
    ild149['occupancy']=(ild149_1['occupancy']+ild149_1['occupancy'])/2
    
    ild146['flow']=ild146_1['flow']+ild146_2['flow']
    ild148['flow']=ild148_1['flow']+ild148_2['flow']
    ild149['flow']=ild149_1['flow']+ild149_2['flow']
    
    ild146['date_time']=ild146_1['data_time']+ild146_2['flow']
    ild148['flow']=ild148_1['flow']+ild148_2['flow']
    ild149['flow']=ild149_1['flow']+ild149_2['flow']

