##Jil Shah
##596358
##2 digit years to four digit years
##April 30 2018
##Mr Veera



num_lines=int(input(""))  ##input the number of lines of code that is going to be checked

months=["January","Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

finaloutput_sentence=[]

for line_num in range(num_lines):  ##loop for the number of sentences that need to be checked
    sent=input("").split() ##input a sentence from the user
    output_sentence=''   ##a new variable is set which holds a string 

    ##sent=sent.split() ## split the sentence input by the person 
    
    for i in range(len(sent)):  ## a loop for the index value of of each word in the sentence
        each_word=sent[i] ##this variable holds the word at a certain index value 
        is_not_number=0  ##this is used to check if the word is a number or not
        

        for character in range(len(each_word)):   ##this loop goes through every single character in the word 
            each_letter=each_word[character]
            if ((ord(each_letter)<46 or ord(each_letter)>57) and ord(each_letter)!=44):  ##checks if it is anything but a numbers period comma and a slash 
                is_not_number+=1  ##add 1 to the non number checker


        if is_not_number==0 and (each_word.count("/")==2):    ##if it is a number and has two slashes
            check_for_period= False  ##the boolean value is pre-set to false as the period checker's original value is false
            check_for_comma= False       ##the boolean value is pre-set to false as the comma checker's original value is false               

            if (each_word[-1]==","):    ##if the last character is a comma
                each_word=each_word.rstrip(",")    ##remove the comma
                check_for_comma==True   ## the comma checker is set to True
            elif(each_word[-1]=="."):    ## if the last character is a period
                each_word=each_word.rstrip(".")     ## removes the last character which is a period
                check_for_period= True     ##the period checker is set to True
                                   
            d_m_y= each_word.split("/")    ## the variable holds the removed slash day,month, year
            two_dig_year=d_m_y[2]       ##this holds the two digit year 

            int_month=int(d_m_y[1])   ##integer value of the month(dd/mm/yy)
            int_date=int(d_m_y[0])    ##integer value of the date (dd/mm/yy)      
            int_year= int(two_dig_year)   ##integer value of the two digit year (dd/mm/yy)


            if 1<=int_month<=12: ##if the month checker is between 1 and 12
                if int_month== 2:   ##february checker, if its the second month
                    if 1<=int_date<30:  ##if it is between 1 and less than 30
                        if int_year<=24:  ##check the year if its less than 24
                            final_year= str(int_year+2000)  ##then add 2000
                        elif int_year>=25:   ##if it is greater than 25
                            final_year= str(int_year+1900)    ##add 1900
                elif 1<=int_date<=31:  ##if the date is between 1 and 31 
                    if int_year<=24:  ##check the year if its less than 24
                        final_year= str(int_year+2000)   ##then add 2000
                    elif int_year>25:   ##if it is greater than 25
                        final_year= str(int_year+1900)    ##add 1900
                        
            if check_for_period==True:  ##if the checker for the period was selected and the original word had a period at the end 
                final_year= str(final_year+".")  ##then add the period to the changed year
            elif check_for_comma==True:   ##if the checker for the comma was selected and the original word had a comma at the end 
                final_year= str(final_year+",")   ##then add a comma to the changed year
            each_word= str(int_date)+("/") +str(int_month)+"/"+ final_year
            
        elif is_not_number==0 and each_word.count(".")==2  or each_word.count(".") ==3 and each_word[-1]==",":  ## if the word only has periods, or commas and numbers then the following will be followed
                check_for_period= False  ##the boolean value is pre-set to false as the period checker's original value is false
                check_for_comma= False       ##the boolean value is pre-set to false as the comma checker's original value is false               

                if (each_word[-1]==","):    ##if the last character is a comma
                        each_word=each_word.rstrip(",")    ##remove the comma
                        check_for_comma==True   ## the comma checker is set to True
                elif(each_word[-1]=="."):    ## if the last character is a period
                        each_word=each_word.rstrip(".")     ## removes the last character which is a period
                        check_for_period= True     ##the period checker is set to True
                                       
                y_m_d= each_word.split(".")    ## the variable holds the removed slash day,month, year
                two_dig_year=y_m_d[0]       ##this holds the two digit year 

                int_month=int(d_m_y[1])   ##integer value of the month(yy/mm/dd)
                int_date=int(d_m_y[2])    ##integer value of the date (yy/mm/dd)     
                int_year= int(two_dig_year)   ##integer value of the two digit year (yy/mm/dd)

                if 1<=int_month<=12: ##if the month checker is between 1 and 12
                    if int_month== 2:   ##february checker, if its the second month
                        if 1<=int_date<30:  ##if it is between 1 and less than 30
                            if int_year<24:  ##check the year if its less than 24
                                final_year= int_year+2000   ##then add 2000
                            elif int_year>25:   ##if it is greater than 25
                                final_year= int_year+1900    ##add 1900
                    elif 1<=int_date<=31:  ##if the date is between 1 and 31 
                        if int_year<24:  ##check the year if its less than 24
                            final_year= int_year+2000   ##then add 2000
                        elif int_year>25:   ##if it is greater than 25
                            final_year= int_year+1900    ##add 1900  
                if check_for_period==True:  ##if the checker for the period was selected and the original word had a period at the end 
                    final_year_date= final_year+ "." +int_month+"."+int_date+ "."    ##then add the periods to the correct locations and the end
                elif check_for_comma==True:   ##if the checker for the comma was selected and the original word had a comma at the end 
                    final_year_date= final_year+ "." +int_month+"."+int_date + ","    ##then add the periods to the correct locations then add a comma to the end



        else:
            if each_word in months:
                check_for_period= False  ##the boolean value is pre-set to false as the period checker's original value is false
                check_for_comma= False       ##the boolean value is pre-set to false as the comma checker's original value is false               
                indexs_required= i+3   ##the number of index's needed for the month date, year format
                if (len(sent)>=indexs_required):   ##if the length of the sentence is greater than the index needed then,
                    actual_month=(sent[i])##integer value of the month(yy/mm/dd)
                    str_date= sent[i+1]  ##the string value of the date
                    str_year=sent[i+2]
  
                                       

                    if str_date[-1]==",":   ##if the last character is a comma
                        str_date= str_date.rstrip(",")    ##remove the comma
                        if str_year[-1]==",":    ## if the last character is a comma
                            str_year= str_year.rstrip(",")  ##remove the comma
                            check_for_comma=True    ##set the comma checker to true
                        elif str_year[-1]==".": ##if the last character is a period
                            str_year= str_year.rstrip(".")   ##remove the period
                            check_for_period=True  ##set the period checker to true

                        int_date=int(str_date)    ##integer value of the date (yy/mm/dd)
                    
                        int_year= int(str_year)   ##integer value of the two digit year (yy/mm/dd)


                        if int_month== "Febuary":   ##february checker, if its the second month
                            if 1<=int_date<30:  ##if it is between 1 and less than 30
                                if int_year<24:  ##check the year if its less than 24
                                    final_year= int_year+2000   ##then add 2000
                                elif int_year>25:   ##if it is greater than 25
                                    final_year= int_year+1900    ##add 1900
                        elif 1<=int_date<=31:  ##if the date is between 1 and 31 
                            if int_year<24:  ##check the year if its less than 24
                                final_year= int_year+2000   ##then add 2000
                            elif int_year>25:   ##if it is greater than 25
                                final_year= int_year+1900    ##add 1900
                                
                        if check_for_period== True:  ##if the period checker is true
                            final_year=str(final_year)
                            final_year= str(final_year)+"."    ##set the final year to a string and add a period
                        elif check_for_comma== True:   ##if the comma checker is true
                            final_year=str(final_year)+","     ##set the final year to a string and add a comma

                        sent.pop(i+2)   ## used to remove the item from the list at 2 positions after the index value
                        sent.insert(i+2,final_year)  ##replace it with the updated final year
                        
        output_sentence=str(output_sentence+ ' ' + each_word)  ##the final sentence including the original sentence and new word
                            
                        
        
    finaloutput_sentence.append(output_sentence)  ##the output sentence is added into a list because of the multiple sentences
print (str(finaloutput_sentence)) ## the string is then printed
               
