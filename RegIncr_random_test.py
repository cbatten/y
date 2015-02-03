#-------------------------------------------------------------------------
# test_random
#-------------------------------------------------------------------------

import random

def test_random( dump_vcd ):

  test_vector_table = [( 'in_', 'out*' )]
  last_result = '?'
  for i in xrange(20):
    rand_value = Bits( 8, random.randint(0,0xff) )
    test_vector_table.append( [ rand_value, last_result ] )
    last_result = Bits( 8, rand_value + 1 )

  run_test_vector_sim( RegIncr(), test_vector_table, dump_vcd )

