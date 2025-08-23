club = []

while True:
    print ("")
    choice = input("choose option")
    if choice =="1":
        club_name=input("name of club:")
        club[club_name]=set()
        print(f"club:`{club_name}`added")

        # club_memb=input("enter total members:")
        # club.append({"club":club_name,"members":club_memb})
      
    elif choice == "3":
        if club:
            print(club)    