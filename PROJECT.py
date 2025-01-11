import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Connection setup using psycopg2 for

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="ganesh24",
    database="retaildb"
    
)
myquery = conn.cursor()
st.markdown("""
    <style>
        
        .stApp {
            background-color:  #black;  
        }
        
        

    </style>
""", unsafe_allow_html=True)

#creating streamlit pattern

r=st.sidebar.selectbox("SELECT THE TABS",["ABOUT","Query1_to_10","Query11_to_20"]) 
r1=None
r2=None        

if r  == "ABOUT":
    st.header("MY FIRST PROJECT")
    st.subheader("This is my first project in my course of Data Science@guvi")
                 
    st.subheader("Retail_Order_Analysis")
    st.balloons()
    st.write("""
    HI,
    This is MRS.Kaladevi Senthilnathan.
    This is my first project.
    I have given mine 100% of my work.


    PROJECT 1
                   
    In a retail store, it is important to understand the sales data. 
    The sales data can provide valuable insights to the business. 
    The sales data can help the business to understand the sales performance.
     
    The main objectives of the project are:              
    To analyze and optimize sales performance .             
    Analyze the dataset to find the valuable insights .
    To understand the sales data and improve the sales performance.            
      
    This project is based on the retail dataset which contains the information about the sales of the products in the retail store    
    This dataset has been cleansed and converted into 2 dataframes and inserted into sql    
    The queries has been solved in sql and the results are displayed in streamlit
    The database contains 2 tables
    1. dataframe1
    2. dataframe2

    The database contains 20 queries
    The queries are solved using sql and displayed in streamlit
    They are displayed in the form of tables and charts
    The charts are displayed using matplotlib and plotly
    
 
     """)


    
elif r=="Query1_to_10":  

  #execution of queries from database to streamlit    

 
    r1=st.sidebar.radio("SELECT THE QUERY",["Query1","Query2","Query3","Query4","Query5","Query6","Query7","Query8","Query9","Query10"])



         

 
   
if r1 == "Query1":
     st.header(" Order the segment column with C")
    
 # Query execution with parameterized query
     myquery.execute('SELECT * FROM dataframe1 WHERE "SEGMENT" LIKE %s', ('C%',))
     result = myquery.fetchall()

# Converting the result to a pandas DataFrame for displaying in Streamlit
     df = pd.DataFrame(result, columns=[desc[0] for desc in myquery.description])

# Displaying the DataFrame in Streamlit
     st.dataframe(df)
   
   

elif r1 == "Query2":  
   st.header("List of 1st 10 MAXIMUM profit based on the Sub_category")  

 # Query execution with parameterized query    
   myquery.execute('SELECT "SUB_CATEGORY", MAX("PROFIT") AS maxprofit FROM dataframe2 GROUP BY "SUB_CATEGORY" ORDER BY MAX("PROFIT") DESC LIMIT 10')
   result = myquery.fetchall()

        # Creating the DataFrame with the correct column names
   df = pd.DataFrame(result, columns=["SUB_CATEGORY", "maxprofit"])

        # Displaying the table

   st. dataframe(df)
   
   # MATPLOTLIB  CHART
   # LINE CHART
   plt.plot(df["SUB_CATEGORY"], df["maxprofit"], color="red", marker="o", linestyle="--", label="maxprofit",)
   plt.title("Maxmum Profit Based on Sub_Category")
   plt.xticks(rotation=45)
   st.pyplot(plt)
   
       

elif r1=="Query3":
       
      myquery.execute('select "CATEGORY",Avg("SALE_PRICE"*"QUANTITY") as "AVG_SALES" from dataframe2  group by  "CATEGORY" ')
      data = myquery.fetchall()
      st.header("list of Avg sales based on category")
      df=pd.DataFrame(data,columns=("CATEGORY","AVG_SALES"))
      st.dataframe(df)
      
      # MATPLOTLIB BAR CHART
      plt.figure(figsize=(10, 6))
      plt.bar(df['CATEGORY'], df['AVG_SALES'], color="blue", label="minprofit", width=0.5)
      plt.legend()
      plt.xlabel("CATEGORY")
      plt.ylabel("AVG_SALES")
      plt.title("AVG_SALES BASED ON CATEGORY")
      st.pyplot(plt)  # Display Matplotlib chart in Streamlit

   
      
elif r1 == "Query4":
     myquery.execute('SELECT "CATEGORY", SUM("DISCOUNT") AS "TOTAL_DISCOUNT" FROM dataframe2 GROUP BY "CATEGORY" ORDER BY SUM("DISCOUNT") DESC')
     data = myquery.fetchall()
     st.header("List of total discount based on category")
     df = pd.DataFrame(data, columns=["CATEGORY", "TOTAL_DISCOUNT"])
     st.dataframe(df)
     
     
     # MATPLOTLIB PIE CHART 
     # PIE CHART
     plt.figure(figsize=(10, 6)) 
     plt.pie(df["TOTAL_DISCOUNT"], labels=df["CATEGORY"], autopct="%1.1f%%", startangle=90)
     plt.title("TOTAL Discount Based ON CATEGORY")
     st.pyplot(plt) 
     
     
        
elif  r1=="Query5":
        myquery.execute('Select "CATEGORY",AVG("SALE_PRICE") from dataframe2 group by "CATEGORY" ORDER BY AVG("SALE_PRICE") DESC')
        data=myquery.fetchall()
        st.header("List of average saleprice based on category")
        df=pd.DataFrame(data,columns=["CATEGORY","AVG_SALE_PRICE"])
        st.dataframe(df)
        
        # MATPLOTLIB SCATTER PLOT
        
        plt.figure(figsize=(10, 6))
        plt.scatter(df["CATEGORY"], df["AVG_SALE_PRICE"], color="green", marker="o", label="AVG_SALE_PRICE")  
        plt.title("Average sale price  Based on Category")
        plt.xlabel("CATEGORY") 
        plt.ylabel("AVG_SALE_PRICE")
        plt.xticks(rotation=45)
        st.pyplot(plt) 
        
elif r1=="Query6" :          
       myquery.execute('select dataframe1."REGION", AVG(dataframe2."SALE_PRICE" ) AS "AVG_SALE_PRICE" from dataframe2 join dataframe1 on	dataframe1."ORDER_ID"=dataframe2."COST_PRICE" group by "REGION" order by  AVG(dataframe2."SALE_PRICE") DESC')
       data=myquery.fetchall()
       st.header("List of Average sale price grouped by Region ")
       df=pd.DataFrame(data,columns=["REGION","AVG_SALE_PRICE"])
       st.dataframe(df)
     
       # MATPLOTLIB pie CHART
       plt.figure(figsize=(10, 6)) 
       plt.pie(df["AVG_SALE_PRICE"], labels=df["REGION"], autopct="%1.1f%%", startangle=90)
       plt.title("AVG_SALE_PRICE Based ON REGION")
       st.pyplot(plt) 
     
    
    
     
       
        
elif r1=="Query7":
     myquery.execute('select "CATEGORY", SUM("PROFIT") as "TOTAL_PROFIT"  from dataframe2 group by "CATEGORY" ORDER BY SUM("PROFIT") DESC')
     data=myquery.fetchall()
     st.header("List of Total Profit based on Category")
     df=pd.DataFrame(data,columns=["CATEGORY","Total_Profit"])
     st.dataframe(df)
     
      # MATPLOTLIB DOUGHNUT CHART
     plt.figure(figsize=(20, 10))
     fig=go.Figure(go.Pie(labels=df["CATEGORY"],values=df["Total_Profit"],hole=0.3,title="Maximum Sale_Price Based on Category"))
     st.plotly_chart(fig)
        
        
elif r1=="Query8":
     myquery.execute('select dataframe1."SEGMENT", SUM(dataframe2."QUANTITY" ) AS "HIGH_QUANTITY_ORDER" from  dataframe1 join dataframe2 on dataframe1."ORDER_ID"=dataframe2."COST_PRICE" group by "SEGMENT" order by SUM(dataframe2."QUANTITY") DESC limit 3;')
     data=myquery.fetchall()
     st.header("Table of 3 Segment with the Highest Quantity of Orders")
     df=pd.DataFrame(data,columns=["SEGMENT","HIGH_QUANTITY_ORDER"])
     st.dataframe(df)
     
     plt.plot(df["SEGMENT"], df["HIGH_QUANTITY_ORDER"], color="green", marker="o", linestyle="--", label="maxprofit",)
     plt.title("Highest quantity order  Based on Segment")
     plt.xticks(rotation=45)
     st.pyplot(plt)
        
        
elif r1=="Query9":
     myquery.execute('select dataframe1."REGION", AVG(dataframe2."DISCOUNT_PERCENT") AS "AVG_DISCOUNT" from dataframe2 RIGHT join dataframe1 on dataframe1."ORDER_ID"=dataframe2."COST_PRICE" group by "REGION" order by AVG(dataframe2."DISCOUNT_PERCENT") DESC')
     data=myquery.fetchall()
     st.header("Right Join table of Region,Discount_Per from 2 dataset to get the average discount")
     df=pd.DataFrame(data,columns=["REGION","AVG_DISCOUNT"])
     st.dataframe(df)
       
     #matplotlib histogram chart
     fig = px.histogram(df, x="REGION", y="AVG_DISCOUNT", color="REGION", title="Average Discount Percentage by Region")
     st.plotly_chart(fig)
     
 
             
elif r1=="Query10": 
    myquery.execute('select "CATEGORY", SUM(("SALE_PRICE") *("QUANTITY")) AS "SALES_REVENUE" from dataframe2 group by "CATEGORY" order by "SALES_REVENUE" ASC ;')
    result=myquery.fetchall()
    st.header("List of SALES REVENUE grouped by Category")
    df=pd.DataFrame(result, columns=[desc[0] for desc in myquery.description])
    st.dataframe(df)
      
      #matplot stacked bar chart
    fig = px.bar(df, x="CATEGORY", y="SALES_REVENUE", title="SALES REVENUE" , labels={"SALES REVENUE": "SALESREVENUE", "CATEGORY": "Category"})
    plt.xticks(rotation=45)
    plt.legend()
    st.plotly_chart(fig)


elif r=="Query11_to_20":
    r2=st.sidebar.radio("SELECT THE QUERY",["Query11","Query12","Query13","Query14","Query15","Query16","Query17","Query18","Query19","Query20"])



     
if r2 == "Query11":

    query = '''
        SELECT 
            EXTRACT(YEAR FROM df1."ORDER_DATE"::timestamp) AS year,
            SUM(df2."SALE_PRICE" * df2."QUANTITY") AS total_sales_per_year
        FROM 
            dataframe1 df1
        JOIN 
            dataframe2 df2
        ON 
            df1."ORDER_ID" = df2."COST_PRICE"
        GROUP BY 
            EXTRACT(YEAR FROM df1."ORDER_DATE"::timestamp)
        ORDER BY 
            year;
    '''
    myquery.execute(query)
    data = myquery.fetchall()

    # Displaying the results in Streamlit
    st.header("Total Revenue Generated Per Year")
    df = pd.DataFrame(data, columns=["Year", "Total Revenue"])
    st.dataframe(df)
 
       #matplotlib LINE chart

    fig = px.line(df, x="Year", y="Total Revenue", title="Total Revenue Generated Per Year", labels={"Total Revenue": "Total Revenue", "Year": "Year"})
    st.plotly_chart(fig)

   
       
elif r2 == "Query12":
       myquery.execute('select dataframe1."REGION",sum((dataframe2."QUANTITY")*(dataframe2."SALE_PRICE")) as "SALES" from  dataframe1 join   dataframe2 on  dataframe1."ORDER_ID" = dataframe2."COST_PRICE" group by "REGION" order by "SALES" desc limit 5;')
       data = myquery.fetchall()
       st.header(" sales data by region to identify which areas are performing best.")      
       df = pd.DataFrame(data, columns=["REGION","HIGHEST_SALES"])
       st.dataframe(df)
       
       #matplotlib bar chart
       fig = px.bar(df, x="REGION", y="HIGHEST_SALES", title="Total Sales by Region", labels={"HIGHEST_SALES": "Total Sales", "REGION": "Region"})
       st.plotly_chart(fig)
       
       
       
elif r2 == "Query13":
       myquery.execute('select "CATEGORY",sum("DISCOUNT_PERCENT") as DISCOUNT_PERCENT from dataframe2 group by "CATEGORY" order by DISCOUNT_PERCENT')
       data = myquery.fetchall()
       st.header(" discount percent Per Category")
       df = pd.DataFrame(data, columns=["CATEGORY","DISCOUNT_PERCENT"])
       st.dataframe(df)
       
         #matplotlib bar chart
       fig=px.bar(df,x="CATEGORY",y="DISCOUNT_PERCENT",title="discount percent",labels={"DISCOUNT_PERCENT":"discount_percent","CATEGORY":"Category"})
       plt.xticks(rotation=45)
       plt.legend()
       st.plotly_chart(fig)
              
       
               
      
      
elif r2 == "Query14":
       myquery.execute('select dataframe1."CITY",sum(dataframe2."PROFIT") as TOTAL_HIGHEST_PROFIT_per_CITY  from dataframe1 join dataframe2 on dataframe1."ORDER_ID"=dataframe2."COST_PRICE" group by "CITY" having sum(dataframe2."PROFIT")>10000 limit 5')
       data = myquery.fetchall()
       st.title("List of top 5 Cities with the Highest Profit Margins")
       df = pd.DataFrame(data, columns=["CITY","TOP5HIGHEST_PROFIT/CITY"])
       st.dataframe(df)
       
       
       # matplotlib  plot chart
       plt.plot(df["CITY"], df["TOP5HIGHEST_PROFIT/CITY"], color="green", marker="o", linestyle="--", label="maxprofit",)
       plt.title("Top 5 Cities with the Highest Profit Margins")
       plt.xticks(rotation=45)
       st.pyplot(plt)
        
          
         
   

       
       
elif  r2 == "Query15":
       myquery.execute('select dataframe1."REGION",avg(dataframe2."DISCOUNT_PERCENT") as "AVERAGE_DISCOUNT"  from dataframe2 right join dataframe1 on dataframe1."ORDER_ID"=dataframe2."COST_PRICE" group by dataframe1."REGION"')
       data = myquery.fetchall()
       st.header(" List of the Average Discount Percentage As Per Region")
       df = pd.DataFrame(data, columns=["REGION","AVERAGE_DISCOUNT"])
       st.dataframe(df)
       
       
       #MATPLOTLIB DOUGHNUT CHART
       fig = px.pie(df, values="AVERAGE_DISCOUNT", names="REGION", hole=0.3, title="Average Discount Percentage by Region")
       st.plotly_chart(fig)
       
       
       
       
elif r2 == "Query16":
       myquery.execute('select "REGION",Avg(dataframe2."SALE_PRICE") as HIGHEST_AVE_SALES_PER_PRODUCT_CATEGORY from dataframe2 join dataframe1 on dataframe1."ORDER_ID"=dataframe2."COST_PRICE" group by "REGION"')
       data = myquery.fetchall()
       st.header("List of the Average Sale Price Per Product Category")
       df = pd.DataFrame(data, columns=["REGION","AVG_SALES/PRO.CATEGORY"])
       st.dataframe(df)  
       
        #matplotlib histogram chart
       fig = px.histogram(df, x="REGION", y="AVG_SALES/PRO.CATEGORY", color="REGION", title="Average Sale Price Per Product Category by Region")
       st.plotly_chart(fig)
        
            
                  
             
elif r2 == "Query17":
    # Define the query
     query = '''
     SELECT 
        dataframe2."PRODUCT_ID",
        dataframe2."SALE_PRICE" AS sale_price,
        dataframe2."DISCOUNT" AS discount,
        dataframe2."LIST_PRICE" AS list_price,
        (dataframe2."SALE_PRICE" - dataframe2."DISCOUNT") AS "discount_impact",
        dataframe2."DISCOUNT_PERCENT"
          
     FROM dataframe2
     WHERE (dataframe2."DISCOUNT_PERCENT" )> 2
     ORDER BY "discount_impact" DESC;
     '''

    # Execute the query
     myquery.execute(query)
     data = myquery.fetchall()# Title and description


     st.title("Discount Analysis")
     st.write("This app identifies products with discounts greater than 2% and calculates the impact of discounts on sales.")


    # Convert fetched data to a DataFrame
     df = pd.DataFrame(data, columns=["PRODUCT_ID", "sale_price", "discount", "list_price", "discount_impact", "DISCOUNT_PERCENT"])

    # Check if the DataFrame is empty
     if df.empty:
        st.warning("No products found with discounts greater than 2%.")
     else:
        # Display raw data
        st.subheader("Products with Discount> 2%")
        st.dataframe(df)
       
        # Aggregate data to calculate overall impact of discounts
        summary = df.groupby("DISCOUNT_PERCENT").agg( 
        total_sales=pd.NamedAgg(column="sale_price",aggfunc="sum"), 
        total_discount_impact=pd.NamedAgg(column="discount_impact", aggfunc="sum"))
        # Display summary data
        st.subheader("Impact of Discounts on Sales")
        st.dataframe(summary)

       #matplotlib bar chart
        fig = px.bar(summary, x=summary.index, y="total_discount_impact", title="Impact of Discounts on Sales")
        st.plotly_chart(fig)
        
        

     
elif  r2 == "Query18":       
       myquery.execute('select "PRODUCT_ID",SUM(("QUANTITY")*("SALE_PRICE")) as "HIGHEST_REVENUE"  FROM dataframe2  group by "PRODUCT_ID" order by SUM(("QUANTITY")*("SALE_PRICE"))  DESC limit 10;')
       data = myquery.fetchall()
       st.header("List of the Top 10 Products with the Highest Revenue")
       df = pd.DataFrame(data, columns=["PRODUCT_ID","HIGHEST_REVENUE"])
       st.dataframe(df)  
       
      # matplotlib bar chart
       plt.figure(figsize=(8,6))
       plt.bar(df["PRODUCT_ID"],df["HIGHEST_REVENUE"],color='green',edgecolor='blue')
       plt.title('Highest Revenue by PRODUCT_ID ')
       plt.xlabel('PRODUCT_ID')
       plt.ylabel('HIGHEST REVENUE')
       plt.xticks(rotation=75)
       st.pyplot(plt)




       
elif r2 == "Query19":

      
      myquery.execute('select dataframe2."CATEGORY",SUM(dataframe2."QUANTITY") as "TOTAL_QUANTITY" from dataframe1 join dataframe2 on dataframe1."ORDER_ID"=dataframe2."COST_PRICE" GROUP BY dataframe2."CATEGORY" ORDER BY "TOTAL_QUANTITY" DESC')
      data=myquery.fetchall()
      st.title("LIST OF CATEGORY WITH TOTAL_QUANTITY")
      df=pd.DataFrame(data,columns=["CATEGORY","TOTAL_QUANTITY"])
      st.dataframe(df)

     #matplotlib line chart
      #matplotlib histogram chart
      fig = px.histogram(df, x="CATEGORY", y="TOTAL_QUANTITY", color="CATEGORY", title="TOTAL QUANTITY grouped by Category")
      st.plotly_chart(fig)
        

      

elif r2=="Query20":  
    myquery.execute('select  df2."CATEGORY",EXTRACT(YEAR FROM df1."ORDER_DATE"::timestamp) AS  "year", SUM(df2."SALE_PRICE" * df2."QUANTITY") AS total_sales FROM  dataframe1 df1 JOIN  dataframe2 df2 ON  df1."ORDER_ID" = df2."COST_PRICE"  GROUP BY  EXTRACT(YEAR FROM df1."ORDER_DATE"::timestamp),"CATEGORY"  ORDER BY "total_sales";')  
    data=myquery.fetchall()
    st.title ("list of category and year")
    df=pd.DataFrame(data,columns=["CATEGORY","year","total_sales"])
    st.dataframe(df)

    summary = df.groupby("CATEGORY").agg( 
    total_sales=pd.NamedAgg(column="total_sales",aggfunc="sum")) 
    st.subheader("TOTAL SALES GROUPED BY CATEGORY")
    st.dataframe(summary)

    fig = px.bar(summary, x=summary.index, y="total_sales", title="TOTAL SALES GROUPED BY CATEGORY")
    st.plotly_chart(fig)


    st.success('THANK YOU')
    myquery.close()
    conn.close()
    
           
  