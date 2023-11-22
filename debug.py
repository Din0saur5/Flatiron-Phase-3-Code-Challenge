#!/usr/bin/env python3
import ipdb
from lib.classes.movie import Movie
from lib.classes.viewer import Viewer
from lib.classes.review import Review



m1 = Movie(title="Avatar: The Way of Water")
v1 = Viewer(username="johndoe")
v2 = Viewer(username="janedoe")
r1 = Review(v1,m1,3)



ipdb.set_trace()