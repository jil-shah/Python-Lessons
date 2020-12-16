##Jil Shah
##596358
##ISC-3UO-D
##Signage jils version
##May 21st 2018
##Mr Veera
def words():
    words_fit=0  
    final_sentence=[]
    for index in range(len(sentence)):

        word = sentence[index]

        words_fit=words_fit+len(word)
        if words_fit<=limit_num:
            if words_fit+1<=limit_num:
                final_sentence.append(word)
                final_sentence.append(".")
                words_fit=words_fit+1
            else:
                final_sentence.append(sentence[index])
                print (final_sentence)
                final_sentence=[]
        elif words_fit>limit_num:
            used_space= words_fit-len(word)

            left_space= limit_num-used_space
            if left_space>0:
                for index_value in range(len(final_sentence)):
                    while left_space!=0:
                        final_sentence.insert(final_sentence, index_value, ".")
                    left_space-=1
                
                        
                    
            print (final_sentence)
            used_space=0
            words_fit=0
            final_sentence.clear
            final_sentence=[]
            final_sentence.append(word)
            final_sentence.append(".")
            words_fit=len(word)+1



        


limit_num=int(input("Enter a number:"))

sentence="WELCOME TO CCC GOOD LUCK TODAY".split(" ")

if limit_num>=30:
    print(original)
else:
    words()
