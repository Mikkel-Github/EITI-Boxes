import math

# Bin Packing Algorithm with box orientation consideration and height limit
def bin_packing(box_dimensions, mir_dimensions, max_height):
    l, w, h = box_dimensions  
    L_mir, W_mir = mir_dimensions  
    
    # Try all possible orientations of the boxes
    orientations = [
        (l, w, h),  # No rotation
        (w, l, h),  # Rotate box in the xy-plane
        (h, l, w),  # Stand box upright
        (h, w, l),  # Rotate box on its side
        (l, h, w),  # Rotate box in the other direction
        (w, h, l)   # Rotate box in the third possible way
    ]
    
    best_orientation = None
    max_boxes_per_layer = 0
    
    # Iterate over each orientation to find the best fit
    for orient in orientations:
        l_box, w_box, h_box = orient  
        
        # Calculate how many boxes fit along the length and width of the MiR
        boxes_per_length = int(L_mir // l_box)
        boxes_per_width = int(W_mir // w_box)
        boxes_in_layer = boxes_per_length * boxes_per_width 
        
        # Check if the current orientation allows more boxes in a layer
        if boxes_in_layer > max_boxes_per_layer:
            max_boxes_per_layer = boxes_in_layer
            best_orientation = orient
    
    # Once the best orientation is found, calculate the number of layers
    best_l, best_w, best_h = best_orientation
    num_layers = int(max_height // best_h)  
    total_boxes = max_boxes_per_layer * num_layers 
    
    # Calculate the actual stack height
    total_stack_height = num_layers * best_h
    
    return total_boxes, total_stack_height, best_orientation, max_boxes_per_layer, num_layers

# Stability Calculation
def calculate_stability(total_boxes, box_dimensions, mass_per_box, mir_dimensions, num_layers):
    l, w, h = box_dimensions
    L_mir, W_mir = mir_dimensions
    m_box = mass_per_box

    total_height = num_layers * h  

    cog_height = (total_height / 2) if total_height > 0 else h / 2

    total_mass = total_boxes * m_box  

    g = 9.81
    critical_tipping_accel = (W_mir / 2) * g / cog_height

    return {
        "total_height": total_height,
        "cog_height": cog_height,
        "total_mass": total_mass,
        "critical_tipping_accel": critical_tipping_accel
    }

# Safe Speed Calculation
def calculate_safe_speed(stability_data, max_speed):
    cog_height = stability_data['cog_height']
    critical_tipping_accel = stability_data['critical_tipping_accel']

    safe_speed = math.sqrt(critical_tipping_accel * (stability_data['total_mass'] / cog_height))
    safe_speed = min(safe_speed, max_speed)

    return safe_speed

# Optimized Stack and Speed Calculation Without Knowing n
def optimize_stack_and_speed(box_dimensions, mir_dimensions, mass_per_box, max_speed, max_height):
    total_boxes, total_stack_height, best_orientation, boxes_per_layer, num_layers = bin_packing(box_dimensions, mir_dimensions, max_height)
    
    # Corrected stability calculation
    stability_data = calculate_stability(total_boxes, best_orientation, mass_per_box, mir_dimensions, num_layers)
    
    # Calculate safe speed based on stability data
    safe_speed = calculate_safe_speed(stability_data, max_speed)

    return {
        "total_boxes": total_boxes,
        "total_height": stability_data['total_height'],
        "cog_height": stability_data['cog_height'],
        "total_mass": stability_data['total_mass'],
        "safe_speed": safe_speed,
        "best_orientation": best_orientation,
        "boxes_per_layer": boxes_per_layer,
        "num_layers": num_layers
    }

# Example Usage
box_dimensions = (0.4, 0.6, 0.3)  # Length, width, height
mir_dimensions = (1.2, 0.8)  # Length, width 
mass_per_box = 2  
max_speed = 1.5 
max_height = 2.5 

result = optimize_stack_and_speed(box_dimensions, mir_dimensions, mass_per_box, max_speed, max_height)

# Output results
print(f"Total Boxes: {result['total_boxes']}")
print(f"Total Stack Height: {result['total_height']} meters")
print(f"Center of Gravity (CoG) Height: {result['cog_height']} meters")
print(f"Total Mass: {result['total_mass']} kg")
print(f"Safe Speed: {result['safe_speed']} m/s")
print(f"Best Orientation: {result['best_orientation']}")
print(f"Boxes Per Layer: {result['boxes_per_layer']}")
print(f"Number of Layers: {result['num_layers']}")
