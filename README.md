# Noisey-shapes
**Description** <br>
Making the computer draw weird shapes using basic trigonometry and different species of randomness(noise). Will draw more complicated shapes eventually. <br>


The folder `images_` contains the shapes drawn by the file `main.py`.
The folder `reference_material`contains visual examples and explanations of Perlin noise implementation and how to use it in Python.


## Challenges
I got started by going through *A practical guide using Processing by Matt Pearson*. The thing is the book shows example and case studies written in processing, a sort of java-like syntax language. My struggles:
*   I use python and fortunately there is this library `python-cairo` which is documented, but very          few example online. So it was fun learning how to use this library.
*   One of the most used function in processing is the `noise()`. It returns a random value using the Perlin algorithm, (Perlin Noise). Which is quite different from python's randoms functions. Graphs are shown below. If you want to use it you need the Python `noise` library. Its quite simple to use once you learned how it works!

**Random Noise** <br>
High variance in output, not ideal for drawing smooth shapes.

![img](/images_/random_noise.png?raw=true "image")


**Perlin Noise** <br>
The variance is better looking. Perlin noise in Python is achieved using the `noise` library, see `reference_material` for how use it.

![img](/images_/perlin_noise.png?raw=true "image")

**Libraries**
*   `numpy`
*   `python-cairo`
*   `noise`

**Note** <br>
It's way easier to install all these libraries using conda instead of pip.



