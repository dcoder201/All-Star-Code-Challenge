def str_count(strng, letter):
	return(strng.count(letter) if strng else 0)


@test.describe('Should return the correct character count')
def fixed():
    @test.it("")
    def f():
        test.assert_equals(str_count('hello', 'l'), 2)
        test.assert_equals(str_count('hello', 'e'), 1)
        test.assert_equals(str_count('codewars', 'c'), 1)
        test.assert_equals(str_count('ggggg', 'g'), 5)
        test.assert_equals(str_count('hello world', 'o'), 2)
        test.assert_equals(str_count('', 'z'), 0)
