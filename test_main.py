import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==100, "you have plotted the wrong number of points" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "One or more of your x-coordinates is wrong" )
  
  def test_yvalues(self) : 
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      self.assertTrue( len(this_y)==100, "you have plotted the wrong number of points" )
      for i in range( len(this_x) ) :
          self.assertTrue( (this_y[i]-np.floor(this_y[i])) < 1e-7, "one of the geometric random variables you have plotted is not an integer" )
          self.assertTrue( this_y[i]>0, "one of the geometric random variables you have plotted is less than 1" )
      mean = sum(this_y) / len(this_y) 
      bar = np.sqrt((1-prob)/(prob*prob)/100)*st.norm.ppf( (0.99 + 1) / 2 )
      self.assertTrue( np.fabs( mean - 1/prob )<bar, "you are not sampling from the correct distribution" )
