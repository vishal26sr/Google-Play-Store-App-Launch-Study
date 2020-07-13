import tkinter as tk
from tkinter import *
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fractions import Fraction
from tkinter import Listbox
import tkinter
import matplotlib
from tkinter import messagebox
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from PIL import ImageTk,Image
from sklearn.linear_model import LinearRegression
import pymysql
from textblob import TextBlob
import re

data=pd.read_csv("googleplaystore-App-data.csv")#DataFrames is two-dimensional(2-D) data structure defined in pandas which consists of rows and columns.
data["Is"]=list(data.Installs)
data["Installs"] = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in data["Installs"] ]
data1=pd.read_csv("googleplaystore_user_reviews.csv")


         

def point_1():
    
    cat_array=data.Category.unique()
    cat_list=list(data.Category)    
    total_installs=0.0
    for i in data.Installs:
        total_installs=total_installs+i
    cat_installs={}
    for i in cat_array:
        sum=0.0
        for j in range(len(cat_list)):
            if i==cat_list[j]:
                sum=sum+data.Installs[j]
        percentage=(sum/total_installs)*100        
        cat_installs.update({i:float("{:.2f}".format(percentage))})
    plt.figure(figsize=(14,8))
#    plt.figure()
#fm = plt.get_current_fig_manager()
#fm.canvas.figure = fig1
#fig1.canvas = fm.canvas
    
    
    percent_installs = plt.bar(range(len(cat_installs)), list(cat_installs.values()),color=['yellow','blue','black','orange','pink'])
    plt.xticks(range(len(cat_installs)), list(cat_installs.keys()),rotation='vertical')
    plt.xlabel('Category',fontsize=15)
    plt.ylabel('%age of Downloads',fontsize=15)
    plt.tight_layout()
    plt.new_figure_manager
    for bar in percent_installs:
        yval = bar.get_height()
        plt.text(bar.get_x() - .2, yval + .1, str(yval)+"%",fontsize=8)
def point_2():
    
    plt.figure(figsize=(14,8))
#    j=fig1.add_subplot(111)
    
    a,b,c,d,e=0,0,0,0,0
    for i in data['Installs']:
        
        if 10000<=i<50000 :
            a=a+1
        elif 50000<=i<150000 :
            b=b+1
        elif 150000<= i <500000:
            c=c+1
        elif 500000<=i<5000000 :
            d=d+1
        else:
            e=e+1
    dic_data={"10000-50000":a,"50000-150000":b,"150000-500000":c,"500000-5000000":d,"5000000+":e}
    graph=plt.bar(dic_data.keys(),dic_data.values(),color=['yellow','blue','black','orange','pink'])
    plt.xlabel("Range")
    plt.ylabel("No.of Installs")
    plt.tight_layout()
    for bar in graph:
        yval = bar.get_height()
        plt.text(bar.get_x() + .3, yval + .1, str(yval),fontsize=16)

def point_3():

    screen_3=Tk()
    screen_3.title(" Category of apps have managed to get the most and  least downloads. ")
    adjustwindow(screen_3)
    Categorys=data.Category.unique()
    category_column=list(data.Category)
    category_installs={}
    for i in Categorys:
    
        sum=0.0
        for j in range(len(category_column)):
            if i==category_column[j]:
                sum=sum+data.Installs[j]
        category_installs.update({i:sum})
    
#    print(category_installs)
    fig=Figure(figsize=(10,6))
    a=fig.add_subplot(211)
    #a.set_xlabel("Category")
    a.set_ylabel("No.of Installs")
    for tick in a.get_xticklabels():
        tick.set_rotation(90)
    a.bar(category_installs.keys(),category_installs.values(),color='yellow')
    canvas = FigureCanvasTkAgg(fig, master=screen_3)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    df = pd.DataFrame(data=category_installs, index=[0])
    
    df = (df.T)
    
#    print (df)
#    df.to_excel('dict1.xlsx')
    
    data2=pd.read_excel("dict1.xlsx", sep='\t', header=None)
    data2.columns = ["Category","Installs"]
    def Complete():
        screen_31=Tk()
        adjustwindow(screen_31)
        screen_31.configure(background='#ffe2a4')
        txt1=data2.Category
        txt2=data2.Installs
        Label(screen_31,text=txt1,font=("Open Sans",10,'bold'),bg='#ffe2a4').place(x=150,y=0)
        Label(screen_31,text=txt2,font=("Open Sans",10,'bold'),bg='#ffe2a4').place(x=550,y=0)
    #pd.to_numeric(data1("Installs"))
#    print(data1)
    in_list=[]
    in_list = list(map(float,data2.Installs))
    
    for j in range(len(data2.Category)):
        if data2.Installs[j]==max(data2.Installs):
            txt=str("MOST DOWNLOAD :"+data2.Category[j]) 
            Label(screen_3,text=txt,font=("Open Sans",20,'bold'),bg="white").pack()
    #data1.drop(['nan'])
    for j in range(len(data2.Category)):
        if (data2.Installs[j]==min(data2.Installs)):
            txt=str("LEAST DOWNLOAD :"+data2.Category[j]) 
            Label(screen_3,text=txt,font=("Open Sans",20),bg="white").pack()
    Button(screen_3,text="Installs of Each Category ",bg="#66dda5",width=40,height=1,font=("Open Sans",13,'bold'),fg="white",command=Complete).pack()
def point_4():
#    screen_4=Tk()
#    adjustwindow(screen_4)
    plt.figure(figsize=(14,8))
#    a=fig.add_subplot(211)
   
    cat_array=data.Category.unique()
    cat_list=list(data.Category)
    avg_rats={}
    for i in cat_array:
        sum=0.0
        count=0.0
        for j in range(len(cat_list)):
            if i==cat_list[j] and data.Rating[j]==data.Rating[j]:
                sum=sum+data.Rating[j]
                count+=1.0
        avg=sum/count        
        avg_rats.update({i:float("{:.2f}".format(avg))})
    
    g=plt.bar(avg_rats.keys(), avg_rats.values())
    plt.xticks(rotation=90)
    plt.xlabel('Category',fontsize=15)
    plt.ylabel('Average Rating',fontsize=15)
    plt.tight_layout()
    for bar in g:
        yval = bar.get_height()
        plt.text(bar.get_x() + .1, yval + .0, str(yval),fontsize=10)
#    m1=max(avg_rats.values())
#    
#    for i in avg_rats.items():
#        if i[1]==m1:
#            txt="Category with highest average Ratings is "+i[0]
#            Label(screen_4,text=txt,font=("Open Sans",20,'bold'),bg="white").pack()#add all vallue
#        
#            
#    canvas = FigureCanvasTkAgg(fig,master=screen_4)
#    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def point_6():
    global screen_6
    screen_6=Tk()
    screen_6.title("For the years 2016,2017,2018 what are the category of apps that have got the most and  the least downloads. What is the percentage increase or decrease that the apps have got over the period of three years. d")
    adjustwindow(screen_6)
    category_installs1={}
    category_installs2={}
    category_installs3={}
    
    sum6=0.0
    sum7=0.0
    sum8=0.0
    sumo=0.0
    Categorys=data.Category.unique()
    for category in Categorys:
        
        cat=data.loc[data['Category']==category]#loc function is used for returning rows
        
        cat=cat.sort_values('Last Updated')
        #installs = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in cat["Installs"] ]
        ins = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in cat["Is"] ]
        #cat_install=cat["Ins"]
        #print(ins)
        dates=list(cat['Last Updated'])
        dates=[i.replace(',', '') if ',' in i else float(0) for i in cat["Last Updated"] ]
    
        list_sum=[]
        
    
        for year in ['2016','2017','2018']:
                sum=0.0
                for i in range(len(dates)):
                    j=dates[i].split()
                    if(j[2]==year):
                        sum=sum+ins[i]
                
                    
                list_sum.append(sum)
        category_installs1.update({category:list_sum[0]})
        category_installs2.update({category:list_sum[1]})
        category_installs3.update({category:list_sum[2]})
        sum6=sum6+list_sum[0]
        sum7=sum7+list_sum[1]
        sum8=sum8+list_sum[2]
        sumo=sumo+list_sum[0]+list_sum[1]+list_sum[2]
    
    fig=Figure(figsize=(18,7))
    fig.tight_layout()
    k=fig.add_subplot(331)
    l=fig.add_subplot(332)
    m=fig.add_subplot(333)
    k.bar(category_installs1.keys(),category_installs1.values(),color='yellow')
    k.set_xlabel("Category")
    k.set_ylabel("No.of Installs in 2016")
    for tick in k.get_xticklabels():
        tick.set_rotation(90)
#    plt.xticks(rotation=90)
#    plt.show()
    inverse=[(value,key) for key, value in category_installs1.items()]
    
    l.bar(category_installs2.keys(),category_installs2.values(),color='Red')
    l.set_xlabel("Category")
    l.set_ylabel("No.of Installs in 2017")
    for tick in l.get_xticklabels():
        tick.set_rotation(90)
#    plt.xticks(rotation=90)
#    plt.show()
    invers=[(value,key) for key, value in category_installs2.items()]
   
    m.bar(category_installs3.keys(),category_installs3.values(),color='Green')
    m.set_xlabel("Category")
    m.set_ylabel("No.of Installs in 2018")
    for tick in m.get_xticklabels():
        tick.set_rotation(90)
#    plt.xticks(rotation=90)
#    plt.show()
    
    canvas = FigureCanvasTkAgg(fig,master=screen_6)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.draw()
    inver=[(value,key) for key, value in category_installs3.items()]
    
    diff67=sum7-sum6
    per67=(diff67/sumo)*100
    
    diff78=sum8-sum7
    per78=float((diff78/sumo)*100)
    if per67>0:
        txt="Increase by percent of Installs of apps from year 2016 to 2017 is ",per67
    else:
        txt="Decrease by percent of Installs of apps from year 2016 to 2017 is",per67
    if per78>0:
        txt1="\nIncrease by percent of Installs of apps from year 2017 to 2018 is",per78
    else:
        txt1="\n Decrease by percent of Installs of apps from year 2017 to 2018 is",per78
    txt2=txt+txt1
    ans=str("Highest no.of Installs in year 2016 is "+max(inverse)[1]+" with total no.of Installs being  "+str(max(inverse)[0])+" Lowest no.of installs in 2016 is "+min(inverse)[1]+" with total no.of Installs being "+str(min(inverse)[0])+" \n Highest no.of Installs in year 2017 is "+max(invers)[1]+" with total no.of Installs being "+str(max(invers)[0])+" Lowest no.of installs in 2017 is "+min(invers)[1]+" with total no.of Installs being "+ str(min(invers)[0])+"\n Highest no.of Installs in year 2018 is "+max(inver)[1]+" with total no.of Installs being"+str(max(inver)[0])+" Lowest no.of installs in 2018 is "+min(inver)[1])+" with total no.of Installs being "+str(min(inver)[0])
    Label(screen_6,text=ans,font=("Open Sans",10),bg="white").pack()
    Label(screen_6,text=txt2,font=("Open Sans",10,'bold'),bg="white").place(x=0,y=0)
    #Label(screen_6,text=txt2,font=("Open Sans",10,'bold'),bg="white").pack(x=0,y=5)

    
def point_7():
    screen_7=Tk()
    screen_7.title(" apps whose version not an issue percentage increase or decrease in the downloads. ")
    adjustwindow(screen_7)
    
    Label(screen_7,text="Change in Percentage",width=30,height=3,bg="white",font=("Open Sans", 12, 'bold')).place(x=20,y=50)
        
    Andriod_version=data.loc[data['Android Ver']!='Varies with device']#loc function is used for returning rows
    #print(Andriod_version)
    last_Updated=[i.replace(',', '') if ',' in i else float(0) for i in Andriod_version["Last Updated"]] 
    last_updated=list(last_Updated)
    installs =list( Andriod_version["Installs"]) 
    #installs=list(Andriod_version['Installs'])
    #print(Andriod_version['installs'])
    last_updated1=[]
    for i in last_updated:
        j=i.split()
        last_updated1.append(j[2])
    #print(last_updated1)
    total_install=0.0
    for i in installs:
        total_install=total_install+i
        
    dic_trend={}
    years=['2011','2012','2013','2014','2015','2016','2017','2018']
    for year in years:
        sum=0.0
        for i in range(len(last_updated1)):
            if last_updated1[i]==year:
                sum=sum+installs[i]
        dic_trend.update({year:sum})
    
           
    #print(sum)
    #print(dic_trend)
    def graph():
        fig=plt.Figure(figsize=(6,6),dpi=80)
        a=fig.add_subplot(111)
        x=dic_trend.keys()
        y=dic_trend.values()
        a.bar(x,y)
        a.set_xlabel("years")
        a.set_ylabel("Downloads")
        canvas = FigureCanvasTkAgg(fig, master=screen_7)
        canvas.get_tk_widget().place(x=400,y=100)
        
    
    def percentage(x1,x2):
        return((x2-x1)/total_install *100)
        
    y=100
    for year in dic_trend:
        if year=='2018':
            break
        else:
            percent=percentage(dic_trend[year],dic_trend[str(int(year)+1)])
            txt=str(year+" to "+str(int(year)+1)+ "  :  "+str(percent)+"%")
            Label(screen_7,text=txt,bg="white",width=30,height=2).place(x=50,y=y)
            y=y+40
    Button(screen_7,text="Graph",width=20,height=2,bg="#80ff00",command=graph).place(x=400,y=30)


    
def point_9():
    global screen_9
    screen_9=Tk()
    adjustwindow(screen_9)
    data3=pd.read_csv("googleplaystore-App-data.csv")
    data3["Installs"] = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in data3["Installs"] ]
    data3=data3[np.isfinite(data3['Rating'])]
    data3=data3[np.isfinite(data3['Installs'])]
    x=data3['Rating'].values.reshape(-1,1)
    y=data3['Installs'].values.reshape(-1,1)
    reg=LinearRegression()
    reg.fit(x,y)
    predictions=reg.predict(x)
    fig=Figure(figsize=(8,5))
    a=fig.add_subplot(111)
    a.scatter(data3['Rating'],data3['Installs'],c='yellow')
    a.plot(data3['Rating'],predictions,c='red',linewidth=2)
    a.set_xlabel("Rating")
    a.set_ylabel("Installs")
    canvas = FigureCanvasTkAgg(fig,master=screen_9)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    count=0
    sum1=0
    data_list=list(data.Rating)
    for i in range(len(data_list)):
        if(data.Installs[i]>99999 and data.Rating[i]==data.Rating[i]):
            count=count+1
            sum1=sum1+data.Rating[i]
    avg=sum1/count
    tex=str("The average rating of app whose Install is greater than 1,00,000 is "+str(avg))
    Label(screen_9,text=tex,bg="#663399",font=("Open Sans",13,'bold'),fg="white").pack()
    conclu="The Graph is Slightly lifted as the rating is Increased afer 4.1 hence there is a certain relation between Installs and Rating"
    Label(screen_9,text=conclu,bg="#663399",font=("Open Sans",13,'bold'),fg="white").pack()
#    
#    fig = plt.figure(figsize=(10,8))
#   
#    plt.scatter(data['Rating'],data["Installs"],c='purple')
#    plt.xlabel("Ratings",fontsize=12)
#    plt.ylabel("Downloads",fontsize=12)
    

def point_10():
    os.system('python test1.py')

def point_11():
    last_Updated=[i.replace(',', '') if ',' in i else float(0) for i in data["Last Updated"]] 
    last_updated=list(last_Updated)
    installs =list( data["Installs"])
    last_updated1=[]
    last_updated2=[]
    for i in last_updated:
        j=i.split()
        last_updated1.append(j[2])
        last_updated2.append(j[0])
    
    #print(last_updated2)
    months1=['January','February','March']
    months2=['April','May','June']
    months3=['July','August','September']
    months4=['October','November','December']
    
    dic_trend={}
    
    years=['2011','2012','2013','2014','2015','2016','2017','2018']
    for year in years:
        sum=0.0
        sum1=0.0
        sum2=0.0
        sum3=0.0
        for i in range(len(last_updated1)):
            if last_updated1[i]==year and (last_updated2[i]==months1[0] or last_updated2[i]==months1[1] or last_updated2[i]==months1[2]  ):
                sum=sum+installs[i]
            if last_updated1[i]==year and (last_updated2[i]==months2[0] or last_updated2[i]==months2[1] or last_updated2[i]==months2[2]  ):
                sum1=sum1+installs[i]
            if last_updated1[i]==year and (last_updated2[i]==months3[0] or last_updated2[i]==months3[1] or last_updated2[i]==months3[2]  ):
                sum2=sum2+installs[i]
            if last_updated1[i]==year and (last_updated2[i]==months4[0] or last_updated2[i]==months4[1] or last_updated2[i]==months4[2]  ):
                sum3=sum3+installs[i]
        dic_trend.update({"Quater 1 of year "+year:sum,"Quater 2 of year "+year:sum1,"Quater 3 of year "+year:sum2,"Quater 4 of year "+year:sum3})
        
    #print(sum)
    plt.figure(figsize=(14,8))
    quater_installs=plt.bar(dic_trend.keys(),dic_trend.values())
    plt.xlabel("Quater of each year")
    plt.ylabel("No.of Installs")
    plt.xticks(rotation=90)
    plt.tight_layout()
#    for bar in quater_installs:
#        yval = bar.get_height()
#        plt.text(bar.get_x() - .5, yval - .0, str(yval),fontsize=9)
    
def point_12():
    global screen_12
    screen_12=Tk()
    screen_12.title("Most Positive and negative Sentiment")
    adjustwindow(screen_12)
    
    apps=data1.App.unique()
    app_column=list(data1.App)

    app_sentiment1={}
    app_sentiment2={}
    app_sentiment3={}
    d=[]
#    diff={}

    data1['Sentiment'].dropna()
    for i in apps:
        a,b,c=0,0,0
        count=0
        for j in range(len(app_column)):
#            count=count+1        
            if i==app_column[j]:
                if(data1.Sentiment[j]=='Positive'):
                    a=a+1
                elif(data1.Sentiment[j]=='Negative'):
                        b=b+1
                else:
                    c=c+1
        e=a-b
        if(e==0):
            d.append(i)

        app_sentiment1.update({i:a})
        app_sentiment2.update({i:b})
#        app_sentiment3.update({i:c})
    no_emoji=[]
    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF""]+", flags=re.UNICODE)
    for i in d:
        emoji_pattern.sub(r'',i)
        no_emoji.append(emoji_pattern.sub(r'',i))
    
        
    inverse=[(value,key) for key, value in app_sentiment1.items()]
    inver1=[(value,key) for key, value in app_sentiment2.items()]
    txt1="App with most positive reviews is "+max(inverse)[1]
    txt2="App with most negative reviews is "+max(inver1)[1]
    Label(screen_12,text=txt1,bg="cyan",fg="red").place(x=0,y=0)
    Label(screen_12,text=txt2,bg="cyan",fg="red").place(x=0,y=40)
    Label(screen_12,text="Apps with almost equal positive and negative review",bg="cyan",fg="red").place(x=0,y=80)
    
    listbox=Listbox(screen_12,height=12,width=50)
    scrool=Scrollbar(screen_12,orient="vertical")
    scrool.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.place(x=400,y=80)
    scrool.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrool.set)
    for i in d:
#        d.insert(tk.END,*no_emoji)
        listbox.insert(tk.END,*no_emoji)
        listbox.insert(tk.END, i)
        
    
    
    

#    diff = {key: app_sentiment1[key] - app_sentiment2.get(key, 0) for key in app_sentiment1.keys()}
#    
#    min_val = None
#    result = None
#    for k, v in diff.items():
#        if v and (min_val is None or v < min_val):
#            min_val = v
#            result = k
#    
#   
#    
#    
#    q=Label(screen_12,text="App with approx equal ratio of +ve and -ve reviews are",bg="cyan",fg="red")
#    q.place(x=0,y=80)
#    p=Label(screen_12,text=result,bg="cyan",fg="red")
#    p.place(x=290,y=80)#place(x=30,y=69)
#    Button(screen_12,text="Apps as per downloads",bg="#66dda5",width=83,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=200,y=200)


    
def point_13():
    global screen_13
    screen_13=Tk()
    adjustwindow(screen_13)
    newdata1=pd.read_csv("googleplaystore_user_reviews.csv")
    newdata1=newdata1[np.isfinite(newdata1['Sentiment_Polarity'])]
    newdata1=newdata1[np.isfinite(newdata1['Sentiment_Subjectivity'])]
    x=newdata1['Sentiment_Polarity'].values.reshape(-1,1)
    y=newdata1['Sentiment_Subjectivity'].values.reshape(-1,1)
    reg=LinearRegression()
    reg.fit(x,y)
    predictions=reg.predict(x)
    fig=Figure(figsize=(8,5))
    a=fig.add_subplot(111)
    a.scatter(newdata1['Sentiment_Polarity'],newdata1['Sentiment_Subjectivity'],c='yellow')
    a.plot(newdata1['Sentiment_Polarity'],predictions,c='red',linewidth=2)
    a.set_xlabel("sentiment polarity")
    a.set_ylabel("sentiment subjectivity")
    canvas = FigureCanvasTkAgg(fig,master=screen_13)
    canvas.get_tk_widget().pack()
    canvas.draw()
    TXt="If Slope is Positve there is a postive relation \n if Slope is Negative there is negative relation else no relation"
    Label(screen_13,text=TXt,bg="#663399",font=("Open Sans",13,'bold'),fg="white").pack()
    #plt.show()
def point_15():
    global screen_15
    screen_15=Tk()
    adjustwindow(screen_15)
#    cat_array=data.App.unique()
    
    app_study=data1.loc[data1['App']=='10 Best Foods for You']
    app_data=data.loc[data['App']=='10 Best Foods for You']
    Label(screen_15,text="App Info",bg="Red",font=("Open Sans",13,'bold'),fg="white").place(x=10,y=0)
#    appdata=app_data.App.unique()
    appname=list(app_data['App'])
    b1=list(app_data['Rating'])
    c1=list(app_data['Reviews'])
    d1=list(app_data['Size'])
    e1=list(app_data['Installs'])
    f1=list(app_data['Type'])
    g1=list(app_data['Category'])
    h1=list(app_data['Content Rating'])
    j1=list(app_data['Genres'])
    k1=list(app_data['Current Ver'])
    l1=list(app_data['Android Ver'])
#    n1=list(app_data['Rating'])
    i=0
    a=app_data['Android Ver']
    Label(screen_15,text="App Name-:",font=("Open Sans",13,'bold'),fg="Black").place(x=10,y=30)
    Label(screen_15,text=appname[0],font=("Open Sans",13,'bold'),fg="Black").place(x=140,y=30)
    Label(screen_15,text="Rating-:",font=("Open Sans",13,'bold'),fg="Black").place(x=10,y=60)
    Label(screen_15,text=b1[0],font=("Open Sans",13,'bold'),fg="Black").place(x=140,y=60)
    Label(screen_15,text="Reviews Given-:",font=("Open Sans",13,'bold'),fg="Black").place(x=10,y=90)
    Label(screen_15,text=c1[0],font=("Open Sans",13,'bold'),fg="Black").place(x=140,y=90)
    Label(screen_15,text="Size-:",font=("Open Sans",13,'bold'),fg="Black").place(x=10,y=120)
    Label(screen_15,text=d1[0],bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=140,y=120)
    Label(screen_15,text="Installs-:",bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=10,y=150)
    Label(screen_15,text=e1[0],bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=140,y=150)
    Label(screen_15,text="Type-:",bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=10,y=180)
    Label(screen_15,text=f1[0],bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=140,y=180)
    Label(screen_15,text="Category-:",bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=500,y=30)
    Label(screen_15,text=g1[0],bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=640,y=30)
    Label(screen_15,text="Content Rating-:",bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=500,y=60)
    Label(screen_15,text=h1[0],bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=640,y=60)
    Label(screen_15,text="Genres-:",bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=500,y=90)
    Label(screen_15,text=j1[0],bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=640,y=90)
    Label(screen_15,text="Current Version-:",bg="white",font=("Open Sans",13,'bold'),fg="Black").place(x=500,y=120)
    Label(screen_15,text=k1[0],font=("Open Sans",13,'bold'),fg="Black").place(x=640,y=120)
    Label(screen_15,text="Android Version-:",font=("Open Sans",13,'bold'),fg="Black").place(x=500,y=150)
    Label(screen_15,text=l1[0],font=("Open Sans",13,'bold'),fg="Black").place(x=640,y=150)
    #print(app_study['Sentiment'])
    app_sentiment1={}
    app_sentiment2={}
    app_sentiment3={}
    
    diff={}
    a,b,c=0,0,0
    count=0
    
    for i in app_study['Sentiment']:
        
        
                
        
        if(i=='Positive'):
            a=a+1
        elif(i=='Negative'):
            b=b+1
        elif(i=='Neutral'):
            c=c+1
    d=a+b+c
    per_pos=(a/d)*100
    per_neg=(b/d)*100
    Label(screen_15,text="App review analysis",bg="Red",font=("Open Sans",13,'bold'),fg="white").place(x=10,y=250)
    posi="Of the "+str(d)+" review given "+str(per_pos)+"% people have given positive review "
    negi="Of the "+str(d)+" review given" +str(per_neg)+"% people have given Negative review "
    con="Since "+str(per_pos)+"% has given positive review and only "+str(per_neg)+"% has given negative review hence it is mostly positive "
    con1="and most of the people are satisfied with the app therfore it is advisible to use 10 Best Food app for you or app like that"
#    print("Of the {} review given {}% people have given positive review ".format(d,per_pos))
#    print("Of the {} review given {}% people have given Negative review ".format(d,per_neg))
#    print("Since {}% has given positive review and only {}% has given negative review hence it is mostly positive hence most of the people are happy with the app hence it is advisible to use 10 Best Food app for you".format(per_pos,per_neg))
    Label(screen_15,text=posi,bg="#663399",font=("Open Sans",13,'bold'),fg="white").place(x=10,y=290)
    Label(screen_15,text=negi,bg="#663399",font=("Open Sans",13,'bold'),fg="white").place(x=10,y=330)
    Label(screen_15,text=con,bg="#663399",font=("Open Sans",13,'bold'),fg="white").place(x=10,y=370)
    Label(screen_15,text=con1,bg="#663399",font=("Open Sans",13,'bold'),fg="white").place(x=10,y=390)
#if wanted calculate the height 
def point_16():
    global screen_16
    screen_16=Tk()
    screen_16.title(" month(s) of the year , is the best indicator to the avarage downloads that an app will generate over the entire year")
    adjustwindow(screen_16)
    dates=[i.replace(',', '') if ',' in i else float(0) for i in data["Last Updated"] ]
    #print(dates)
    #data["Installs"] = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in data["Installs"] ]
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    mon=[]
    for date in dates:
        j=date.split()
        mon.append(j[0])
    dic={}    
    for month in months:
        sum=0.0
        for i in range(len(mon)):
            if(month==mon[i]):
                sum=sum+data["Installs"][i]
        dic.update({month:sum})  
    fig=Figure(figsize=(12,8)) 
    a=fig.add_subplot(111)
    x=months
    y=dic.values()
    a.bar(x,y)
    for tick in a.get_xticklabels():
        tick.set_rotation(90)
    canvas = FigureCanvasTkAgg(fig,master=screen_16)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def point_17():
    Andriod_version=data.loc[data['Size']!='Varies with device']
#    Andriod_version["Installs"] = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in Andriod_version["Installs"] ]
    #Andriod_version["Size"]=[ i.replace('M','')  for i in Andriod_version["Size"] ]
    #print(Andriod_version["Size"])
    size=[]
    size1=[]
    for i in Andriod_version["Size"]:
        if "M" in i:
            
            a=float(i.replace('M',''))
            #a=a*1000
            s1=[a]
            size.append(s1)
            size1.append(a)
        if "k" in i:
            a=float(i.replace('k',''))
            a=a/1000
            s1=[a]
            
            size.append(s1)
            size1.append(a)
    #print(size)
    #plt.scatter(size,Andriod_version["Installs"])
    #for i in range(len(size)):
    #    size[i]=Andriod_version.Size[i]
            
    #print(Andriod_version["Size"])    
    x=size
    
    y=Andriod_version['Installs'].values.reshape(-1,1)
    
    reg=LinearRegression()
    reg.fit(x,y)
    predictions=reg.predict(x)
    plt.figure(figsize=(14,8))
    plt.scatter(size1,Andriod_version['Installs'],c='yellow')
    plt.plot(size1,predictions,c='red',linewidth=2)
    plt.xlabel("Size in Mb")
    plt.ylabel("Installs")
    plt.show()

def adjustwindow(window):
    
    w=1100
    h=700
    ws=window.winfo_screenwidth()
    hs=window.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    window.geometry('%dx%d+%d+%d'%(w,h,x,y))
    window.resizable(False,False)
    window.configure(background='white')
def adjustWindow(window):
    
    w=1000
    h=800
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    window.geometry('%dx%d+%d+%d'%(w,h,x,y))
#    window.resizable(False,False)
    window.configure(background='white')
   
    
#def submit2():
#        app_det = TextBlob(inputValue)
##    print(app_det.polarity)
#        app_pol=app_det.polarity
#        app_sub=app_det.subjectivity
#        if(app_det.polarity > 0):
#            sent="Positive"
#        else:
#            sent="Negative"
#    
#        connection = pymysql.connect(host="localhost", user="root", passwd="", database="app_data") # database connection 
#        cursor = connection.cursor() 
#        insert_query = "INSERT INTO app_review(app,review, sentiment, sentiment_polarity,sentiment_subjectivity) VALUES('"+ aname1.get() + "', '"+ str(inputValue) + "', '"+ str(sent) + "', '"+ str(app_pol) + "','"+ str(app_sub) +  "');" # queries for inserting values 
#        cursor.execute(insert_query) # executing the queries 
#        connection.commit() # commiting the connection then closing it. 
#        connection.close() # closing the connection of the database 
#        Label(sub2, text="Data Entered in review Dataset", fg="green", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=600, y=750)

    
def reg2():
 
    sp=Tk()#initializing the tkinter window
    sp.title("Welcome")
    adjustWindow(sp)#configuring the window
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    def retrieve_input():
        global inputValue,inp1
        inputValue=textBox.get("1.0","end-1c")
        inp1=aname1.get("1.0","end-1c")
        submit2()
        
    def submit2():
        
        app_det = TextBlob(inputValue)
        #    print(app_det.polarity)
        app_pol=app_det.polarity
        app_sub=app_det.subjectivity
        if(app_det.polarity > 0):
            sent="Positive"
        else:
            sent="Negative"
        
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="app_data") # database connection 
        cursor = connection.cursor() 
        insert_query = "INSERT INTO app_review(app,review, sentiment, sentiment_polarity,sentiment_subjectivity) VALUES('"+ str(inp1) + "', '"+ str(inputValue) + "', '"+ str(sent) + "', '"+ str(app_pol) + "','"+ str(app_sub) +  "');" # queries for inserting values 
        cursor.execute(insert_query) # executing the queries 
        connection.commit() # commiting the connection then closing it. 
        connection.close() # closing the connection of the database 
        Label(sp, text="Data Entered in review Dataset", fg="green", font=("calibri", 20), width='27',height='5', bg='white').place(x=250, y=400)
    

    global aname1
    aname1=StringVar()
    Label(sp,text="User Review Data Entry",width="27",height="1",font=("Calibri",25,'bold'),fg='white',bg='#174873').pack()
    Label(sp,text="App Name",font={"Open Sans",10,'bold'},bg='#174873',fg='white').place(x=270,y=100)
    Label(sp,text="*",font={"Open Sans",10,'bold'},bg='white',fg='red').place(x=600,y=100)
#    Entry(tab2, textvar=aname1,width='20').place(x=475,y=100)
    aname1=Text(sp, height=1, width=30)
    aname1.place(x=475,y=100)
    Label(sp,text="App Review",font={"Open Sans",10,'bold'},bg='#174873',fg='white').place(x=270,y=200)
    #    Label(screen1,text="*",font={"Open Sans",10,'bold'},bg='white',fg='red').place(x=845,y=200)
    #    Text(screen2, text="",width='20').place(x=150,y=200)
    textBox=Text(sp, height=4, width=30)
    textBox.place(x=475,y=200)
    buttonCommit=Button(sp, height=3, width=20, text="Submit",bg='brown', fg='white',command=lambda: retrieve_input()).place(x=350,y=300)

def register():
    global screen1, appname,category,rat,rev,size,installs,types,price,content,gener,lup,cver,aver 
    appname = StringVar()
    category = StringVar()
    rat = StringVar()
    rev = StringVar()
    size = StringVar()
    types = IntVar()
    installs = StringVar()
    price = StringVar()
    content = StringVar()
    gener = StringVar()
    lup = StringVar()
    cver= StringVar()
    aver = StringVar()
    screen1 = Toplevel(screen)
    screen1.title("Registeration")
    adjustWindow(screen1)

    Label(screen1, text="App Name:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=50)
    Entry(screen1, textvar=appname).place(x=150, y=50)
    Label(screen1, text="Category:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=100)
    Entry(screen1, textvar=category).place(x=150, y=100)
    Label(screen1, text="Type", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873',anchor=W).place(x=0, y=360)
    Radiobutton(screen1, text="Free", variable=types, value=1,bg='#fff4f3').place(x=150, y=360)
    Radiobutton(screen1, text="Paid", variable=types, value=2,bg='#fff4f3').place(x=210, y=360)
    Label(screen1, text="Rating :", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=310)
    Entry(screen1, textvar=rat).place(x=150, y=310)

    Label(screen1, text="Review:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=210)
    Entry(screen1, textvar=rev).place(x=150, y=210)
    Label(screen1, text="Size:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=260)
    entry_4 = Entry(screen1, textvar=size)
    entry_4.place(x=150, y=260)
    #######
    Label(screen1, text="Installs:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=160)
    Entry(screen1, textvar=installs).place(x=150, y=160)
    Label(screen1, text="Price:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=410)
    Entry(screen1, textvar=price).place(x=150, y=410)

    Label(screen1, text="Content :", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=460)
    Entry(screen1, textvar=content).place(x=150, y=460)

    Label(screen1, text="Genres:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=510)
    Entry(screen1, textvar=gener).place(x=150, y=510)
    Label(screen1, text="LAST UPDATED:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=560)
    Entry(screen1, textvar=lup).place(x=150, y=560)
    Label(screen1, text="DD/MM/YY", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=300, y=560)
    Label(screen1, text="Current version:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=610)
    Entry(screen1, textvar=cver).place(x=150, y=610)
    Label(screen1, text="Android version:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=0, y=660)
    Entry(screen1, textvar=aver).place(x=150, y=660)
    
    Button(screen1, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown',fg='white', command=register_user).place(x=700, y=600)

def register_user():
    pc=0
    if appname.get() and category.get() and  rev.get() and size.get() and rat.get() and installs.get() and  price.get() and content.get() and gener.get() and lup.get() and cver.get() and aver.get() and types.get():
        Label(screen1, text="                                  ", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=300, y=300)
        I=list(installs.get())
#        print(I)
        for i in I:
            if(i=='+'):
                pc=pc+1
                if(pc>=2):
                    Label(screen1, text="Invalid input", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=160)
                    return
            if( i.isalpha()):
#                print("why")
                Label(screen1, text="Invalid input", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=160)
                return
        Label(screen1, text="                                  ", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=160)
        r=list(rat.get())
        review12=list(rev.get())
        for i in review12:
             if(i.isalpha() or i=='.'):
                Label(screen1, text="Review should be numeric and integer form", fg="red",font=("calibri", 11), width='40', anchor=W, bg='white').place(x=220, y=210)
                return
        Label(screen1, text="                                          ", fg="red",font=("calibri", 11), width='50', anchor=W, bg='white').place(x=220, y=210)
        for i in r:
            if(i.isalpha()):
                Label(screen1, text="Rating could be numeric only", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=310)
                return
        Label(screen1, text="                                         ", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=310)
        
        rating=float(rat.get())
        if(rating>5):
            Label(screen1, text="Rating should be less than or equal to 5", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=310)
            return
        else:
            Label(screen1, text="                                           ", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=310)
        sic=list(size.get())
        j=len(sic)
        l=0
        for i in sic:
            l=l+1
            if(i.isalpha()):
                if(i=='M' or i=='K' or i=='G'):
                    break
                else:
                    Label(screen1, text="Invalid size", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=260)
                    return
            else:
                if(l==j):
                    Label(screen1, text="Please give whether size is in M-Mb or K-Kb or G-Gb", fg="red",font=("calibri", 11), width='50', anchor=W, bg='white').place(x=220, y=260)
                    return
        Label(screen1, text="                                                    ", fg="red",font=("calibri", 11), width='50', anchor=W, bg='white').place(x=220, y=260)
        if types.get()==2:
            if price.get()=='0':
                Label(screen1, text="Price  cant be 0 if selected paid", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=410)
                return
        if types.get()==1:
            if price.get()!='0':
                Label(screen1, text="Price should be zero", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=410)
                return
        Label(screen1, text="                                              ", fg="red",font=("calibri", 11), width='50', anchor=W, bg='white').place(x=220, y=410)
        curver=list(cver.get())
        for i in curver:
            if(i.isalpha()):
                Label(screen1, text="Invalid Input", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=610)
                return
        Label(screen1, text="                 ", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=220, y=610)
                
        try:
            datetime.datetime.strptime(lup.get(),'%d/%m/%Y')
        except ValueError:
            Label(screen1,text="\n").place(x=220,y=560)
            Label(screen1,text="Incorrect data format ,should be DD/MM/YYYY",font=("Courier New",12),fg="red").place(x=220,y=560)
            return
        Label(screen1,text="                                                ",font=("Courier New",12),fg="red").place(x=220,y=560)
        gender_value = 'Free'
        if types.get() == 2:
            
            gender_value = 'Paid'
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="app_data")
        cursor = connection.cursor()
        insert_query = "INSERT INTO data (App_name , Category , Rating , Reviews , Size , Installs , Type , Price , Content_rating , Genres, Last_updated , Current_ver , Android_ver) VALUES(' " + str(appname.get()) + " ' , ' "+ str(category.get()) + " ' , ' "+ str(rat.get()) + " ' , ' "+ str(rev.get()) + " ' , ' "+ str(size.get()) + " ' , ' "+ str(installs.get()) + " ' , ' "+ str(gender_value) + " ' , ' "+ str(price.get()) + " ' , '"+ str(content.get()) + "' , '"+ str(gener.get()) + "','"+ str(lup.get()) + "','"+ str(cver.get()) + "','"+ str(aver.get()) + "');"
        cursor.execute(insert_query)
        connection.commit()
        connection.close()
        Label(screen1, text="Data Entered Succesfully", fg="green", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=680)
    else:
        Label(screen1, text="Please give all data ", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=300, y=300)
        return
def main_screenok():
    global screenentry
    screenentry =Tk()
    adjustwindow(screenentry)
#    photo=PhotoImage(file="new-google-play.png")
    Button(screenentry,text="App Data",height=5,width=15,bg='black',font=("Open Sans",26,'bold'),fg='orange',command=register).place(x=175,y=150)
    Button(screenentry,text="App Review",height=5,width=15,bg='black',font=("Open Sans",26,'bold'),fg='orange',command=reg2).place(x=550,y=150)                     

def main_screen():
    global mscreen,name
    mscreen=Tk()#initializing the tkinter window
#    screen.configure(background="#000000")
    
    name=StringVar()
    mscreen.title("Welcome")
    adjustwindow(mscreen)#configuring the window
    back=Image.open("new-google-play.png")
    photo=ImageTk.PhotoImage(back)
    label1=Label(mscreen,image=photo)
    label1.pack()
    label1.image=photo
    Label(mscreen,text="Google PlayStore App Launch Study",width="70",height="3",font=("Calibri",25,'bold'),fg='white',bg='#174873').place(x=-50,y=50)
#    Label(text="",bg='white').place(x=50,y=60)
    Label(mscreen,text="Enter Name",font={"Open Sans",20,'bold'},bg='#174873',fg='white').place(x=400,y=300)
    Entry(mscreen, textvar=name).place(x=600,y=300) 
    Button(mscreen, text="Submit", bg="black", width=15, height=1, font=("Open Sans", 13, 'bold'), fg='orange',command=next_1).place(x=470,y=350) 
    Label(mscreen,text="Downloads",width="33",height="3",font={"Open Sans",20,'bold'},bg='Red',fg='white').place(x=0,y=500)
    Label(mscreen,text="Trends",width="33",height="3",font={"Open Sans",20,'bold'},bg='blue',fg='white').place(x=290,y=500)
    Label(mscreen,text="Reviews",width="33",height="3",font={"Open Sans",20,'bold'},bg='orange',fg='white').place(x=580,y=500)
    Label(mscreen,text="Relation",width="33",height="3",font={"Open Sans",20,'bold'},bg='black',fg='white').place(x=860,y=500) 
    mscreen.mainloop()

def next_1():
    if name.get():
        mscreen.destroy()
        
    else: 
        Label(mscreen, text="Please enter Name", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
        return


#def main_screen():
#    global screen
#    screen = Tk()
#
#    screen.title("Google playstore app study")
#    adjustwindow(screen)
#    Button(screen,text=" Percentage download in each category",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_1).place(x=30,y=30+30+30)
##    Button(screen,text="Data Entry",height=1,width=83,bg='#e79700',font=("Open Sans",13,'bold'),fg='white',command=register).place(x=30,y=446+92)
#    Button(screen,text=" Percentage download in each category",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_1).place(x=30,y=30+30+30)
#    Button(screen,text="Apps as per downloads",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_2).place(x=30,y=62+30+30)
#    Button(screen,text="Most and Least downloads by an category",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_3).place(x=30,y=94+30+30)       
#    Button(screen,text="Category managed to get the highest maximum average ratings",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_4).place(x=30,y=126+30+30)
#    #Button(mainscreen,text="Download trend category wise over the period",bg="#66dda5",width=83,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=30,y=158+30+30)
#    Button(screen,text="category got Most & Least Download(2016,2017,2018)",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_6).place(x=30,y=190+30+30)
#    Button(screen,text="Apps with Maximum Compatibility",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_7).place(x=30,y=222+30+30)
#    #Button(mainscreen,text="Feature 8",bg="#e79700",width=60,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=30,y=30)
#    Button(screen,text="Apps 1,00,000+ downloads and rated 4.1 or above",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_9).place(x=30,y=254+30+30)
#    Button(screen,text="quaterly download of each year",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),command=point_11,fg="white").place(x=30,y=286+30+30)
#    #Button(mainscreen,text="Highest number of install for each app(Quarterly)",bg="#66dda5",width=83,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=30,y=318+30+30)
#    Button(screen,text="Apps generated most Positive, Negative & equal Sentiments",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_12).place(x=30,y=350+30+30)
#    Button(screen,text="Relation B/W Sentiment-polarity & Sentiment-subjectivity",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_13).place(x=30,y=382+30+30)
#    Button(screen,text="Month having highest average download by apps",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_16).place(x=30,y=414+30+30)
#    Button(screen,text="Relation between size and Installs",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_17).place(x=30,y=446+30+30)
#    Button(screen,text="Next",bg="#990011",width=20,height=1,font=("Open Sans",14,'bold'),fg="white",command=main_screenok).place(x=800,y=625)       
#    Button(screen,text="10 best food App",bg="#990011",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_15).place(x=30,y=478+30+30)       
#
#    screen.mainloop()
    
#def next_1():
#    if name.get():
#        mscreen.destroy()
#        
#    else: 
#        Label(mscreen, text="Please enter Name", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
#        return
#    
    
main_screen()         


global screen
screen = Tk()

screen.title("Google playstore app study")
adjustwindow(screen)
back=Image.open("surprise.png")
photo=ImageTk.PhotoImage(back)
label1=Label(screen,image=photo)
label1.pack()
label1.image=photo

back1=Image.open("CAPTURE.PNG")
photo1=ImageTk.PhotoImage(back1)
label2=Label(screen,width='260',height='100',image=photo1)
label2.place(x=800,y=103)
label2.image=photo
label3=Label(screen,width='260',height='100',image=photo1)
label3.place(x=10,y=450)
label3.image=photo
#Button(screen,text=" Percentage download in each category",bg="#00FF00",width=83,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_1).place(x=30,y=30+30+30)
Label(screen,text="Welcome "+name.get()+ "!",bg="white",width=20,height=1,font=("Open Sans",20,'bold'),fg="#990011").place(x=30,y=30)

#    Button(screen,text="Data Entry",height=1,width=83,bg='#e79700',font=("Open Sans",13,'bold'),fg='white',command=register).place(x=30,y=446+92)
Button(screen,text=" Percentage download in each category",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_1).place(x=30,y=30+30+30)
Button(screen,text="Apps as per downloads",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_2).place(x=30,y=62+30+30)
Button(screen,text="Most and Least downloads by an category",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_3).place(x=30,y=94+30+30)       
Button(screen,text="Category managed to get the highest maximum average ratings",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_4).place(x=30,y=126+30+30)
#Button(mainscreen,text="Download trend category wise over the period",bg="#66dda5",width=83,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=30,y=158+30+30)
Button(screen,text="category got Most & Least Download(2016,2017,2018)",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_6).place(x=200,y=190+30+30)
Button(screen,text="Apps with Maximum Compatibility",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_7).place(x=200,y=222+30+30)
#Button(mainscreen,text="Feature 8",bg="#e79700",width=60,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=30,y=30)
Button(screen,text="Apps 1,00,000+ downloads and rated 4.1 or above",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_9).place(x=200,y=254+30+30)
Button(screen,text="quaterly download of each year",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),command=point_11,fg="white").place(x=200,y=286+30+30)
#Button(mainscreen,text="Highest number of install for each app(Quarterly)",bg="#66dda5",width=83,height=1,font=("Open Sans",13,'bold'),fg="white").place(x=30,y=318+30+30)
Button(screen,text="Apps generated most Positive, Negative & equal Sentiments",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_12).place(x=300,y=350+30+30)
Button(screen,text="Relation B/W Sentiment-polarity & Sentiment-subjectivity",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_13).place(x=300,y=382+30+30)
Button(screen,text="Month having highest average download by apps",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_16).place(x=300,y=414+30+30)
Button(screen,text="Relation between size and Installs",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_17).place(x=300,y=446+30+30)
Button(screen,text="Next",bg="#990011",width=20,height=1,font=("Open Sans",14,'bold'),fg="yellow",command=main_screenok).place(x=825,y=600)       
Button(screen,text="10 best food App",bg="#990011",width=60,height=1,font=("Open Sans",14,'bold'),fg="white",command=point_15).place(x=300,y=478+30+30)       

screen.mainloop()