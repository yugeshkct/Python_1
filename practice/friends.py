def friends(names):
    close_friends=[]
    for i in names:
        if len(i)==4:
            close_friends.append(i)
    print(close_friends)
        
names_list = ["Ryan", "Kieran", "Mark", "Dhivakar", "Ramu", "Arul"]
friends(names_list)

w_list=["ryan","kieran","mark","dhivakar","ramu","arul"]
friends(names_list)
    
close_friends=[]
def friend(names):
    for i in names:
        if(len(i)==4):
            close_friends.append(i)
    print(close_friends)
    