#导入pytest
import pytest

def test_login():
    print('i am coming')

def testlogin():
    print('i am coming2')

if __name__ == '__main__':
    pytest.main(['-s','-v','test_api.py'])

