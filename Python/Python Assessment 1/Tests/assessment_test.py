import pytest
from Code import python1

def test_one():
    assert python1.one("hi","hello") == "hello"
    assert python1.one("three", "two") == "three"
    assert python1.one("three", "hello") == "three hello"
    assert python1.one("echo", "print") == "print"
    assert python1.one("fire","rib") == "fire"

def test_two():
    assert python1.two("bertclivebert") == "clive"
    assert python1.two("xxbertfridgebertyy") == "fridge"
    assert python1.two("xxBertfridgebERtyy") == "fridge"
    assert python1.two("xxbertyy") == ""
    assert python1.two("xxbeRTyy") == ""

def test_three():
    assert python1.three(3) == "fizz"
    assert python1.three(10) == "buzz"
    assert python1.three(15) == "fizzbuzz"
    assert python1.three(8) == "null"
    assert python1.three(75) == "fizzbuzz"

def test_four():
    assert python1.four("55 72 86") == 14
    assert python1.four("15 72 80 164") == 11
    assert python1.four("555 72 86 45 10") == 15
    assert python1.four("98 63 34 1 13") == 17
    assert python1.four("98 107 415") == 17

def test_five():
    assert python1.five("Jeff,random.py,False,1445") == ["Jeff"]
    assert python1.five("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") == ["Jeff"]
    assert python1.five("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") == ["Bert","Jeff"]
    assert python1.five("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") == ["Bert","Jeff"]
    assert python1.five("Bert,files.py,True,1447,Bert,tests.py,True,1318,Jeff,app.py,True,1445") == []

def test_six():
    assert python1.six("ceiling") == True
    assert python1.six("believe") == True
    assert python1.six("glacier") == False
    assert python1.six("height") == False
    assert python1.six("receive") == True

def test_seven():
    assert python1.seven("Hello") == 2 
    assert python1.seven("hEelLoooO") == 6
    assert python1.seven("WhitEboarD") == 4
    assert python1.seven("as") == 1
    assert python1.seven("pass") == 1

def test_eight():
    assert python1.eight(1) == 1
    assert python1.eight(3) == 6
    assert python1.eight(4) == 24
    assert python1.eight(6) == 720
    assert python1.eight(8) == 40320

def test_nine():
    assert python1.nine("This is a Sentence","s") == 4
    assert python1.nine("This is a Sentence","S") == 8
    assert python1.nine("Fridge for sale","z") == -1
    assert python1.nine("I love Python", "L") == -1
    assert python1.nine("I LOVE PYTHON", "L") == 2

def test_ten():
    assert python1.ten("The",2,"h") == True
    assert python1.ten("AAbb",1,"b") == False
    assert python1.ten("Hi-There",10,"e") == False
    assert python1.ten("HEY",2,"e") == True
    assert python1.ten("on-premise",3,"-") == True
