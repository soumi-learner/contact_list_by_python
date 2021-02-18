contact_list={}
while True:
    print( "================" )
    print( "1: Add Person" )
    print( "2: List People" )
    print( "3: Search Person" )
    print( "4: Delete Person" )
    print( "================" )
    print( "\n" )
    sel = input( "Pick One: " )
    if sel == "1" :
        line = input( "enter name and phone no separated by comma or 'q' to exit" )
        if line == 'q' :
            break
        name, phno = line.split( ',' )
        contact_list.update( {name : phno} )
        for x, y in contact_list.items() :
            print( x, y )
        # search from list
    if sel == "3" :
        key = input( "entre name for search" )
        if key in contact_list :
            print( 'key=', key, 'value=', contact_list[ key ] )
        else :
            print( "name not found." )
            # see list
    if sel == "2" :
           print(contact_list)
    if sel == "4" :
        print("enter name for delete contact list:")
        user_ip=input("enter the name to delete from contact list")
        if user_ip in contact_list.keys():
            del contact_list[user_ip]
        else:
            print("name doesnt found in your contact list ")



