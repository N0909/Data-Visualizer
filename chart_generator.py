import pandas as pd 
import plotly.express as px 

class gen_chart():
    def __init__(self,df):
        self.df = df
        self.univariate = self.univariate(self)
        self.bivariate = self.bivariate(self)
    class univariate:
        def __init__(self,outer_instance):
            self.df = outer_instance.df

        def column(self,x_axis):
            fig = px.bar(x=self.df[x_axis].unique(),y=self.df[x_axis].value_counts(),labels=self.df[x_axis].unique())
            return fig
        
        def pie(self,name):
            fig = px.pie(names=self.df[name].unique(),values=self.df[name].value_counts())
            return fig
        
        def histplot(self,name):
            fig = px.histogram(data_frame=self.df,x=name)
            return fig
    
    class bivariate:
        def __init__(self,outer_instance):
            self.df = outer_instance.df
        def column(self,x_axis,y_axis):
            fig = px.bar(data_frame=self.df,x=x_axis,y=y_axis)
            return fig
        
        def pie(self,value,name):
            fig = px.pie(self.df,values=value,names=name)
            return fig
        
        def scatter(self,x_axis,y_axis):
            fig = px.scatter(self.df,x=x_axis,y=y_axis)
            return fig



