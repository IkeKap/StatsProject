# StatsProject

Using a Monte Carlo simulation to calculate a value for π

![2bb5d450319f0a721c07d202cc35d324](https://user-images.githubusercontent.com/24295451/48987535-e97d0480-f0ed-11e8-9820-bf6e009401e9.gif)

![2nd GIF](https://i.gyazo.com/818484a04fd1efd1ff76974a2ce36d29.gif)

## Useful definitions

1. Length of a simulation = How many points/coordinates were used in that simulation
2. Execution time = How long it takes the program to complete the simulation
3. Unit Circle = Circle of radius 1 with a center at the origin (0,0) on a standard coordinate system

## Initial goals

* Determine the association, if at all, between the accuracy of a simulation and the length of the simulation
* Determine the association, if at all, between the spread of resulting values of π and how many coordinates/points were used in the simulation
* Determine the association, if at all, between the length of the simulation and the execution time

## Description of the methodology

By definition, Monte Carlo simulations use random number sampling to obtain a desired numerical result. To understand the justification for using such a simulation to calculate an experimental value for π, one needs only a rudimentary knowledge of probability, algebra and geometry.

![unit_circle](http://mathfaculty.fullerton.edu/mathews/n2003/montecarlopi/MonteCarloPiMod/Images/MonteCarloPiMod_gr_5.gif)

The above is the unit circle inscribed inside a square. While it is technically possible to run the simulation with this figure, I decided not to for several reasons.

1. This is a larger area and the resultant data would be equivalent to data acquired from a smaller segment
2. It would be more difficult, in my view, to understand the visual representation
3. The side length of the square is double the magnitude of the circle's radius. Because of this, the calculations would be more complex

I instead opted to slice the diagram into a fourth as shown below.

![quarter_segment](https://i.stack.imgur.com/c9Qhr.png)

The area of the region inside the quarter circle is exactly equal to 1/4 the area of a full unit circle and since in this example we're using the unit circle as our baseline, the radius is equal to 1, the area of the region is as follows

<p align="center"><img src="/tex/67cfb22871d6761ae070272286973adb.svg?invert_in_darkmode&sanitize=true" align=middle width=196.7322192pt height=35.77743345pt/></p>

The area of a square in which the unit circle is inscribed is

<p align="center"><img src="/tex/bfb9de8e49725f57da9e139be7099904.svg?invert_in_darkmode&sanitize=true" align=middle width=224.07807674999998pt height=18.905967299999997pt/></p>

The area of the square in the above diagram, which is a quarter of the area of the original square is
<p align="center"><img src="/tex/b8989cfefe0511ed4bbe9ff955bd77ab.svg?invert_in_darkmode&sanitize=true" align=middle width=210.73350045pt height=33.62942055pt/></p>

With the areas determined, we can now determine the probability, if points are "placed" in the quarter square randomly, that they fall within the area of the quarter circle

<p align="center"><img src="/tex/b56895db667ad864c5b1a7da0ad1a34f.svg?invert_in_darkmode&sanitize=true" align=middle width=173.8940445pt height=38.332593749999994pt/></p>

So, by this chain of logic, we may construct a Monte Carlo simulation to determine a value for π by having the program generate 2 sets of random numbers (for the x and y dimensions) between 0 and 1. If, as the image above states, the sum of the 2 squares is less than 1, the point is counted as falling inside the area of the quarter circle. At the end, the experimental value of π is calculated by

1. Dividing the number of points inside the quarter circle by the total amount of points "thrown".
2. Multiply the ratio from above by 4, since otherwise, as the equation from above demonstrates, the result would be approaching π/4

## How the program works

I used 4 Python libraries within my program. They and their function within my program are as follows:

1. Mathplotlib.pyplot. I used this library to generate a visual representation of the data.
2. Numpy. This library was used to make arrays to store the coordinate data. That data was used to calculate the experimental value for Pi. It was also later exported to pyplot and xlsxwriter. Numpy also contained a built-in value for pi that I used to compare the experimental value against.
3. Xlsxwriter. This library was used to export my data to excel once the run is complete and the data is completely collected. One limitation of this library was that it did not support writing to pre-existing excel documents. Because of this, I split the data by run and later combined 10 runs of the same length into 1 excel document by trial, and combined those trials into 1 final document.
4. Time. I used the built-in time package to measure the execution time of a run.

Line 9 of my code is what controls the length of a run. I commented out the input section to make data collection faster for myself, but if it is desirable for you to control it via console input, feel free to uncomment it.

Once a run is completed, an excel document (with its name defined based on line 15) is generated in the root directory and a mathplot diagram is displayed. Points that fall inside the area of the curve are marked with a blue color and points that fall outside are marked with a red color to make them more distinct from one another.

## Layout of the repository

Main.<span>py is the main program. This is what I used for my data collection.

mc_pi<span>.py is a reference code that I found online at [this](https://github.com/dandrewmyers/numerical/blob/master/mc_pi.py) address. Credits for this piece of code got to @dandrewmyers. I used this code as the basis for my code but heavily modified it. As the code had no license attached, I assumed that the code was open-source. My version has the MIT license attached so the code can be used without many limitations (see LICENSE for full legalese).

Project_outline was the original project proposal I submitted to my AP Statistics teacher

The Excel Workbooks directory contains all the data that I collected in my trials. I collected 10 runs per trial of a given length. The length went from 10 to 50 to 100 etc. I could not manage to do any length greater than 100,000 points within a reasonable timeframe. The original data (untouched other than minor formatting) is categorized by length and run number.

The figure Snapshots directory stores all of the mathplot images for each run.

The tex directory is a directory used by a github app attached to this repository. Its function is to render out the LaTEX equations within the readme automatically

## Example Mathplots

The following are visual representations of the data I collected.

Respectively they are runs of length
10, 50, 100, 500, 1000, 5000, 10000, 50000, and 100000

![10pi3](https://user-images.githubusercontent.com/24295451/48963663-9ed08080-ef65-11e8-9700-e17c8e68bf84.png)

![50pi3](https://user-images.githubusercontent.com/24295451/48964276-d6ddc080-ef71-11e8-9354-1cda293f289b.png)

![100pi3](https://user-images.githubusercontent.com/24295451/48963662-9bd59000-ef65-11e8-9fea-c8dbd7c7a820.png)

![500pi3](https://user-images.githubusercontent.com/24295451/48964278-d9d8b100-ef71-11e8-89f0-b0798220a8fb.png)

![1kpi3](https://user-images.githubusercontent.com/24295451/48963661-99733600-ef65-11e8-911a-b6a4f1800a3d.png)

![5kpi3](https://user-images.githubusercontent.com/24295451/48964279-dd6c3800-ef71-11e8-8f30-bb1c4230f0c2.png)

![10kpi3](https://user-images.githubusercontent.com/24295451/48964274-d1807600-ef71-11e8-9928-e41220011b31.png)

![50kpi3](https://user-images.githubusercontent.com/24295451/48964280-e8bf6380-ef71-11e8-9aac-e62f1fa28424.png)

![100kpi3](https://user-images.githubusercontent.com/24295451/48963659-92e4be80-ef65-11e8-9da0-3cd3725eebb3.png)

## Credits

https://github.com/dandrewmyers/numerical/blob/master/mc_pi.py - My code's foundation

https://www.codecogs.com/latex/eqneditor.php - rerendered out my LaTEX equations because Github for some bizzare reason does not render LaTEX in ReadMe's

http://mathfaculty.fullerton.edu/mathews/n2003/montecarlopimod.html
https://academo.org/demos/estimating-pi-monte-carlo/
Both of these links described the math behind my program.