def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    """
    Parameters:
    n - number of disks
    from_rod - SOURCE rod (where disks are moving FROM)
    to_rod - DESTINATION rod (where disks are moving TO)  
    aux_rod - HELPER/AUXILIARY rod (temporary storage)
    """
    if n == 1:
        # Base case: Move single disk directly from source to destination
        print("Move disk 1 from rod", from_rod, "(SOURCE) to rod", to_rod, "(DESTINATION)")
        return
    
    # STEP 1: Move n-1 disks from SOURCE to HELPER (using destination as temporary)
    # SOURCE=from_rod, DESTINATION=aux_rod, HELPER=to_rod
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    
    # STEP 2: Move largest disk n from SOURCE to DESTINATION
    # SOURCE=from_rod, DESTINATION=to_rod
    print("Move disk", n, "from rod", from_rod, "(SOURCE) to rod", to_rod, "(DESTINATION)")
    
    # STEP 3: Move n-1 disks from HELPER to DESTINATION (using source as temporary)
    # SOURCE=aux_rod, DESTINATION=to_rod, HELPER=from_rod
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Test for n = 1, 2, 3, 4
print("=== n = 1 ===")
# SOURCE='A', DESTINATION='C', HELPER='B'
TowerOfHanoi(1, 'A', 'C', 'B')

print("\n=== n = 2 ===")
# SOURCE='A', DESTINATION='C', HELPER='B'
TowerOfHanoi(2, 'A', 'C', 'B')

print("\n=== n = 3 ===")
# SOURCE='A', DESTINATION='C', HELPER='B'
TowerOfHanoi(3, 'A', 'C', 'B')

print("\n=== n = 4 ===")
# SOURCE='A', DESTINATION='C', HELPER='B'
TowerOfHanoi(4, 'A', 'C', 'B')


print("\n=== n = 20 ===")
# SOURCE='A', DESTINATION='C', HELPER='B'
TowerOfHanoi(20, 'A', 'C', 'B')