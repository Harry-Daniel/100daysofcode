def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formated_f_fname= f_name.title()
    formated_l_fname= l_name.title()
    return f"Result: {formated_f_fname} {formated_l_fname} "
    

print(format_name(input("What is your first name?"),input("What is your last name?")))