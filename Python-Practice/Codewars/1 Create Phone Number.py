def create_phone_number(n):
    pn = "("
    for number in range(len(n)):
      pn = pn + str(n[number])
      if number == 2:
        pn = pn + ") "
      if number == 5:
        pn = pn + "-"

    return(pn)
         

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

#result best practices :0 clever:0
# best answer 
# def create_phone_number(n):
	# return "({}{}{}) {}{}{}-{}{}{}{}".format(*n) 