#=========================================================================
# RegIncrFlat
#=========================================================================
# This is a simple flat model for a registered incrementer. An eight-bit
# value is read from the input port, registered, incremented by two, and
# finally written to the output port.

from pymtl import *

class RegIncrFlat( Model ):

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

    # Concurrent block modeling register

    s.reg_out = Wire( Bits(8) )

    @s.tick
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_

    # Concurrent block modeling first incrementer

    s.temp = Wire( Bits(8) )

    @s.combinational
    def block2():
      s.temp.value = s.reg_out + 1

    # Concurrent block modeling second incrementer

    @s.combinational
    def block3():
      s.out.value = s.temp + 1

