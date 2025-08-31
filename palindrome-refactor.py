

def main():

## All functions defined here

    def get_option():

        valid_options = [x for x in range(1,8)]
        print("How would you like the input processed?")
        print("1.  All whitespace, symbols and numbers removed.  Not case-sensitive.")
        print("2.  All whitespace, symbols and numbers removed.  Case-sensitive.")
        print("3.  All whitespace and symbols removed.  Not case-sensitive.")
        print("4.  All whitespace and symbols removed.  Case-sensitive.")
        print("5.  All whitespace removed.  Not case-sensitive.")
        print("6.  All whitespace removed.  Case-sensitive.")
        print("7.  Processes the string EXACTLY as entered.")
        try:
            o = int(input("Please enter an option: "))
            if o in valid_options:
                print(f'option {o} entered.')
            else:
                print(f"-------------------------\nInvalid input: {o}, Please enter a valid option.\n-------------------------")
                return get_option()
        except ValueError:
            print(f"-------------------------\nInvalid input, Please enter a valid option.\n-------------------------")
            return get_option()
        return o


        

    def is_palindrome_recursive(s,o):
        
        if o == 1: 
            working_list = [x.lower() for x in s if x.isalpha()]
        elif o == 2:
            working_list = [x for x in s if x.isalpha()]
        elif o == 3:
            working_list = [x.lower() for x in s if x.isalnum()]
        elif o == 4:
            working_list = [x for x in s if x.isalpha()]
        elif o == 5:
            working_list = [x.lower() for x in s.replace(" ","")]
        elif o == 6:
            working_list = [x for x in s.replace(" ","")]
        elif o == 7:
            working_list = [x for x in s]
        else:
            raise Exception("something went wrong")
        
        
        if len(working_list) > 2:
            return is_palindrome_recursive("".join(working_list[1:-1]), o) if working_list[0] == working_list[-1] else False
        return True if ( 
            (len(working_list) == 2 and 
            working_list[0] == working_list[1]) or 
            len(working_list) <= 1
            ) else False



## User input here

    s = input("Enter your word to find out if it is a palindrome: ")
   
    if not isinstance(s, str):
        print("Stop trying to break my stuff.  This only works with strings.")
        return
    elif not s:
        print("No input detected. Technically this IS a palindrome.......")
        return
    elif not s.strip():
        print("Spacebar mashing detected. Technically this IS a palindrome............")
        return
    else:
        o = get_option()

    
## get the answer


    try:
        answer = is_palindrome_recursive(s, o)
    except Exception as e:
        print(e)



## fun ascii art
########################


    true_art = '''
     **********   *******     **     **   ********
    /////**///   /**////**   /**    /**  /**///// 
        /**      /**   /**   /**    /**  /**      
        /**      /*******    /**    /**  /******* 
        /**      /**///**    /**    /**  /**////  
        /**      /**  //**   /**    /**  /**      
        /**      /**   //**  //*******   /********
        //       //     //    ///////    //////// 

    -----------------------
    '''

    false_art = '''
     ********       **       **          ********   ********
    /**/////       ****     /**         **//////   /**///// 
    /**           **//**    /**        /**         /**      
    /*******     **  //**   /**        /*********  /******* 
    /**////     **********  /**        ////////**  /**////  
    /**        /**//////**  /**               /**  /**      
    /**        /**     /**  /********   ********   /********
    //         //      //   ////////   ////////    //////// 

    -----------------------
    '''

##################


##answer return
    
    print(f'\n-----------------------\nIt is {answer} that "{s}" is a palindrome.')
    print(true_art) if answer else print(false_art)

      
main()