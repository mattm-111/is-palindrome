

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
        if o == 2:
            working_list = [x for x in s if x.isalpha()]
        if o == 3:
            working_list = [x.lower() for x in s if x.isalnum()]
        if o == 4:
            working_list = [x for x in s if x.isalpha()]
        if o == 5:

        if o == 6:

        if o == 7:
        
        
        
        
        
        if len(working_list) > 2:
            return is_palindrome_recursive("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
        return True if ( 
            (len(working_list) == 2 and 
            working_list[0] == working_list[1]) or 
            len(working_list) <= 1
            ) else False


    # def is_palindrome_recursive_case(s):
    #     working_list = [x for x in s if x.isalpha()]
    #     if len(working_list) > 2:
    #         return is_palindrome_recursive_case("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
    #     return True if ( 
    #         (len(working_list) == 2 and 
    #         working_list[0] == working_list[1]) or 
    #         len(working_list) <= 1
    #         ) else False
    

    # def is_palindrome_recursive_num(s):
    #     working_list = [x.lower() for x in s if x.isalnum()]
    #     if len(working_list) > 2:
    #         return is_palindrome_recursive_num("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
    #     return True if ( 
    #         (len(working_list) == 2 and 
    #         working_list[0] == working_list[1]) or 
    #         len(working_list) <= 1
    #         ) else False
    

    # def is_palindrome_recursive_num_case(s):
    #     working_list = [x for x in s if x.isalpha()]
    #     if len(working_list) > 2:
    #         return is_palindrome_recursive_num_case("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
    #     return True if ( 
    #         (len(working_list) == 2 and 
    #         working_list[0] == working_list[1]) or 
    #         len(working_list) <= 1
    #         ) else False


    # def is_palindrome_recursive_symb(s):
    #     working_list = [x.lower() for x in s.strip()]
    #     if len(working_list) > 2:
    #         return is_palindrome_recursive_symb("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
    #     return True if ( 
    #         (len(working_list) == 2 and 
    #         working_list[0] == working_list[1]) or 
    #         len(working_list) <= 1
    #         ) else False
    

    # def is_palindrome_recursive_symb_case(s):
    #     working_list = [x for x in s.strip()]
    #     if len(working_list) > 2:
    #         return is_palindrome_recursive_symb_case("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
    #     return True if ( 
    #         (len(working_list) == 2 and 
    #         working_list[0] == working_list[1]) or 
    #         len(working_list) <= 1
    #         ) else False
    

    # def is_palindrome_recursive_all(s):
    #     working_list = [x for x in s]
    #     if len(working_list) > 2:
    #         return is_palindrome_recursive_all("".join(working_list[1:-1])) if working_list[0] == working_list[-1] else False
    #     return True if ( 
    #         (len(working_list) == 2 and 
    #         working_list[0] == working_list[1]) or 
    #         len(working_list) <= 1
    #         ) else False


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

    
## if block that calls specific functions based on option

    if o == 1:
        try:
            answer = is_palindrome_recursive(s)
        except Exception as e:
            print(e)
    elif o == 2:
        try:
            answer = is_palindrome_recursive_case(s)
        except Exception as e:
            print(e)
    elif o == 3:
        try:
            answer = is_palindrome_recursive_num(s)
        except Exception as e:
            print(e)
    elif o == 4:
        try:
            answer = is_palindrome_recursive_num_case(s)
        except Exception as e:
            print(e)
    elif o == 5:
        try:
            answer = is_palindrome_recursive_symb(s)
        except Exception as e:
            print(e)
    elif o == 6:
        try:
            answer = is_palindrome_recursive_symb_case(s)
        except Exception as e:
            print(e)
    elif o == 7:
        try:
            answer = is_palindrome_recursive_all(s)
        except Exception as e:
            print(e)
    else:
        print(f'DEBUG INFO = Option chosen = {o}')
        fail = isinstance(o, int)
        print(f'DEBUG INFO = Is Option an INT = {fail}')
        raise Exception("Something went terribly wrong.")


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