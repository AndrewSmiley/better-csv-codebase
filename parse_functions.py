__author__ = 'pridemai'
import string
"""
Function to read a file and return a string of the contents
"""

class BetterCSV:
    def make_parseable(self,string,characters):
        for search,replace_with in characters.iteritems():
                if search in string:
                    string = string.replace(search, replace_with)

        return string


    def trim_whitespace(self, string):
        return string.replace(" ","")

    def read_file(self,filename, arguments=""):
        f  = open(filename, arguments)
        values = f.read()
        f.close()
        return values


    def search(self,search_terms, search_values,threshold=0):
        valid_search_terms=[]
        valid_search_values=[]
        for s in search_terms:
            s = s.replace("("," ")
            s = s.replace(")"," ")
            s = s.replace(")"," ")
            s = s.replace(","," ")
            s = s.replace(":"," ")
            s = s.replace("/"," ")
            # s = self.make_parseable(s, {"/": " ", "(":" ",")":" ",",":" "})
            if len(s) > 4 and any(char.isdigit() for char in s):
                if "/" in s:
                    new = s.split("/")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) > 4:
                            valid_search_terms.append(sn)
                elif "," in s:
                    new = s.split(",")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_terms.append(sn)

                elif ", " in s:
                    new = s.split(", ")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_terms.append(sn)
                elif " " in s:
                    new = s.split(" ")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_terms.append(sn)
                else:
                    valid_search_terms.append(s.replace(" ",""))
        for s in search_values:
            # s = self.make_parseable(s, {"/": " ", "(":" ",")":" "})
            s = s.replace("("," ")
            s = s.replace(")"," ")
            s = s.replace(")"," ")
            s = s.replace(","," ")
            s = s.replace(":"," ")
            s = s.replace("/"," ")
            if len(s) > 4 and any(char.isdigit() for char in s):
                if "/" in s:
                    new = s.split("/")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_values.append(sn)
                elif "," in s:
                    new = s.split(",")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_values.append(sn)
                elif ", " in s:
                    new = s.split(", ")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_values.append(sn)
                elif " " in s:
                    new = s.split(" ")
                    for sn in new:
                        if len(sn) >4:
                            valid_search_values.append(sn)



                else:
                    valid_search_values.append(s.replace(" ",""))

        if len(valid_search_terms) > 0 and len(valid_search_values) > 0:
            #really want to get away from using
            if threshold != 0:
                from_end=0
                while from_end <= threshold:
                    for search_term in valid_search_terms:
                        if from_end <= 0:
                            from_end = from_end+1
                            for search_value in valid_search_values:
                                if search_term in search_value:
                                    # print "Match Found: %s in %s" % (search_term,search_value)
                                    return True
                        else:
                            from_end = from_end+1
                            for search_value in valid_search_values:
                                if search_term[:from_end*-1] in search_value:
                                    # print "Match Found: %s in %s" % (search_term,search_value)
                                    return True
            else:
                for search_term in valid_search_terms:
                    for search_value in valid_search_values:
                        if search_term in search_value:
                            # print "Match Found: %s in %s" % (search_term,search_value)
                            return True
            # print "No valid search terms :("
            # for search_value in valid_search_values:
            #     for search_term in valid_search_terms:
            #         if search_term in search_value:
            #             return True


        return False

    def get_lines(self,text_string):
        return text_string.split("\r") if len(text_string.split("\r")) > 1 else text_string.split("\n") if len(text_string.split("\n")) > 1 else text_string.split("\r\n")

    # string = "\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls"
    def get_lists(self,lines):
        arrays = []
        for string in lines:
            should_get_last = True
            last_position = 0
            line = []
            if "\"" in string:
                last_position = 0
                #print ("%s/%s" % (last_position,len(string)))
                while string[last_position:len(string)].find(",") != -1:
                    comma_pos = string[last_position:len(string)].find(",")
                    # check to see if we found a qoute
                    if "\"" in string[last_position:comma_pos+last_position]:
                        #check to see if there's a comma within the qouted string
                        first_qoute = string[last_position:].find("\"")
                        second_qoute = string[last_position+first_qoute+1:].find("\"")
                        if "," in string[first_qoute+last_position:second_qoute+last_position+1]:
                        # if (string[last_position+comma_pos:].find(",") < string[last_position+comma_pos:].find("\"")) and string[last_position+comma_pos:].find(",") != -1:
                            #yes, there's a comma in it
                            #so basically we want
                            #" $(3,562.86)",
                            first_comma = string[last_position:].find(",")+1
                            second_comma = string[last_position+first_comma:].find(",")
                            line.append(string[last_position: last_position+first_comma+second_comma])
                            last_position = last_position+first_comma+second_comma+1
                        else:
                            tmp =string[last_position:last_position+string[last_position+1:].find("\"")+2]
                            line.append(tmp)
                            # line.append(string[last_position:last_position+string[last_position:].find("\"")+1])
                            #the +1 ensures we skip passed the next one
                            last_position = string.find(tmp)+1+len(tmp)
                            # last_position = last_position+string[last_position+1:].find("\"")+1


                    #get the
                    # last_comma_pos = last_position+(comma_pos+1)
                    # comma_pos = string[last_comma_pos:].find(",")
                    # if "\"" in string[last_comma_pos:comma_pos+last_comma_pos]:
                    #     line.append(string[last_position:(comma_pos+last_comma_pos)])
                    #     last_position = (comma_pos+last_comma_pos)+1
                    # else:
                    #     line.append(string[last_position:last_comma_pos-1])
                    #     last_position = (comma_pos+last_comma_pos)+1
                    else:
                        # if last_position == 0:
                            #print(string[last_position:comma_pos])
                        if last_position < len(string) -1:
                            # has_qoutes=[string[last_position + comma_pos + 1] == '\"',string[last_position] == "\"" ]
                            if string[(last_position + comma_pos + 1) if (last_position + comma_pos + 1) < len(string) else len(string)-1] == '\"' or string[last_position] == "\"" :
                                #begin processing for qoute
                                line.append(string[last_position:comma_pos + last_position:])
                                open_qoute_pos = last_position + comma_pos + 1
                                close_qoute_pos = string[open_qoute_pos + 1:len(string)].find('\"')
                                line.append(string[open_qoute_pos:(close_qoute_pos + 2) + open_qoute_pos])
                                last_position = open_qoute_pos + close_qoute_pos + 2
                                if last_position == len(string):
                                    should_get_last = False
                                    break
                                if string[last_position] != ",":
                                    print("whoa something is fucky on line %s" % line)
                                else:
                                    #just so we start at at the character after the comma
                                    last_position = last_position + 1
                                    # #print string[open_qoute_pos:close_qoute_pos+open_qoute_pos+2]
                            else:
                                # #print "found comma at position %s" % str(last_position+comma_pos+1)

                                line.append(string[last_position:comma_pos + last_position])
                                # string = string[string.find(",")+1:]
                                #because we want to start the seardch after the comma
                                last_position = last_position + (comma_pos + 1)
                        else:
                            if string[last_position-1] == ",":
                                while string[last_position-1:len(string)].find(",") != -1:
                                    line.append(string[last_position:string[last_position+1:len(string)].find(",")])
                                    last_position = last_position+1
                                    should_get_last = False
                            else:
                                while string[last_position-1:len(string)].find(",") != -1:
                                    line.append(string[last_position:string[last_position+1:len(string)].find(",")])
                                    last_position = last_position+1
                                    should_get_last = False

                            # line.append(string[last_position:len(string)])
                    # arrays.append(line)
            else:
                #print ("nothing to do")
                arrays.append(string.split(","))
                should_get_last = False
                continue
            if should_get_last:
                line.append(string[last_position:len(string)])
            arrays.append(line)



        return  arrays

    """
    Function to get a list of dictionaries with the column names from the index_row argument
    """
    def get_dicts(self,lines,headers_row=0):
        rows = self.get_lists(lines)
        column_headers= rows[headers_row]
        dicts = []
        #in this, we're making the assumtion that the csv is consistent in column length
        for row in rows:
            dict_container={}
            i = 0
            while i < len(column_headers):
                try:
                    dict_container[column_headers[i]]=row[i]
                except IndexError as ie:
                    print "Bad index in row %s column %s: %s" % (row,i,ie)
                    return None
                i = i+1

            dicts.append(dict_container)

        #assuming that all worked, return dicts
        return dicts


    """
    Function to find the first index of a partular row (i.e. a list inside of our collection of list)
    searchterm: The string searchterm to look for
    rows: The list of lists to search in
    """
    def find_row(self, searchterm, rows):
        #todo-fill this one in
        pass

    """
    Function to the index of all rows that contain the search term
    searchterm: The string searchterm to look for
    rows: The list of lists to search in
    """
    def find_rows(self, searchterm, rows):
        indexes = []
        #todo-fill this one in
        return indexes
    """
    Function to append list_a into list_b
    """
    def append_list(self, list_a, list_b):

        #todo-fill me in
        return list_a








