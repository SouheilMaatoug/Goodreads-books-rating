import pandas as pd

##Two codes to adapt in functions, one tells the lines with error, the other creates "clean_books_automated.csv"
filepath='../data/books.csv'



#Code to see which lines have an error as they have one more column
df = pd.read_csv(filepath,sep=',',error_bad_lines=False)
print("Dataframe INFO")
print(" " + str(df.info()) + " " )
print( df.isnull().sum() )




# Code that will load "books_clean.csv", will open the csv as lines, identify every lines that are above the 12 columns and merge the extra author column 
# this takes from 15 secondes to 60 seconds depending on processors, could be optimized but it's automated 
# It only merges the columns that are specifically troublesome in our case, it will have to be adapted to merge other columns if needed

# hard coded header_list, to adapt to the file
header_list=["bookID","title","authors","average_rating","isbn","isbn13","language_code","  num_pages","ratings_count","text_reviews_count","publication_date","publisher"]

#Initiate dataframe with header
df=pd.DataFrame(columns=header_list)

#Open file 
with open(filepath, "r", encoding="utf-8") as f:
    #Decompose in line
    for line in f:
        line_list = line.rstrip("\n").split(",") 
        #ignore the first line (header)
        if line_list != header_list:
            #if the rows are different to 12, enter the if loop
            if len(line_list) != len(header_list):
                print(len(line_list), "columns")
                print(line_list, "\n") 
                # merge the author columns
                line_list=line_list[0:2]+[''.join(line_list[2 : 4])]+line_list[4:13]
            line_df=pd.DataFrame(data=[line_list],columns=header_list)
            df=pd.concat([df,line_df],ignore_index=True)

#Store the result in a new csv "clean_books_automated"
#df.to_csv("../data/clean_books_automated.csv",index=False)