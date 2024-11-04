#colour definitions 
blue = color(36,151,237)
pale_yellow = color(255,253,208)
beige = color(245,245,220)
black = color(0,0,0)
white = color(255,255,255)
light_purple = color(177,156,217)
lavender = color(230,230,250)
grey = color(233,234,236)
blue_light = color(175,196,225)
blue_medium = color(70,118,208)
blue_almost = color(4,4,139)
yellow = color(255,215,0)

#background settings
background (0,0,128)
size(700,700)

#sky gradient
stroke(blue_almost)
fill(blue_almost)
strokeWeight(10)
circle(700,0,500)

stroke(blue_medium)
fill(blue_medium)
strokeWeight(10)
circle(700,0,400)

stroke(blue_light)
fill(blue_light)
strokeWeight(10)
circle(700,0,300)

#sun
stroke(yellow)
fill(yellow)
strokeWeight(10)
circle(700,0,50)

stroke(yellow)
fill(yellow)
strokeWeight(5)
line(700,0,600,50)

stroke(yellow)
fill(yellow)
strokeWeight(5)
line(700,0,690,100)

stroke(yellow)
fill(yellow)
strokeWeight(3)
line(700,0,670,50)

stroke(yellow)
fill(yellow)
strokeWeight(3)
line(700,0,610,10)

#moon
stroke(beige)
fill(beige)
strokeWeight(5)
circle(350,350,225)

stroke(pale_yellow)
fill(white)
strokeWeight(10)
circle(350,350,200)

#Star 1
stroke(pale_yellow)
strokeWeight(5)
line(50,200,100,200)

stroke(pale_yellow)
strokeWeight(5)
line(75,175,75,225)

stroke(pale_yellow)
strokeWeight(5)
line(50,175,100,225)

stroke(pale_yellow)
strokeWeight(5)
line(100,175,50,225)

#star 2
stroke(white)
strokeWeight(2)
line(500,200,500,225)

stroke(white)
strokeWeight(2)
line(487.5,212.5,512.5,212.5)

#star 3
stroke(white)
strokeWeight(2)
line(100,350,125,350)

stroke(white)
strokeWeight(2)
line(112.5,337.5,112.5,362.5)

#spots
stroke(pale_yellow)
fill(white)
strokeWeight(3)
circle(470,270,5)

stroke(white)
fill(white)
strokeWeight(3)
circle(100,500,5)

stroke(pale_yellow)
fill(pale_yellow)
strokeWeight(5)
circle(120,180,10)

#cloud 1
stroke(light_purple)
fill(light_purple)
strokeWeight(10)
circle(650,650,200)

stroke(light_purple)
fill(light_purple)
strokeWeight(10)
circle(500,650,300)

stroke(light_purple)
fill(light_purple)
strokeWeight(10)
circle(350,650,150)

stroke(light_purple)
fill(light_purple)
strokeWeight(10)
circle(250,675,150)

#cloud 2
stroke(lavender)
fill(lavender)
strokeWeight(10)
circle(100,650,250)

stroke(lavender)
fill(lavender)
strokeWeight(10)
circle(250,675,100)

stroke (lavender)
fill(lavender)
strokeWeight(10)
circle(320,690,50)

#cloud 3
stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(450,600,50)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(475,575,50)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(500,600,75)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(550,600,50)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(525,575,50)

#cloud 4
stroke(grey)
fill(grey)
strokeWeight(5)
ellipse(250,350,100,30)

stroke(grey)
fill(grey)
strokeWeight(5)
ellipse(325,330,150,40)

stroke(grey)
fill(grey)
strokeWeight(5)
ellipse(350,300,100,30)

stroke(grey)
fill(grey)
strokeWeight(5)
ellipse(375,315,100,30)

stroke(grey)
fill(grey)
strokeWeight(5)
ellipse(425,325,100,30)

#cloud 5
stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(50,50,50)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(100,0,100)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(120,60,100)

stroke(lavender)
fill(lavender)
strokeWeight(5)
circle(175,20,55)

save("CelestialDrawing.jpg")
save("CelestialDrawing.png")
