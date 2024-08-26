import myfile

def test_pass:
  assert myfile.check_num(0) == true

def test_fail:
  assert myfile.check_num("hello") == true
  
