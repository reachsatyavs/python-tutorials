# write a program to calculate dimension of each room, hall, kitches, etc in my house

#def <functionName>( arguments list ) -> return type:

def calculate_area( l: str , w: str , living: str ):
    print(type(l))
    print(type(w))
    area_float = l * w
    area = int(l) * int(w)
    print( f"float area: {area_float}" )
    room_name = str(living)
    print (f" Area of {room_name}: {area} sqft")
    return area


# room 1 - master bedroom 
calculate_area(12.1, 14.1, "Master Bed Room" )

# kids room 1 
#calculate_area(11, 13, "Kids Room" )

# Kitchen 
#calculate_area(15, 10, "Kitchen" )

#help(calculate_area)


def add_num( a, b):
    return ( int(a) + int(b))
    
print(f"Sum of two numbers: {add_num( 10.1, 10.2)}")

