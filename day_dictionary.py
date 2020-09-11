import datetime 
import calendar 
  
def findDay(D):
    D_D= { 'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0,'Sat':0,'Sun':0}
    
    for keys in D:
        val=D[keys]
        name = datetime.datetime.strptime(keys, '%Y-%m-%d').weekday() 
        if ( calendar.day_name[name] == 'Monday'):
            D_D['Mon']=( D_D['Mon']+ val)
        
        elif ( calendar.day_name[name] == 'Tuesday'):
            D_D['Tue']=D_D['Tue']+ val 
        
        elif ( calendar.day_name[name] == 'Wednesday'):
            D_D['Wed']=  (D_D['Wed'] + val)
        
        elif ( calendar.day_name[name] == 'Thursday'):
            D_D['Thu']=D_D['Thu']+ val
        
        elif ( calendar.day_name[name] == 'Friday'):
            D_D['Fri']=D_D['Fri']+ val 
        
        elif ( calendar.day_name[name] == 'Saturday'):
            D_D['Sat']=D_D['Sat']+ val
        
        elif ( calendar.day_name[name] == 'Sunday'):
            D_D['Sun']=D_D['Sun']+ val    
    print(D_D)
# Driver program 
D = {'2020-01-01':6}

print(findDay(D)) 