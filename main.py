import cairo, math, random, uuid, noise
import numpy as np

file_format = "PNG"
width, height = 1000, 1000
grid_size = 100
border, mag_border = 50, 450

# lmts stands for limits, array containing the limits
lmts = [width-50, height-50, 50, 50]

N = 360 * 4
def main():
    
    # SETTING UP CONTEXT OBJECT
    
    context.set_source_rgba(0.95, 0.95, 0.95, 1)
    context.paint()
    
    #SETTING UP "CONSTANTS"
    
    PI = math.pi
    RADIUS = 400
    
    centerx = width//2
    centery = height//2
    
    # SETTING UP NOISE VARIABLES (ANGLES, CENTER, RADIUS, POS-X,Y)
    
    noisey_ = 0
    
    # SETTING UP SPACE
    x = np.linspace(-1, 0, N)
    
    # OTHER
    
    isX, isY = 0, 1
    
    # EXECUTING LOOP TO DRAW FIGURE
    
    for i in range(N):
        
        colour = 1 - (i/N)*0.5
        
        noisey_ = noise.pnoise1(x[i], octaves=8, persistence=0.7)
        
        angle = (2*PI/360 * i)
        #angle += ((noisey_*6) - 1)
        
        # CHANGING ANGLE'S DIRECTION
        if (i % 360 == 0):
            angle*= -1
            isX = isX ^ 1
            isY = isY ^ 1
            print("Pass: " + str(i))
            print("isX: " + str(isX) +"\n")
            print("isY: " + str(isY) + "\n")
            
        if (isX):
            radx_ = RADIUS * noisey_
            rady_ = RADIUS
        
        if (isY):
            radx_ = RADIUS
            rady_ = RADIUS * noisey_
            
        context.set_line_width(0.9)
        context.set_source_rgba(colour, colour, colour, 1)
        
        # RANDOMIZING CENTER
        centerx = width//2 + noisey_*100 - 50
        centery = width//2 + noisey_*100 - 50
        
        x1 = centerx + radx_ * math.cos(angle)
        y1 = centery + rady_ * math.sin(angle)

        x2 = centerx + radx_ * math.cos(angle + PI)
        y2 = centery + rady_ * math.sin(angle + PI)
        
        context.move_to(x1, y1)
        context.line_to(x2, y2)
        context.stroke()
        #print(x1,y1,x2,y2)
        
if __name__ == '__main__':
    if file_format == 'PNG':
        print("PNG")
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        context = cairo.Context(surface)
        main()
        filename = uuid.uuid4().hex[:8]
        print(filename)
        surface.write_to_png("./images/" + str(filename) + '_'+ str(int(N/360)) + '_test' + '.png')
    elif file_format == 'SVG':
        print("SVG")

     
