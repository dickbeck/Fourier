Web VPython 3.2
# Web VPython: Animated Fourier Series building a square wave with extras!

scene = canvas(title='Fourier Series: Building a Square Wave',
               width=900, height=500, background=color.black)
scene.camera.pos = vector(0, 0, 5)
scene.camera.axis = vector(0, 0, -5)

# Display the formula
formula = label(pos=vector(0, 2.0, 0),
                text='f(x) =  4/π  × [sin(x) + (1/3)sin(3x) + (1/5)sin(5x) + ...]',
                height=24, box=False, color=color.white)

# Parameters
max_terms = 40
points = 400
dx = 2 * pi / points
x_vals = [(-pi + i * dx) for i in range(points + 1)]

# Draw axes
for x in range(-10, 11):
    curve(pos=[vector(x, -1.2, 0), vector(x, 1.2, 0)], color=color.gray(0.3))
for y in range(-1, 2):
    curve(pos=[vector(-pi, y, 0), vector(pi, y, 0)], color=color.gray(0.3))

# Target square wave
target_wave = curve(color=color.gray(0.5), radius=0.005)
for x in x_vals:
    y = 1 if (x % (2 * pi)) < pi else -1
    target_wave.append(vector(x, y, 0))

# Initialize labels and curves
label1 = label(pos=vector(-5, 2.2, 0), text='Fourier Terms: 1', box=False, height=16)
label2 = label(pos=vector(-5.2, 1.8, 0), text='Max Error: calculating...', box=False, height=12)
wave = curve(color=color.cyan, radius=0.02)

#brighter_yellow = vector(1.2, 1.2, 0)

error_curve = curve(color=vector(1.4, 1.4, 0), radius=0.009)

scale = 1  # Adjust as needed
# Animate the Fourier series
for term in range(1, max_terms + 1):
    wave.clear()
    error_curve.clear()

    label1.text = f'Fourier Terms: {term}'
    max_error = 0
     
    for i, x in enumerate(x_vals):
        y_sum = 0
        for n in range(1, term * 2, 2):  # Only odd harmonics
            y_sum += (4 / (n * pi)) * sin(n * x)
            
        abs_square_val = 1   #The absolute value of the square 
        if abs(y_sum) > abs_square_val:
            err = abs(y_sum)-abs_square_val
        else:
            err = abs_square_val - abs(y_sum)
        
        wrapped_x = x % (2 * pi) 
        epsilon = 1e-4  # Slightly larger to catch floating point wiggle
        if abs(x) < epsilon or abs(wrapped_x - pi) < epsilon or abs(wrapped_x - 2 * pi) < epsilon:
            err = 0  # At jump points: average of +1 and –1
         
        wave.append(vector(x, y_sum, 0))
        
        error_curve.append(vector(x, err * scale, 0))
        
        if err < .99 and err > max_error  :
            max_error = err

 
    label2.text = f'Max Error: {round(max_error, 4)}'
    scene.waitfor('click')  # Wait for a mouse click to proceed

    rate(1)